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
{'ins_api': {'sid': 'eoc', 'type': 'cli_conf', 'version': '1.0', 'outputs': {'output': {'body': '{"TABLE_intf": {"ROW_intf": [{"vrf-name-out": "default", "intf-name": "Eth1/1", "proto-state": "up", "link-state": "up", "admin-state": "up", "iod": "5", "prefix": "192.168.0.97", "ip-disabled": "FALSE"}, {"vrf-name-out": "default", "intf-name": "Eth1/2", "proto-state": "up", "link-state": "up", "admin-state": "up", "iod": "6", "prefix": "1.1.1.1", "ip-disabled": "FALSE"}, {"vrf-name-out": "default", "intf-name": "Eth1/3", "proto-state": "up", "link-state": "up", "admin-state": "up", "iod": "7", "prefix": "2.1.1.1", "ip-disabled": "FALSE"}]}}\n', 'code': '200', 'msg': 'Success'}}}}
wankim@WANKIM-M-P1E1 010-nx-api % 

'''