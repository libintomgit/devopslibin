from version import VERSION
import requests
import xml.etree.ElementTree as ET
import sys
import re
import math
import getpass
import os

def get_porject(server, auth):
    url = server + "/api/{0}/sites/{1}/workbooks".format(VERSION, site_id)
    paged_url = url + "?pageSize={0}&pageNumber={1}".format(page_size, page_num)
    server_response = requests.get(paged_url, headers={'x-tableau-auth': auth_token})
    _check_status(server_response, 200)
    xml_response = ET.fromstring(_encode_for_display(server_response.text))