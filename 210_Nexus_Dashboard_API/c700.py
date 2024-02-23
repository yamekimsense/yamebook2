import requests, json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

nd_node_ip = "10.70.133.21"
url = f'https://{nd_node_ip}/login'

payload = {
  "userName": "admin",
  "userPasswd": "1234Qwer",
  "domain": "DefaultAuth"
}

# Use verify=False if you are sure the target system is the system you expect and it has a self-signed certificate.
response = requests.post(url=url, json=payload, verify=False)

print ( json.dumps( json.loads( response.text  ) , indent=4) )

json_load = json.loads( response.text  )
token = json_load['jwttoken']
print (token)