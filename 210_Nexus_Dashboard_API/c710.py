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


#
#API_test using cookies
#
cookies = {
    'AuthCookie': token,
}

response = requests.get('https://10.70.133.21/nexus/infra/api/aaa/v4/logindomains', cookies=cookies, verify=False)
print ( json.dumps( json.loads( response.text  ) , indent=4) )

print ("2==================================")

#
#API_test using headers
#
cookie_content = 'AuthCookie=' + token

headers = {
    'Cookie': cookie_content
}

response = requests.get('https://10.70.133.21/nexus/infra/api/aaa/v4/logindomains', headers=headers, verify=False)
print ( json.dumps( json.loads( response.text  ) , indent=4) )


#
#API_test using cookies and headers
#


'''
ERROR
print ("3==================================")


response = requests.get('https://<nd-node-ip>/mso/api/v1/sites', cookies=cookies, headers=headers, verify=False)

print ( json.dumps( json.loads( response.text  ) , indent=4) )
'''



'''
curl -k --request GET 'https://<nd-node-ip>/mso/api/v1/sites' \
  --header 'Cookie: AuthCookie=aaaaa'
  
  
  
 import requests

cookies = {
    'AuthCookie': 'aaaaa',
}

headers = {
    # 'Cookie': 'AuthCookie=aaaaa',
}

response = requests.get('https://<nd-node-ip>/mso/api/v1/sites', cookies=cookies, headers=headers, verify=False) 
'''