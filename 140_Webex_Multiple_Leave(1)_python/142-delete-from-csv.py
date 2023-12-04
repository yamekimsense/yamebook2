from info import token
from info import email
import requests, json

headers = {
    'Authorization': 'Bearer '+token
}


f = open("room_list.csv", 'r')
lines = f.readlines()
for line in lines:
    first_letter = line[0:1]
    if first_letter == "q":
        print(first_letter)
        room_id = line.split(",")[1]
        print (room_id)

        response = requests.get('https://webexapis.com/v1/memberships?roomId=' + room_id, headers=headers)

        json_load = json.loads(response.text)
        items = json_load['items']

        for each in items:
            if each['personEmail'] == email:
                #print(each['id'])

                response2 = requests.delete("https://webexapis.com/v1/memberships/" + each['id'], headers=headers)
                #print(response2.status_code)
                print(response2)

f.close()

'''
   {
      "id": "Y2lzY29zcGFyazovL3VmYzExYTUtODIzZi00YjA5LTk2NTEtYzVjZmYzZjVkYWZiOjlhZDllOGQwLThmNGQtMTFlZS1hNzk3LTViODM4OWY2MzdlYw",
      "roomId": "Y2lzY29zcGFyazo0vOWFkOWU4ZDAtOGY0ZC0xMWVlLWE3OTctNWI4Mzg5ZjYzN2Vj",
      "roomType": "group",
      "personId": "Y2lzY29zcGFya1BFT1BMRS9jYmZjMTFhNS04MjNmLTRiMDktOTY1MS1jNWNmZjNmNWRhZmI",
      "personEmail": "wankim@cisco.com",
      "personDisplayName": "Wansoo Kim",
      "personOrgId": "Y2lzY29zcGF3VzL09SR0FOSVpBVElPTi8xZWI2NWZkZi05NjQzLTQxN2YtOTk3NC1hZDcyY2FlMGUxMGY",
      "isModerator": false,
      "isMonitor": false,
      "created": "2023-11-30T06:56:36.986Z"
    },
    
    

'''