#Extract data from Rest API
import requests
resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=resp.json()
print(len(users))  #10
#Transform - for json file and csv file

users_json=[]
for user in users:
    users_json.append({
        'uid':user['id'],
        'name':user['username'],
        'city':user['address']['city'],
        'company':user['company']['name']
    })
    print(len(users_json))
#Load data into new json file and csv file
import json
fp1=open('users.json','w')
json.dump(users_json,fp1)