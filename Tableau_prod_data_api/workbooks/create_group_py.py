# grp_name = "other thing"
#
#
#
#
# xml_content = f'''<tsRequest>
#     <group name="{grp_name}"
#     minimumSiteRole="explorer"/>
# </tsRequest>'''
# print(xml_content)

import requests

url = "https://tableau-staging02.corp.kwalee.com/api/3.15/sites/b6e3fb37-660e-42bd-9ada-493763ed1ff8/"

method = "groups"
method_id = ""
method_endpoint = ""
auth_key = "X-Tableau-Auth"
auth_value = "O_AqA-tpQui0V29oXfPY-w|EiAq4MlcJeiBo0freyGLGZLGPP87rOoC"
auth_atr = {f"{auth_key}":f"{auth_value}"}
url_endpoint = url + method + method_id + method_endpoint
import sys
import os
import getpass

# if sys.version[0] == '3': raw_input=input

# something1 = raw_input("whats your name")

# workbook_file_path = os.path.basename("some.txt")
# print(workbook_file_path)

# # print("\n*Publishing '{0}' to the default project as {1}*")
# password = getpass.getpass("tell me your pass")
# print(password)
# workbook_file = "somefile.twbx"
# workbook_filename, file_extension = workbook_file.split('.', 1)
# print(file_extension)
import xml.etree.ElementTree as ET
from requests.packages.urllib3.fields import RequestField
from requests.packages.urllib3.filepost import encode_multipart_formdata

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

xml_request = ET.Element('tsRequest')
workbook_element = ET.SubElement(xml_request, 'workbook', name="workbook_filename")
ET.SubElement(workbook_element, 'project', id="project_id")
xml_request = ET.tostring(xml_request)

parts = {'request_payload': ('', "xml_request", 'text/xml'),
         'tableau_workbook': ("workbook_file", "1000", 'application/octet-stream')}

payload, content_type = _make_multipart(parts)

print(content_type)