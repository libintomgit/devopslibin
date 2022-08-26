grp_name = "other thing"

views= ['Dash','Welcome']

views_file = open("views.txt").read()

print(views_file)

xml_content = f'''<tsRequest>
	<workbook name="Downloads All Time" showTabs="true" >
	<project id="efae5dad-d639-4d34-ad95-d9ab239c62a5"/>
	<views>
        {views_file}
	</views>
	</workbook>
</tsRequest>'''
print(xml_content)