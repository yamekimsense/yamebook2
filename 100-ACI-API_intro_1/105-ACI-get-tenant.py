from z100credential import *
from z110LoginToken import *
import requests, json
requests.packages.urllib3.disable_warnings()

token = getToken(host, id, password)

payload = {}
headers = {'Cookie': "APIC-cookie=" + token}
url = f"https://{host}/api/node/class/fvTenant.json"
response = requests.request("GET", url, headers=headers, data=payload, verify=False).json()
print(json.dumps(response, indent=4))

tenants = response['imdata']
for each in tenants:
    print (each['fvTenant']['attributes']['name'])