
from version import VERSION
import requests # Contains methods used to make HTTP requests
import xml.etree.ElementTree as ET # Contains methods used to build and parse XML
import sys
import re
import math
import getpass
import os

# The following packages are used to build a multi-part/mixed request.
# They are contained in the 'requests' library
from requests.packages.urllib3.fields import RequestField
from requests.packages.urllib3.filepost import encode_multipart_formdata

#####
# Move a specified workbook from a source server to a specified
# server's 'default' project by downloading workbook to a temp file.
#####

# The namespace for the REST API is 'http://tableausoftware.com/api' for Tableau Server 9.0
# or 'http://tableau.com/api' for Tableau Server 9.1 or later
xmlns = {'t': 'http://tableau.com/api'}

# The maximum size of a file that can be published in a single request is 64MB
FILESIZE_LIMIT = 1024 * 1024 * 64   # 64MB

# For when a workbook is over 64MB, break it into 5MB(standard chunk size) chunks
CHUNK_SIZE = 1024 * 1024 * 5    # 5MB

# If using python version 3.x, 'raw_input()' is changed to 'input()'
if sys.version[0] == '3': raw_input=input


class ApiCallError(Exception):
    pass


class UserDefinedFieldError(Exception):
    pass


def _encode_for_display(text):
    """
    Encodes strings so they can display as ASCII in a Windows terminal window.
    This function also encodes strings for processing by xml.etree.ElementTree functions.

    Returns an ASCII-encoded version of the text.
    Unicode characters are converted to ASCII placeholders (for example, "?").
    """
    return text.encode('ascii', errors="backslashreplace").decode('utf-8')


def _make_multipart(parts):
    """
    Creates one "chunk" for a multi-part upload

    'parts' is a dictionary that provides key-value pairs of the format name: (filename, body, content_type).

    Returns the post body and the content type string.

    For more information, see this post:
        http://stackoverflow.com/questions/26299889/how-to-post-multipart-list-of-json-xml-files-using-python-requests
    """
    mime_multipart_parts = []
    for name, (filename, blob, content_type) in parts.items():
        multipart_part = RequestField(name=name, data=blob, filename=filename)
        multipart_part.make_multipart(content_type=content_type)
        mime_multipart_parts.append(multipart_part)

    post_body, content_type = encode_multipart_formdata(mime_multipart_parts)
    content_type = ''.join(('multipart/mixed',) + content_type.partition(';')[1:])
    return post_body, content_type


def _check_status(server_response, success_code):
    """
    Checks the server response for possible errors.

    'server_response'       the response received from the server
    'success_code'          the expected success code for the response
    Throws an ApiCallError exception if the API call fails.
    """
    if server_response.status_code != success_code:
        parsed_response = ET.fromstring(server_response.text)
        # Obtain the 3 xml tags from the response: error, summary, and detail tags
        error_element = parsed_response.find('t:error', namespaces=xmlns)
        summary_element = parsed_response.find('.//t:summary', namespaces=xmlns)
        detail_element = parsed_response.find('.//t:detail', namespaces=xmlns)

        # Retrieve the error code, summary, and detail if the response contains them
        code = error_element.get('code', 'unknown') if error_element is not None else 'unknown code'
        summary = summary_element.text if summary_element is not None else 'unknown summary'
        detail = detail_element.text if detail_element is not None else 'unknown detail'
        error_message = '{0}: {1} - {2}'.format(code, summary, detail)
        raise ApiCallError(error_message)
    return


def sign_in(server, username, password, site):
    """
    Signs in to the server specified with the given credentials

    'server'   specified server address
    'username' is the name (not ID) of the user to sign in as.
               Note that most of the functions in this example require that the user
               have server administrator permissions.
    'password' is the password for the user.
    'site'     is the ID (as a string) of the site on the server to sign in to. The
               default is "", which signs in to the default site.
    Returns the authentication token and the site ID.
    """
    url = server + "/api/{0}/auth/signin".format(VERSION)

    # Builds the request
    xml_request = ET.Element('tsRequest')
    credentials_element = ET.SubElement(xml_request, 'credentials', personalAccessTokenName=username, personalAccessTokenSecret=password)
    ET.SubElement(credentials_element, 'site', contentUrl=site)
    xml_request = ET.tostring(xml_request)

    # Make the request to server
    server_response = requests.post(url, data=xml_request)
    _check_status(server_response, 200)

    # ASCII encode server response to enable displaying to console
    server_response = _encode_for_display(server_response.text)

    # Reads and parses the response
    parsed_response = ET.fromstring(server_response)

    # Gets the auth token and site ID
    token = parsed_response.find('t:credentials', namespaces=xmlns).get('token')
    site_id = parsed_response.find('.//t:site', namespaces=xmlns).get('id')
    user_id = parsed_response.find('.//t:user', namespaces=xmlns).get('id')
    return token, site_id, user_id


def sign_out(server, auth_token):
    """
    Destroys the active session and invalidates authentication token.

    'server'        specified server address
    'auth_token'    authentication token that grants user access to API calls
    """
    url = server + "/api/{0}/auth/signout".format(VERSION)
    server_response = requests.post(url, headers={'x-tableau-auth': auth_token})
    _check_status(server_response, 204)
    return


def start_upload_session(server, auth_token, site_id):
    """
    Creates a POST request that initiates a file upload session.

    'server'        specified server address
    'auth_token'    authentication token that grants user access to API calls
    'site_id'       ID of the site that the user is signed into
    Returns a session ID that is used by subsequent functions to identify the upload session.
    """
    url = server + "/api/{0}/sites/{1}/fileUploads".format(VERSION, site_id)
    server_response = requests.post(url, headers={'x-tableau-auth': auth_token})
    _check_status(server_response, 201)
    xml_response = ET.fromstring(_encode_for_display(server_response.text))
    return xml_response.find('t:fileUpload', namespaces=xmlns).get('uploadSessionId')


def get_workbook_id(server, auth_token,site_id):
    """
    Gets the id of the desired workbook to relocate.

    'server'        specified server address
    'auth_token'    authentication token that grants user access to API calls
    'user_id'       ID of user with access to workbook
    'site_id'       ID of the site that the user is signed into
    'workbook_name' name of workbook to get ID of
    Returns the workbook id and the project id that contains the workbook.
    """
    page_size = 200
    page_num = 1

    url = server + "/api/{0}/sites/{1}/workbooks".format(VERSION, site_id)
    paged_url = url + "?pageSize={0}&pageNumber={1}".format(page_size, page_num)
    server_response = requests.get(paged_url, headers={'x-tableau-auth': auth_token})
    _check_status(server_response, 200)
    xml_response = ET.fromstring(_encode_for_display(server_response.text))

    # print(server_response.text)
    out={}
    for workbook in xml_response.findall('.//t:workbook',namespaces=xmlns):
        print(workbook)
        try:
            # print(workbook.find('.//t:project',namespaces=xmlns).get('id'))
            out.update({workbook.get('id'):workbook.find('.//t:project',namespaces=xmlns).get('name')})
        except AttributeError:
            out.update({workbook.get('id'): "Default"})
            continue
    return out
    error = "Workbook not found"
    raise LookupError(error)


def get_project_id(server, auth_token, site_id, project_name):
    """
    Returns the project ID for the 'default' project on the Tableau server.

   x 'server'        specified server address
    'auth_token'    authentication token that grants user access to API calls
    'site_id'       ID of the site that the user is signed into
    """
    page_num, page_size = 1, 100  # Default paginating values

    # Builds the request
    url = server + "/api/{0}/sites/{1}/projects".format(VERSION, site_id)
    paged_url = url + "?pageSize={0}&pageNumber={1}".format(page_size, page_num)
    server_response = requests.get(paged_url, headers={'x-tableau-auth': auth_token})
    _check_status(server_response, 200)
    xml_response = ET.fromstring(_encode_for_display(server_response.text))

    # Used to determine if more requests are required to find all projects on server
    total_projects = int(xml_response.find('t:pagination', namespaces=xmlns).get('totalAvailable'))
    max_page = int(math.ceil(total_projects / page_size))

    projects = xml_response.findall('.//t:project', namespaces=xmlns)

    # Continue querying if more projects exist on the server
    for page in range(2, max_page + 1):
        paged_url = url + "?pageSize={0}&pageNumber={1}".format(page_size, page)
        server_response = requests.get(paged_url, headers={'x-tableau-auth': auth_token})
        _check_status(server_response, 200)
        xml_response = ET.fromstring(_encode_for_display(server_response.text))
        projects.extend(xml_response.findall('.//t:project', namespaces=xmlns))

    # Look through all projects to find the 'default' one
    for project in projects:
        if project.get('name') == project_name:
        # if project.get('name') == 'default' or project.get('name') == 'Default':
            return project.get('id')
    print("\tProject named 'default' was not found in {0}".format(server))


def download(server, auth_token, site_id, workbook_id):
    """
    Downloads the desired workbook from the server (temp-file).

    'server'        specified server address
    'auth_token'    authentication token that grants user access to API calls
    'site_id'       ID of the site that the user is signed into
    'workbook_id'   ID of the workbook to download
    Returns the filename of the workbook downloaded.
    """
    print("\tDownloading workbook to a temp file")
    url = server + "/api/{0}/sites/{1}/workbooks/{2}/content".format(VERSION, site_id, workbook_id)
    server_response = requests.get(url, headers={'x-tableau-auth': auth_token})
    _check_status(server_response, 200)

    # Header format: Content-Disposition: name="tableau_workbook"; filename="workbook-filename"
    filename = re.findall(r'filename="(.*)"', server_response.headers['Content-Disposition'])[0]
    with open(filename, 'wb') as f:
        f.write(server_response.content)
    return filename


def publish_workbook(server, auth_token, site_id, workbook_filename, dest_project_id):
    """
    Publishes the workbook to the desired project.

    'server'            specified server address
    'auth_token'        authentication token that grants user access to API calls
    'site_id'           ID of the site that the user is signed into
    'workbook_filename' filename of workbook to publish
    'dest_project_id'   ID of peoject to publish to
    """
    workbook_name, file_extension = workbook_filename.split('.', 1)
    workbook_size = os.path.getsize(workbook_filename)
    chunked = workbook_size >= FILESIZE_LIMIT

    # Build a general request for publishing
    xml_request = ET.Element('tsRequest')
    workbook_element = ET.SubElement(xml_request, 'workbook', name=workbook_name)
    ET.SubElement(workbook_element, 'project', id=dest_project_id)
    xml_request = ET.tostring(xml_request)

    if chunked:
        print("\tPublishing '{0}' in {1}MB chunks (workbook over 64MB):".format(workbook_name, CHUNK_SIZE / 1024000))
        # Initiates an upload session
        upload_id = start_upload_session(server, site_id, auth_token)

        # URL for PUT request to append chunks for publishing
        put_url = server + "/api/{0}/sites/{1}/fileUploads/{2}".format(VERSION, site_id, upload_id)

        # Reads and uploads chunks of the workbook
        with open(workbook_filename, 'rb') as f:
            while True:
                data = f.read(CHUNK_SIZE)
                if not data:
                    break
                payload, content_type = _make_multipart({'request_payload': ('', '', 'text/xml'),
                                                         'tableau_file': ('file', data, 'application/octet-stream')})
                print("\tPublishing a chunk...")
                server_response = requests.put(put_url, data=payload,
                                               headers={'x-tableau-auth': auth_token, "content-type": content_type})
                print(f"chunk {server_response}")
                _check_status(server_response, 200)

        # Finish building request for chunking method
        payload, content_type = _make_multipart({'request_payload': ('', xml_request, 'text/xml')})

        publish_url = server + "/api/{0}/sites/{1}/workbooks".format(VERSION, site_id)
        publish_url += "?uploadSessionId={0}".format(upload_id)
        publish_url += "&workbookType={0}&overwrite=true".format(file_extension)
    else:
        print("\tPublishing '{0}' using the all-in-one method (workbook under 64MB)".format(workbook_name))

        # Read the contents of the file to publish
        with open(workbook_filename, 'rb') as f:
            workbook_bytes = f.read()

        # Finish building request for all-in-one method
        parts = {'request_payload': ('', xml_request, 'text/xml'),
                 'tableau_workbook': (workbook_filename, workbook_bytes, 'application/octet-stream')}
        payload, content_type = _make_multipart(parts)

        publish_url = server + "/api/{0}/sites/{1}/workbooks".format(VERSION, site_id)
        publish_url += "?workbookType={0}&overwrite=true".format(file_extension)

    # Make the request to publish and check status code
    print("\tUploading...")
    server_response = requests.post(publish_url, data=payload,
                                    headers={'x-tableau-auth': auth_token, 'content-type': content_type})
    _check_status(server_response, 201)
    parsed_response = ET.fromstring(_encode_for_display(server_response.text))
    # print(parsed_response)
    # work_id = parsed_response.find('t:workbook', namespaces=xmlns).get('id')

    workbook = parsed_response.findall('.//t:workbook', namespaces=xmlns)
    print(workbook, "This is workbook from publish")
    views = workbook[0].findall('.//t:view', namespaces=xmlns)

    print(views, "This is views")
    out = []
    for view in views:
        # out.update({view.get('id'):view.get('name') })
        out.append(view.get('name'))
    # with open("publish_respose.xml", "w") as f:
    #     f.write(server_response.text)
    return out


def get_workbook_views(server, auth_token, site_id, workbook_id):
    url = server + "/api/{0}/sites/{1}/workbooks/{2}/views".format(VERSION, site_id,workbook_id)
    server_response = requests.get(url, headers={'x-tableau-auth': auth_token})
    _check_status(server_response, 200)
    xml_response = ET.fromstring(_encode_for_display(server_response.text))

    out = []
    # print(xml_response,"xml_response in get_workbook_views")
    # workbook = xml_response.findall('.//t:workbook', namespaces=xmlns)
    print("Workbook in get_workbook_views")
    views = xml_response.findall('.//t:view', namespaces=xmlns)
    for view in views:
        try:
            # print(workbook.find('.//t:project',namespaces=xmlns).get('id'))
            # out.update({view.get('id'):view.get('name')})
            out.append(view.get('name'))
        except AttributeError:
            # out.update({workbook.get('id'): "Default"})
            continue
    return out
    # error = "Workbook not found"
    # raise LookupError(error)


def update_workbook(server, auth_token, site_id, workbook_filename, dest_project_id, views):
    # views = ["Dash", "Welcome"]
    #
    # xml_request = ET.Element('tsRequest')
    # workbook_element = ET.SubElement(xml_request, 'workbook', name="workbook_name")
    # ET.SubElement(workbook_element, 'project', id="dest_project_id")
    # view_element = ET.SubElement(workbook_element, 'views')
    # for i in views:
    #     ET.SubElement(view_element, 'view', name=i, hidden="true")
    # xml_request = ET.tostring(xml_request)

    ### copied from the publish ####
    workbook_name, file_extension = workbook_filename.split('.', 1)
    workbook_size = os.path.getsize(workbook_filename)
    chunked = workbook_size >= FILESIZE_LIMIT

    # Build a general request for publishing
    xml_request = ET.Element('tsRequest')
    workbook_element = ET.SubElement(xml_request, 'workbook', name=workbook_name)
    ET.SubElement(workbook_element, 'project', id=dest_project_id)
    view_element = ET.SubElement(workbook_element, 'views')
    for i in views:
        ET.SubElement(view_element, 'view', name=i, hidden="true")
    xml_request = ET.tostring(xml_request)

    ##########################
    # xml_request = ET.Element('tsRequest')
    # workbook_element = ET.SubElement(xml_request, 'workbook', name=workbook_name)
    # ET.SubElement(workbook_element, 'project', id=dest_project_id)
    # xml_request = ET.tostring(xml_request)

    if chunked:
        print("\tPublishing '{0}' in {1}MB chunks (workbook over 64MB):".format(workbook_name, CHUNK_SIZE / 1024000))
        # Initiates an upload session
        upload_id = start_upload_session(server, site_id, auth_token)

        # URL for PUT request to append chunks for publishing
        put_url = server + "/api/{0}/sites/{1}/fileUploads/{2}".format(VERSION, site_id, upload_id)

        # Reads and uploads chunks of the workbook
        with open(workbook_filename, 'rb') as f:
            while True:
                data = f.read(CHUNK_SIZE)
                if not data:
                    break
                payload, content_type = _make_multipart({'request_payload': ('', '', 'text/xml'),
                                                         'tableau_file': ('file', data, 'application/octet-stream')})
                print("\tPublishing a chunk...")
                server_response = requests.put(put_url, data=payload,
                                               headers={'x-tableau-auth': auth_token, "content-type": content_type})
                print(f"chunk {server_response}")
                _check_status(server_response, 200)

        # Finish building request for chunking method
        payload, content_type = _make_multipart({'request_payload': ('', xml_request, 'text/xml')})

        publish_url = server + "/api/{0}/sites/{1}/workbooks".format(VERSION, site_id)
        publish_url += "?uploadSessionId={0}".format(upload_id)
        publish_url += "&workbookType={0}&overwrite=true".format(file_extension)
    else:
        print("\tPublishing '{0}' using the all-in-one method (workbook under 64MB)".format(workbook_name))

        # Read the contents of the file to publish
        with open(workbook_filename, 'rb') as f:
            workbook_bytes = f.read()

        # Finish building request for all-in-one method
        parts = {'request_payload': ('', xml_request, 'text/xml'),
                 'tableau_workbook': (workbook_filename, workbook_bytes, 'application/octet-stream')}
        payload, content_type = _make_multipart(parts)

        publish_url = server + "/api/{0}/sites/{1}/workbooks".format(VERSION, site_id)
        publish_url += "?workbookType={0}&overwrite=true".format(file_extension)

    # Make the request to publish and check status code
    print("\tUploading...")
    server_response = requests.post(publish_url, data=payload,
                                    headers={'x-tableau-auth': auth_token, 'content-type': content_type})
    _check_status(server_response, 201)

def get_project(server,auth_token, site_id):
    page_size = 100
    page_num = 1

    url = server + "/api/{0}/sites/{1}/projects".format(VERSION, site_id)
    paged_url = url + "?pageSize={0}&pageNumber={1}".format(page_size, page_num)
    server_response = requests.get(paged_url, headers={'x-tableau-auth': auth_token})
    _check_status(server_response, 200)
    xml_response = ET.fromstring(_encode_for_display(server_response.text))

    out = {}
    for project in xml_response.findall('.//t:project', namespaces=xmlns):
        if project.get("name") != "default":
            out.update({project.get('name'):project.get('description')})

    return out

def create_project(projects, server, auth_token, site_id):
    url = server + "/api/{0}/sites/{1}/projects".format(VERSION, site_id)

    # Build a general request for publishing
    for project_name, project_description in projects.items():
        xml_request = ET.Element('tsRequest')
        project_element = ET.SubElement(xml_request, 'project', name=project_name, description=project_description)
        # ET.SubElement(workbook_element, 'project', id=dest_project_id)
        xml_request = ET.tostring(xml_request)

        server_response = requests.post(url, data=xml_request, headers={'x-tableau-auth': auth_token, 'Content-Type': 'application/xml'})
        # _check_status(server_response, 200)


def main():
    ##### STEP 0: Initialization #####
    # if len(sys.argv) != 3:
    #     error = "2 arguments needed (server, username)"
    #     raise UserDefinedFieldError(error)
    source_server =  "" #raw_input("\n: source_server address")
    source_username = "" #raw_input("\n source token key: ")
    workbook_name = "" #raw_input("\nName of workbook to move: ")
    dest_server = "" #raw_input("\nDestination server: ")
    dest_username = "" #raw_input("\nDestination server token key: ")
    source_site = ""
    dest_site = ""

    print(f"\n*Moving Workbook from {source_server} to {dest_server} within same porject.")
    source_password = "" #getpass.getpass("Token for {0} on {1}: ".format(source_username, source_server))
    dest_password = "" #getpass.getpass("Token for {0} on {1}: ".format(dest_username, dest_server))
    #
    ##### STEP 1: Sign in #####
    print("\n1. Signing in to both sites to obtain authentication tokens")
    ##### Source server - returns source_auth_token, source_site_id, source_user_id
    source_auth_token, source_site_id, source_user_id = sign_in(source_server, source_username, source_password, source_site)
    # source_auth_token = "NlPGwbqYRNG4QJLHmkFiUQ|UHmuNtEYDbLphUU2g4bHXFZpbpRECPVS|2a4aaa42-86a6-4100-8848-6808f2bb1db1"
    # source_site_id = "2a4aaa42-86a6-4100-8848-6808f2bb1db1"
    # source_user_id = "795bf192-ef91-4e68-82f1-69166a2f06ee"
    ##### Destination server - returns dest_auth_token, dest_site_id, dest_user_id
    dest_auth_token, dest_site_id, dest_user_id = sign_in(dest_server, dest_username, dest_password, dest_site)

    # ##### STEP 2 NEW: Create projects in destaination  as source #####
    # print(f"\n2. Create projects in {dest_server}  from {source_server}")
    # print(f"Fetching project details from {source_server}")
    # ##### returns dict{"project_name":"project_descripiton"}
    # projects = get_project(source_server, source_auth_token, source_site_id)
    # print(f"Creating projects in {dest_server}")
    # ##### returns no value
    # create_project(projects, dest_server, dest_auth_token, dest_site_id)

    ##### STEP 3: Find workbook id with project name
    print(f"\n3. Finding all workbooks id from source server '{source_server}' and associated project name.")
    # workbook_id = "a3b7eeaa-7f7c-41c8-862d-dd9eab2a25a5"
    ##### Return {"workbook_ID": "Project_Name"}
    workbooks_project = get_workbook_id(source_server, source_auth_token, source_site_id)

    ###### STEP 4: Find Project ID at the destination server associated with workbook
    ###### From here loops for all the workbooks
    # workbooks_project = {"a3b7eeaa-7f7c-41c8-862d-dd9eab2a25a5":"All Time Downloads"}
    print(workbooks_project,"before pop")
    workbooks_project.pop("a0868fca-c29d-460d-ade4-32c925834537")
    print(workbooks_project,"After pop")
    for workbook_id, projectname in workbooks_project.items():
        print("\n4. Finding project id at {0}".format(dest_server), end=",")
        print(f" associated with workbook id: {workbook_id} and project name: {projectname}")
        ##### Returns - project id from the destination server
        dest_project_id = get_project_id(dest_server, dest_auth_token, dest_site_id, projectname)

        print(f"   Destination project ID {dest_project_id} for project name {projectname}")\

        ##### STEP 5: Download workbook #####
        print(f"\n5. Downloading the workbook for {workbook_id}", end=":")
        workbook_filename = download(source_server, source_auth_token, source_site_id, workbook_id)
        workbook_name, workbook_name_ext = workbook_filename.split('.',1)
        print(f"Downloaded the workbook ID: {workbook_id}, Name: {workbook_name}, Project Name: {projectname}")
        #dest_project_id="f56bbe80-0f34-11ed-be7e-ab95ffcad120"
        #workbook_filename="Downloads All Time.twbx"

        ##### STEP 6: Publish downloaded workbook to new site #####
        print("\n6. Publishing workbook to {0}".format(dest_server))
        publish_response_views = publish_workbook(dest_server, dest_auth_token, dest_site_id, workbook_filename, dest_project_id)

        ##### STEP 7: Getting view's for workbook from the source server  #####
        print(f"\n7. Getting views list for the {workbook_name} from {source_server}")
        source_workbook_views = get_workbook_views(source_server, source_auth_token, source_site_id, workbook_id)

        for view in source_workbook_views:
            if view in publish_response_views:
                publish_response_views.remove(view)
        print(f"Views to Hide - {publish_response_views} \n Views to Show - {source_workbook_views}\n ")

        ##### STEP 8 : Updating Workbook with view visibility #####
        ##### This will add the view names to the publish request list with hidden true and publish the workbook again####
        print(f"\n8. Updating workbook \"{workbook_name}\" with view visibility.")
        update_workbook(dest_server, dest_auth_token, dest_site_id, workbook_filename, dest_project_id, publish_response_views)

    ##### STEP 10 : Sign out #####
    print("\n9 . Signing out and invalidating the authentication token")
    # sign_out(source_server, source_auth_token)
    sign_out(dest_server, dest_auth_token)


if __name__ == "__main__":
    main()
