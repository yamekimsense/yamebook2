import socket, requests, json, inspect
requests.packages.urllib3.disable_warnings()

csv_file = '021-port-list.csv'
switchuser = 'admin'
switchpassword = '1234Qwer'

#nexus command on A
#   feature nxapi
#   feature udld
#   errdisable detect cause all
#   logging server 192.168.0.4 6 use-vrf management

def lineno(): #to print line number on print
    return inspect.getlineno(inspect.getouterframes(inspect.currentframe())[-1][0])

#SYSLOG server
UDP_IP = "0.0.0.0"
UDP_PORT = 514
sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    data_string = data.decode('utf-8')
    print ("#### LINE #", lineno(), "syslog printing", addr[0], data_string)

    #detect the Error Disable
    if "ERROR_DISABLED" in data_string:
        print ("-------- ERROR DISABLE detected --------")
        port_number = data_string.split("Ethernet")[1].split(" ")[0]
        address = addr[0]
        print ("#### LINE #", lineno(), "issue switch IP and port", address, port_number)

        f = open(csv_file, 'r')
        lines = f.readlines()
        for line in lines:
            line_split = line.split(",")
            ip1   = line_split[0].replace("\n","")
            port1 = line_split[1].replace("\n","")
            ip2   = line_split[2].replace("\n","")
            port2 = line_split[3].replace("\n","")
            print ("#### LINE #", lineno(), ".csv reading", ip1, port1, ip2, port2)

            #get the pair switch/port
            if (address == ip1) and (port_number == port1):
                address_target = ip2
                port_target = port2

            if (address == ip2) and (port_number == port2):
                address_target = ip1
                port_target = port1

            print ("#### LINE #", lineno(), "pair switch and port", address_target, port_target)
        f.close()

        # API to pair switch
        url = 'https://' + address_target + '/ins'
        myheaders = {'content-type': 'application/json'}

        command = "interface e " + port_target + " ; description \"ERROR_DISABLE removed\""
        print ("#### LINE #", lineno(), "command to run", command)

        payload = {
            "ins_api": {
                "version": "1.0",
                "type": "cli_conf",
                "chunk": "0",
                "sid": "sid",
                "input": command,
                "output_format": "json"
            }
        }

        response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=(switchuser, switchpassword), verify=False)
        print("#### LINE #", lineno(), "API Response", response)
        print("#### LINE #", lineno(), "API Response body", response.text)
        print("#### LINE #", lineno(), "API Response code", response.status_code)

        i = 0

        #detect API success or not
        if response.status_code == 200:
            print ("#### LINE #", lineno(),"Success to connect")
            response_json = json.loads(response.text)
            print("#### LINE #", lineno(), "API Response json", response_json)
            response_output = response_json['ins_api']['outputs']['output']
            print("#### LINE #", lineno(), "API response each command response all", response_output)
            for each in response_output:
                print("#### LINE #", lineno(), "each command response", each['code'])
                if each['code']  == '200':
                    i = i + 0
                    print("#### LINE #", lineno(), "i value when 200", i)
                else:
                    i = i + 1
                    print("#### LINE #", lineno(), "i value when not 200", i)

            print ("#### LINE #", lineno(),"final i value", i)
            if i == 0:
                print ("#### LINE #", lineno(),"Success to config\n\n\n")
            else:
                print ("#### LINE #", lineno(),"Fail to Config\n\n\n")

''''
sample log
2022 Dec 25 19:35:57 boram %ETHPORT-5-IF_DOWN_ERROR_DISABLED: Interface Ethernet1/1 is down (Error disabled. Reason:UDLD Tx-Rx Loop)
'''

'''


#### LINE # 27 syslog printing 192.168.0.231 <189>: 2022 Dec 25 21:50:46 UTC: %ETHPORT-5-IF_DOWN_ADMIN_DOWN: Interface Ethernet1/1 is down (Administratively down)
#### LINE # 27 syslog printing 192.168.0.231 <189>: 2022 Dec 25 21:50:48 UTC: %ETHPORT-5-IF_ADMIN_UP: Interface Ethernet1/1 is admin up .
#### LINE # 27 syslog printing 192.168.0.231 <189>: 2022 Dec 25 21:50:50 UTC: %ETHPORT-5-SPEED: Interface Ethernet1/1, operational speed changed to 10 Gbps
#### LINE # 27 syslog printing 192.168.0.231 <189>: 2022 Dec 25 21:50:50 UTC: %ETHPORT-5-IF_DUPLEX: Interface Ethernet1/1, operational duplex mode changed to Full
#### LINE # 27 syslog printing 192.168.0.231 <189>: 2022 Dec 25 21:50:50 UTC: %ETHPORT-5-IF_RX_FLOW_CONTROL: Interface Ethernet1/1, operational Receive Flow Control state changed to off
#### LINE # 27 syslog printing 192.168.0.231 <189>: 2022 Dec 25 21:50:50 UTC: %ETHPORT-5-IF_TX_FLOW_CONTROL: Interface Ethernet1/1, operational Transmit Flow Control state changed to off
#### LINE # 27 syslog printing 192.168.0.231 <189>: 2022 Dec 25 21:50:50 UTC: %ETHPORT-5-IF_UP: Interface Ethernet1/1 is up in mode access
#### LINE # 27 syslog printing 192.168.0.231 <188>: 2022 Dec 25 21:50:50 UTC: %UDLD-4-UDLD_PORT_DISABLED: Interface Ethernet1/1, link error detected: transmit/receive loop.
#### LINE # 27 syslog printing 192.168.0.231 <189>: 2022 Dec 25 21:50:50 UTC: %ETHPORT-5-IF_DOWN_ERROR_DISABLED: Interface Ethernet1/1 is down (Error disabled. Reason:UDLD Tx-Rx Loop)
-------- ERROR DISABLE detected --------
#### LINE # 34 issue switch IP and port 192.168.0.231 1/1
#### LINE # 44 .csv reading 192.168.0.231 1/1 192.168.0.232 1/1
#### LINE # 55 pair switch and port 192.168.0.232 1/1
#### LINE # 63 command to run interface e 1/1 ; description "ERROR_DISABLE removed"
#### LINE # 77 API Response <Response [200]>
#### LINE # 78 API Response body {
        "ins_api":      {
                "sid":  "eoc",
                "type": "cli_conf",
                "version":      "1.0",
                "outputs":      {
                        "output":       [{
                                        "code": "200",
                                        "msg":  "Success",
                                        "body": {
                                }
                                }, {
                                        "code": "200",
                                        "msg":  "Success",
                                        "body": {
                                }
                                }]
                }
        }
}
#### LINE # 79 API Response code 200
#### LINE # 85 Success to connect
#### LINE # 87 API Response json {'ins_api': {'sid': 'eoc', 'type': 'cli_conf', 'version': '1.0', 'outputs': {'output': [{'code': '200', 'msg': 'Success', 'body': {}}, {'code': '200', 'msg': 'Success', 'body': {}}]}}}
#### LINE # 89 API response each command response all [{'code': '200', 'msg': 'Success', 'body': {}}, {'code': '200', 'msg': 'Success', 'body': {}}]
#### LINE # 91 each command response 200
#### LINE # 94 i value when 200 0
#### LINE # 91 each command response 200
#### LINE # 94 i value when 200 0
#### LINE # 99 final i value 0
#### LINE # 101 Success to config



#### LINE # 27 syslog printing 192.168.0.231 <189>: 2022 Dec 25 21:52:43 UTC: %ETHPORT-5-IF_DOWN_ERROR_DISABLED: Interface Ethernet1/1 is down (Error disabled. Reason:UDLD Tx-Rx Loop) (message repeated 1 time)
-------- ERROR DISABLE detected --------
#### LINE # 34 issue switch IP and port 192.168.0.231 1/1
#### LINE # 44 .csv reading 192.168.0.231 1/1 192.168.0.232 1/1
#### LINE # 55 pair switch and port 192.168.0.232 1/1
#### LINE # 63 command to run interface e 1/1 ; description "ERROR_DISABLE removed"
#### LINE # 77 API Response <Response [200]>
#### LINE # 78 API Response body {
        "ins_api":      {
                "sid":  "eoc",
                "type": "cli_conf",
                "version":      "1.0",
                "outputs":      {
                        "output":       [{
                                        "code": "200",
                                        "msg":  "Success",
                                        "body": {
                                }
                                }, {
                                        "code": "200",
                                        "msg":  "Success",
                                        "body": {
                                }
                                }]
                }
        }
}
#### LINE # 79 API Response code 200
#### LINE # 85 Success to connect
#### LINE # 87 API Response json {'ins_api': {'sid': 'eoc', 'type': 'cli_conf', 'version': '1.0', 'outputs': {'output': [{'code': '200', 'msg': 'Success', 'body': {}}, {'code': '200', 'msg': 'Success', 'body': {}}]}}}
#### LINE # 89 API response each command response all [{'code': '200', 'msg': 'Success', 'body': {}}, {'code': '200', 'msg': 'Success', 'body': {}}]
#### LINE # 91 each command response 200
#### LINE # 94 i value when 200 0
#### LINE # 91 each command response 200
#### LINE # 94 i value when 200 0
#### LINE # 99 final i value 0
#### LINE # 101 Success to config
'''