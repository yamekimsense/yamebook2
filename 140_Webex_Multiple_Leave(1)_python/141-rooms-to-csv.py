from info import token
import requests, json

headers = {
    'Authorization': 'Bearer '+token
}

response = requests.get('https://webexapis.com/v1/rooms/', headers=headers)

#print ( json.dumps( json.loads( response.text  ) , indent=4) )

json_load = json.loads( response.text  )
items = json_load['items']


f = open("room_list.csv", 'w')

for each in items:
    #print (each)
    #print (each['id'])
    if each['type'] == "group":
        data = ","+each["id"]+","+each['lastActivity']+",\"" + each['title'] + "\"\n"
        print (data)
        f.write(data)
f.close()


'''
   {
            "id": "Y2lzY29zcGFyazovL3VzL1JPT00vYWIxZDRiOTAtMzFjYi0xMWVlLWI3ODEtNTdmMzQ3NGY1Yjgz",
            "title": "rooms title",
            "type": "group",
            "isLocked": false,
            "lastActivity": "2023-08-04T05:23:07.996Z",
            "creatorId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jYThlOTQ4NS0zZDNlLTQ1ZjQtYjU4Ni1hZGE0MDcwOTJkMjA",
            "created": "2023-08-03T07:02:11.401Z",
            "ownerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8xZWI2NWZkZi05NjQzLTQxN2YtOTk3NC1hZDcyY2FlMGUxMGY",
            "isPublic": false,
            "isReadOnly": false
        },

'''