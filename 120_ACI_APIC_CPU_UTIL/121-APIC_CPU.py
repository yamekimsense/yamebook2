
from z100credential import *
from z110LoginToken import *
import datetime, time, json

token = getToken(host, id, password) #get the token using z110LoginToken

payload={}
headers = { 'Cookie': "APIC-cookie=" + token }


while True:
    temperature = []
    APIC = []
    url = "https://" + host + "/api/node/class/procEntity.json"
    #print ("url", url)
    response = requests.request("GET", url, headers=headers, data=payload, verify=False).json()
    #print(json.dumps(response, indent=4))

    print ("###")
    totalcount = response['totalCount']
    #print (totalcount)
    for i in range (0, int(totalcount) ):
        temperature.append ( response['imdata'][i]['procEntity']['attributes']['cpuPct'])
        APIC.append ( response['imdata'][i]['procEntity']['attributes']['dn'].split("/")[2] )
    print (datetime.datetime.now(), temperature, APIC, totalcount)
    time.sleep(1)

'''

wankim@WANKIM-M-P1E1 050-aci-api % python3 52-cpu-separated.py 
2023-01-02 10:31:17.623075 ['36', '29', '22'] ['node-1', 'node-2', 'node-3'] 3




    APIC1 = (response['imdata'][0]['procEntity']['attributes']['cpuPct'])
    APIC2 = (response['imdata'][1]['procEntity']['attributes']['cpuPct'])
    APIC3 = (response['imdata'][2]['procEntity']['attributes']['cpuPct'])
    print (APIC1, APIC2, APIC3)


    url = "https://" + host + "/api/node/class/procCPU5min.json"
    print ("url", url)
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    print ("##################", response.status_code)
    #print (response.text)


    url = "https://" + host + "/api/node/class/procCPUHist5min.json"
    print ("url", url)
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    print ("##################", response.status_code)
    #print (response.text)


{"totalCount":"3","imdata":[{"procEntity":{"attributes":{"adminSt":"enabled","childAction":"","cpuPct":"23","dn":"topology/pod-1/node-1/sys/proc","maxMemAlloc":"65367572","memFree":"27262420","modTs":"2022-11-10T23:36:42.822+09:00","monPolDn":"uni/fabric/monfab-default","name":"","operErr":"","operSt":"enabled","status":""}}},{"procEntity":{"attributes":{"adminSt":"enabled","childAction":"","cpuPct":"23","dn":"topology/pod-1/node-2/sys/proc","maxMemAlloc":"65367572","memFree":"18673920","modTs":"2022-11-10T23:36:50.884+09:00","monPolDn":"uni/fabric/monfab-default","name":"","operErr":"","operSt":"enabled","status":""}}},{"procEntity":{"attributes":{"adminSt":"enabled","childAction":"","cpuPct":"24","dn":"topology/pod-1/node-3/sys/proc","maxMemAlloc":"65367260","memFree":"26264624","modTs":"2022-11-10T23:36:58.933+09:00","monPolDn":"uni/fabric/monfab-default","name":"","operErr":"","operSt":"enabled","status":""}}}]}



{
    "totalCount": "3",
    "imdata": [
        {
            "procEntity": {
                "attributes": {
                    "adminSt": "enabled",
                    "childAction": "",
                    "cpuPct": "32",
                    "dn": "topology/pod-1/node-1/sys/proc",
                    "maxMemAlloc": "65367572",
                    "memFree": "23826972",
                    "modTs": "2022-12-08T07:52:13.263+09:00",
                    "monPolDn": "uni/fabric/monfab-default",
                    "name": "",
                    "operErr": "",
                    "operSt": "enabled",
                    "status": ""
                }
            }
        },
        {
            "procEntity": {
                "attributes": {
                    "adminSt": "enabled",
                    "childAction": "",
                    "cpuPct": "25",
                    "dn": "topology/pod-1/node-2/sys/proc",
                    "maxMemAlloc": "65367572",
                    "memFree": "15597648",
                    "modTs": "2022-12-08T07:52:08.857+09:00",
                    "monPolDn": "uni/fabric/monfab-default",
                    "name": "",
                    "operErr": "",
                    "operSt": "enabled",
                    "status": ""
                }
            }
        },
        {
            "procEntity": {
                "attributes": {
                    "adminSt": "enabled",
                    "childAction": "",
                    "cpuPct": "21",
                    "dn": "topology/pod-1/node-3/sys/proc",
                    "maxMemAlloc": "65367260",
                    "memFree": "24350796",
                    "modTs": "2022-12-08T07:52:03.293+09:00",
                    "monPolDn": "uni/fabric/monfab-default",
                    "name": "",
                    "operErr": "",
                    "operSt": "enabled",
                    "status": ""
                }
            }
        }
    ]
}
3
['32', '25', '21']

'''