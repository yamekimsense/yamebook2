import requests, json, inspect
requests.packages.urllib3.disable_warnings()

def lineno():  # to print line number on print
  return inspect.getlineno(inspect.getouterframes(inspect.currentframe())[-1][0])

def nxapicall(ip_address, switchuser, switchpassword, command):
    print ("\n\n\n---------------------- def nxapicall ---------------------")
    print("#### LINE #", lineno(), "def nxapicall data from ", ip_address, switchuser, switchpassword, command)
    url='https://' + ip_address + '/ins'
    print("#### LINE #", lineno(), "def nxapicall URL is ", url)

    myheaders={'content-type':'application/json'}
    payload={
      "ins_api": {
        "version": "1.0",
        "type": "cli_conf",
        "chunk": "0",
        "sid": "sid",
        "input": command,
        "output_format": "json"
      }
    }

    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword), verify=False)
    print (response)
    print (response.text)

    print("#### LINE #", lineno(), "def nxapicall API Response", response)
    print("#### LINE #", lineno(), "def nxapicall Response body", response.text)
    print("#### LINE #", lineno(), "def nxapicall Response code", response.status_code)

    i = 0

    # detect API success or not
    if response.status_code == 200:
        print("#### LINE #", lineno(), "def nxapicall Success to connect")
        response_json = json.loads(response.text)
        print("#### LINE #", lineno(), "def nxapicall API Response json", response_json)
        response_output = response_json['ins_api']['outputs']['output']
        print("#### LINE #", lineno(), "def nxapicall API response each command response all", response_output)
        print("#### LINE #", lineno(), "def nxapicall length of response_output", len(response_output))
        print("#### LINE #", lineno(), "def nxapicall type of response_output", type(response_output))

        #### if one command line, LINE # 63 length of response_output 3
        #### if one command line,  LINE # 63 type of response_output <class 'dict'>

        #### if two or more command LINE # 64 length of response_output 2
        #### if two or more command LINE # 64 type of response_output <class 'list'>

        if type(response_output) is dict:
            if response_output['ins_api']['code'] == 200:
                i = i + 0
                print("#### LINE #", lineno(), "def nxapicall i value when 200", i)
            else:
                i = i + 1
                print("#### LINE #", lineno(), "def nxapicall i value when not 200", i)


        if type(response_output) is list:
            for each in response_output:
                print("#### LINE #", lineno(), "def nxapicall - each command response", each['code'])
                if each['code'] == '200':
                    i = i + 0
                    print("#### LINE #", lineno(), "def nxapicall - i value when 200", i)
                else:
                    i = i + 1
                    print("#### LINE #", lineno(), "def nxapicall - i value when not 200", i)

        print("#### LINE #", lineno(), "def nxapicall - final i value", i)
        if i == 0:
            print("#### LINE #", lineno(), "def nxapicall - Success to config\n\n\n")
        else:
            print("#### LINE #", lineno(), "def nxapicall - Fail to Config\n\n\n")

if __name__ == "__main__":
    switchuser='admin'
    switchpassword='1234Qwer'
    ip_address = '192.168.0.233'
    #command = 'show clock ; show clock'
    command = 'show clock ; show clock'

    nxapicall(ip_address, switchuser, switchpassword, command)


