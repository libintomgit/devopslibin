import json

f = open('/Users/libintom/Desktop/Tableau_prod_data_api/data.json')

data = json.load(f)

users = data['tsResponse']['users']['user']
# ',',
with open("/Users/libintom/Desktop/Tableau_prod_data_api/all_user.csv", 'a') as f:
    for i in users:
        csv_out = (f"{i['@name']}, ChangeMe@123, {i['@fullName']}, {i['@siteRole']}, ,yes,{i['@email']}\n")
        f.write(f"{csv_out}")
        print(csv_out)
