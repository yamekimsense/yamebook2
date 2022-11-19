import requests
import json

"""
Modify these please
"""
#For NXAPI to authenticate the client using client certificate, set 'client_cert_auth' to True.
#For basic authentication using username & pwd, set 'client_cert_auth' to False.
client_cert_auth=False
switchuser='admin'
switchpassword='Admin_1234!'
client_cert='PATH_TO_CLIENT_CERT_FILE'
client_private_key='PATH_TO_CLIENT_PRIVATE_KEY_FILE'
ca_cert='PATH_TO_CA_CERT_THAT_SIGNED_NXAPI_SERVER_CERT'

url='https://sandbox-nxos-1.cisco.com/ins'
myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show ip int br",
    "output_format": "json"
  }
}

if client_cert_auth is False:
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword), verify=False).json()
    print (response)
else:
    url='https://10.10.20.95/ins'
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword),cert=(client_cert,client_private_key),verify=ca_cert).json()




'''
wankim@WANKIM-M-P1E1 010-NXAPI % python3 012-nx-api-sample-modify.py 
/usr/local/lib/python3.9/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'sandbox-nxos-1.cisco.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
  warnings.warn(
{'ins_api': {'type': 'cli_show', 'version': '1.0', 'sid': 'eoc', 'outputs': {'output': {'input': 'show ip int br', 'msg': 'Success', 'code': '200', 'body': {'TABLE_intf': {'ROW_intf': [{'vrf-name-out': 'default', 'intf-name': 'Vlan100', 'proto-state': 'down', 'link-state': 'down', 'admin-state': 'down', 'iod': 12, 'prefix': '172.16.100.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Vlan101', 'proto-state': 'down', 'link-state': 'down', 'admin-state': 'down', 'iod': 11, 'prefix': '172.16.101.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Vlan102', 'proto-state': 'down', 'link-state': 'down', 'admin-state': 'down', 'iod': 10, 'prefix': '172.16.102.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Vlan103', 'proto-state': 'down', 'link-state': 'down', 'admin-state': 'down', 'iod': 9, 'prefix': '172.16.103.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Vlan104', 'proto-state': 'down', 'link-state': 'down', 'admin-state': 'down', 'iod': 8, 'prefix': '172.16.104.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Vlan105', 'proto-state': 'down', 'link-state': 'down', 'admin-state': 'down', 'iod': 7, 'prefix': '172.16.105.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Lo1', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 18, 'prefix': '172.16.0.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Lo33', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 20, 'prefix': '10.0.33.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Lo98', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 21, 'prefix': '10.98.98.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Lo99', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': 22, 'prefix': '10.99.99.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Eth1/5', 'proto-state': 'down', 'link-state': 'down', 'admin-state': 'down', 'iod': 28, 'prefix': '172.16.1.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Eth1/7', 'proto-state': 'down', 'link-state': 'down', 'admin-state': 'up', 'iod': 30, 'prefix': '4.1.1.1', 'ip-disabled': 'FALSE'}]}}}}}}
wankim@WANKIM-M-P1E1 010-NXAPI % 



'''