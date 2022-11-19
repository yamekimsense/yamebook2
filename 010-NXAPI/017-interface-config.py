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
    "input": "inter e 1/7 ;no sh ;no sw ;ip address 4.1.1.1 255.255.255.0",
    "output_format": "json"
  }
}

response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser, switchpassword), verify=False).json()
print (response)
