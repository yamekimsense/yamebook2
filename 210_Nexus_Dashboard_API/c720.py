import requests, json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://10.70.133.21/login'
payload = {
  "userName": "admin",
  "userPasswd": "1234Qwer",
  "domain": "DefaultAuth"
}

response = requests.post(url=url, json=payload, verify=False)
json_load = json.loads( response.text  )
token = json_load['jwttoken']

cookies = {
    'AuthCookie': token,
}

response = requests.get('https://10.70.133.21/appcenter/cisco/ndfc/api/v1/lan-fabric/rest/control/fabrics', cookies=cookies, verify=False)
print ( json.dumps( json.loads( response.text  ) , indent=4) )

print ("---------------")
json_load = json.loads( response.text  )
'''
print (json_load[0]['id'])
print (json_load[0]['fabricId'])
print (json_load[0]['fabricName'])
'''

for each in json_load:
    print(each['id'])
    print(each['fabricId'])
    print(each['fabricName'],"\n")


