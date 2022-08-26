from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson

data = readfromjson("Downloads All Time.twbx.xml.json")
print(json2xml.Json2xml(data).to_xml())