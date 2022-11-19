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
    "input": "inter e 1/8 ;no sh ;no sw ;ip address 4.1.1.1 255.255.255.0",
    "output_format": "json"
  }
}

response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser, switchpassword), verify=False).json()
print (response)


'''
wankim@WANKIM-M-P1E1 010-NXAPI % python3 017-interface-config.py 
{'ins_api': {'sid': 'eoc', 'type': 'cli_conf', 'version': '1.0', 'outputs': {'output': [{'code': '200', 'msg': 'Success', 'body': {}}, {'code': '200', 'msg': 'Success', 'body': {}}, {'code': '200', 'msg': 'Success', 'body': {}}, {'code': '400', 'msg': 'CLI execution error', 'clierror': 'overlapping network for ipv4 address: 4.1.1.1/24 on eth1/8, 4.1.1.1/24 already configured on eth1/7\n'}]}}}
wankim@WANKIM-M-P1E1 010-NXAPI %

'''