import json

f = open('Query All Groups.json')

data = json.load(f)

groups = data['tsResponse']['groups']['group']

csv_out = []
for i in groups:
    csv_out = (f"{i['@name']}")
    print(csv_out)
# ',',
# with open("/Users/libintom/Desktop/Tableau_prod_data_api/all_user.csv", 'a') as f:
#     for i in users:
#         csv_out = (f"{i['@name']}, ChangeMe@123, {i['@fullName']}, {i['@siteRole']}, ,yes,{i['@email']}\n")
#         f.write(f"{csv_out}")
#         print(csv_out)