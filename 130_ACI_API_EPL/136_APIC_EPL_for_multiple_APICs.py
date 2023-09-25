
from z110LoginToken import *
import datetime, time, json

HOST_IP = input("Please, input HOST_IP to track? [default 10.193.101.2] ")
if len(HOST_IP) == 0:
    HOST_IP = "10.193.101.2"
HOST_IP = "\"" + HOST_IP + "\""

FINAL_RESULT = []

f = open("z120_APIC_info", 'r')
lines = f.readlines()
for line in lines:
    line = line.replace("\n","")
    #print(line)
    host = line.split(",")[0]
    id = line.split(",")[1]
    password = line.split(",")[2]

    #print ("13", host, id, password)

    token = getToken(host, id, password)  # get the token using z110LoginToken

    payload={}
    headers = { 'Cookie': "APIC-cookie=" + token }

    url = "https://" + host + "/api/node/class/fvCEp.json?rsp-subtree=full&rsp-subtree-include=required&rsp-subtree-filter=eq(fvIp.addr," + HOST_IP + ")"
    #print (url)
    response = requests.request("GET", url, headers=headers, data=payload, verify=False).json()
    #print(json.dumps(response, indent=4))


    totalcount = response['totalCount']
    #print ("totalcount is ", totalcount)

    URL_LIST = []

    for i in range (0, int(totalcount) ):
        DN = response['imdata'][i]['fvCEp']['attributes']['dn']
        #DN = DN.split("/cep-")[0]
        URL_LIST.append (DN)
        #print (DN)

    #print (URL_LIST)

    for i in range (0, int(totalcount) ):
        DN = URL_LIST[i]
        url = "https://" + host + "/mqapi2/troubleshoot.eptracker.json?ep=" + DN
        #print (url)
        response = requests.request("GET", url, headers=headers, data=payload, verify=False).json()
        #print ("========================================")
        #print(json.dumps(response, indent=4))

        totalcount2 = response['totalCount']

        for j in range (0, int(totalcount2)):
            date = response['imdata'][j]['troubleshootEpTransition']['attributes']['date']
            ip =  response['imdata'][j]['troubleshootEpTransition']['attributes']['ip']
            mac = response['imdata'][j]['troubleshootEpTransition']['attributes']['mac']
            action = response['imdata'][j]['troubleshootEpTransition']['attributes']['action']
            path = response['imdata'][j]['troubleshootEpTransition']['attributes']['path']
            encap = response['imdata'][j]['troubleshootEpTransition']['attributes']['encap']

            if ":" not in ip:
                IPv4_RESULT = date + " " + host + " " + ip + " " + mac + " " + action + " " + path + " " + encap
                print ("Doing " + IPv4_RESULT)
                FINAL_RESULT.append(IPv4_RESULT)
f.close()

#print (FINAL_RESULT)

my_list = FINAL_RESULT
result = []

for i in my_list:
    if i not in result:
        result.append(i)

print("\n\n\n############# Final Result Duplication Removed ################")
print ("Data       TIme               APIC_IP     EP IPv4      MAC               Event    DN                                             Encap")
#2023-09-23T06:58:37.187+00:00 10.10.20.14 10.193.101.2 43:CD:BB:C0:00:00 attached topology/pod-1/paths-101/pathep-[Heroes_FI-2B] vlan-201

result.sort()

for i in range ( 0, len(result) ):
    print (   result[i]         )