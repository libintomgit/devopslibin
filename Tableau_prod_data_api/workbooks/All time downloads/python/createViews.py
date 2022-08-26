
import xml.etree.ElementTree as ET # Contains methods used to build and parse XML

views=["Dash","Welcome"]

xml_request = ET.Element('tsRequest')
workbook_element = ET.SubElement(xml_request, 'workbook', name="workbook_name")
ET.SubElement(workbook_element, 'project', id="dest_project_id")
view_element = ET.SubElement(workbook_element, 'views')
for i in views:
    ET.SubElement(view_element, 'view', name=i,hidden="true")
xml_request = ET.tostring(xml_request)


print(xml_request)