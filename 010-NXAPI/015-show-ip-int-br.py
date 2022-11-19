import requests, json
requests.packages.urllib3.disable_warnings()

switchuser='admin'
switchpassword='Admin_1234!'

url='https://sandbox-nxos-1.cisco.com/ins'
myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "sid",
    "input": "show ip int br | json",
    "output_format": "json",
    "rollback": "stop-on-error"
  }
}

response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser, switchpassword), verify=False).json()
print ("=== all result ===============")
print ( json.dumps(response, indent=4, sort_keys=True) )

string = response['ins_api']['outputs']['output']['body'] #string
json_load = json.loads( string )
print ( type (json_load) )
print ("\n\n=== json_load ===============")
print ( json_load )


print ("\n\n=== each interface information===============")

for interface in json_load['TABLE_intf']['ROW_intf']:
  #print (interface)
  print (interface['intf-name'], interface['proto-state'], interface['link-state'], interface['prefix'])

'''
wankim@WANKIM-M-P1E1 010-NXAPI % python3 015-show-ip-int-br.py      
=== all result ===============
{
    "ins_api": {
        "outputs": {
            "output": {
                "body": "{\"TABLE_intf\": {\"ROW_intf\": [{\"vrf-name-out\": \"default\", \"intf-name\": \"Vlan100\", \"proto-state\": \"down\", \"link-state\": \"down\", \"admin-state\": \"down\", \"iod\": \"12\", \"prefix\": \"172.16.100.1\", \"ip-disabled\": \"FALSE\"}, {\"vrf-name-out\": \"default\", \"intf-name\": \"Vlan101\", \"proto-state\": \"down\", \"link-state\": \"down\", \"admin-state\": \"down\", \"iod\": \"11\", \"prefix\": \"172.16.101.1\", \"ip-disabled\": \"FALSE\"}, {\"vrf-name-out\": \"default\", \"intf-name\": \"Vlan102\", \"proto-state\": \"down\", \"link-state\": \"down\", \"admin-state\": \"down\", \"iod\": \"10\", \"prefix\": \"172.16.102.1\", \"ip-disabled\": \"FALSE\"}, {\"vrf-name-out\": \"default\", \"intf-name\": \"Vlan103\", \"proto-state\": \"down\", \"link-state\": \"down\", \"admin-state\": \"down\", \"iod\": \"9\", \"prefix\": \"172.16.103.1\", \"ip-disabled\": \"FALSE\"}, {\"vrf-name-out\": \"default\", \"intf-name\": \"Vlan104\", \"proto-state\": \"down\", \"link-state\": \"down\", \"admin-state\": \"down\", \"iod\": \"8\", \"prefix\": \"172.16.104.1\", \"ip-disabled\": \"FALSE\"}, {\"vrf-name-out\": \"default\", \"intf-name\": \"Vlan105\", \"proto-state\": \"down\", \"link-state\": \"down\", \"admin-state\": \"down\", \"iod\": \"7\", \"prefix\": \"172.16.105.1\", \"ip-disabled\": \"FALSE\"}, {\"vrf-name-out\": \"default\", \"intf-name\": \"Lo1\", \"proto-state\": \"up\", \"link-state\": \"up\", \"admin-state\": \"up\", \"iod\": \"18\", \"prefix\": \"172.16.0.1\", \"ip-disabled\": \"FALSE\"}, {\"vrf-name-out\": \"default\", \"intf-name\": \"Lo33\", \"proto-state\": \"up\", \"link-state\": \"up\", \"admin-state\": \"up\", \"iod\": \"20\", \"prefix\": \"10.0.33.1\", \"ip-disabled\": \"FALSE\"}, {\"vrf-name-out\": \"default\", \"intf-name\": \"Lo98\", \"proto-state\": \"up\", \"link-state\": \"up\", \"admin-state\": \"up\", \"iod\": \"21\", \"prefix\": \"10.98.98.1\", \"ip-disabled\": \"FALSE\"}, {\"vrf-name-out\": \"default\", \"intf-name\": \"Lo99\", \"proto-state\": \"up\", \"link-state\": \"up\", \"admin-state\": \"up\", \"iod\": \"22\", \"prefix\": \"10.99.99.1\", \"ip-disabled\": \"FALSE\"}, {\"vrf-name-out\": \"default\", \"intf-name\": \"Eth1/5\", \"proto-state\": \"down\", \"link-state\": \"down\", \"admin-state\": \"down\", \"iod\": \"28\", \"prefix\": \"172.16.1.1\", \"ip-disabled\": \"FALSE\"}, {\"vrf-name-out\": \"default\", \"intf-name\": \"Eth1/7\", \"proto-state\": \"down\", \"link-state\": \"down\", \"admin-state\": \"up\", \"iod\": \"30\", \"prefix\": \"4.1.1.1\", \"ip-disabled\": \"FALSE\"}]}}\n",
                "code": "200",
                "msg": "Success"
            }
        },
        "sid": "eoc",
        "type": "cli_conf",
        "version": "1.0"
    }
}
<class 'dict'>


=== json_load ===============
{'TABLE_intf': {'ROW_intf': [{'vrf-name-out': 'default', 'intf-name': 'Vlan100', 'proto-state': 'down', 'link-state': 'down', 'admin-state': 'down', 'iod': '12', 'prefix': '172.16.100.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Vlan101', 'proto-state': 'down', 'link-state': 'down', 'admin-state': 'down', 'iod': '11', 'prefix': '172.16.101.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Vlan102', 'proto-state': 'down', 'link-state': 'down', 'admin-state': 'down', 'iod': '10', 'prefix': '172.16.102.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Vlan103', 'proto-state': 'down', 'link-state': 'down', 'admin-state': 'down', 'iod': '9', 'prefix': '172.16.103.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Vlan104', 'proto-state': 'down', 'link-state': 'down', 'admin-state': 'down', 'iod': '8', 'prefix': '172.16.104.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Vlan105', 'proto-state': 'down', 'link-state': 'down', 'admin-state': 'down', 'iod': '7', 'prefix': '172.16.105.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Lo1', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': '18', 'prefix': '172.16.0.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Lo33', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': '20', 'prefix': '10.0.33.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Lo98', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': '21', 'prefix': '10.98.98.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Lo99', 'proto-state': 'up', 'link-state': 'up', 'admin-state': 'up', 'iod': '22', 'prefix': '10.99.99.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Eth1/5', 'proto-state': 'down', 'link-state': 'down', 'admin-state': 'down', 'iod': '28', 'prefix': '172.16.1.1', 'ip-disabled': 'FALSE'}, {'vrf-name-out': 'default', 'intf-name': 'Eth1/7', 'proto-state': 'down', 'link-state': 'down', 'admin-state': 'up', 'iod': '30', 'prefix': '4.1.1.1', 'ip-disabled': 'FALSE'}]}}


=== each interface information===============
Vlan100 down down 172.16.100.1
Vlan101 down down 172.16.101.1
Vlan102 down down 172.16.102.1
Vlan103 down down 172.16.103.1
Vlan104 down down 172.16.104.1
Vlan105 down down 172.16.105.1
Lo1 up up 172.16.0.1
Lo33 up up 10.0.33.1
Lo98 up up 10.98.98.1
Lo99 up up 10.99.99.1
Eth1/5 down down 172.16.1.1
Eth1/7 down down 4.1.1.1
wankim@WANKIM-M-P1E1 010-NXAPI % 


'''