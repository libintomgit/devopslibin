VERSION = "3.4"
server_url = ""
token_name = ""
token_key = ""
site_name = ""
# auth_token = ""
# site_id = ""
def _encode_for_display(text):
    """
    Encodes strings so they can display as ASCII in a Windows terminal window.
    This function also encodes strings for processing by xml.etree.ElementTree functions.

    Returns an ASCII-encoded version of the text.
    Unicode characters are converted to ASCII placeholders (for example, "?").
    """
    return text.encode('ascii', errors="backslashreplace").decode('utf-8')

def sign_in(server, username, password, site):
    url = server + "/api/{0}/auth/signin".format(VERSION)

    ## Builds the request
    xml_request = ET.Element('tsRequest')
    credentials_element = ET.SubElement(xml_request, 'credentials', personalAccessTokenName=username, personalAccessTokenSecret=password)
    ET.SubElement(credentials_element, 'site', contentUrl=site)
    xml_request = ET.tostring(xml_request)

    ## Make the request to server
    server_response = requests.post(url, data=xml_request)
    _check_status(server_response, 200)

    ## ASCII encode server response to enable displaying to console
    server_response = _encode_for_display(server_response.text)

    # Reads and parses the response
    parsed_response = ET.fromstring(server_response)
    token = parsed_response.find('t:credentials', namespaces=xmlns).get('token')
    site_id = parsed_response.find('.//t:site', namespaces=xmlns).get('id')
    user_id = parsed_response.find('.//t:user', namespaces=xmlns).get('id')
    return token, site_id, user_id

def workbook_list(server, auth_token, site_id, workbook_name):
# def workbook_list(server, auth_token, user_id, site_id, workbook_name):
    url = server + "/api/{0}/sites/{1}/workbooks".format(VERSION, site_id)
    # url = server + "/api/{0}/sites/{1}/users/{2}/workbooks".format(VERSION, site_id, user_id)
    server_response = requests.get(url, headers={'x-tableau-auth': auth_token})
    # _check_status(server_response, 200)
    xml_response = ET.fromstring(_encode_for_display(server_response.text))
    print(xml_response)
    workbooks = xml_response.findall('.//t:workbook', namespaces=xmlns)
    with open("workbook_name_id.txt", "a") as file:
        for workbook in workbooks:
            file.write(f"{workbook}, {workbook.get('id')})
            # if workbook.get('name') == workbook_name:
            #     return workbook.get('id')
    # error = "Workbook named '{0}' not found.".format(workbook_name)
    # raise LookupError(error)

sign_in(server_url, token_name, token_key, site_name)