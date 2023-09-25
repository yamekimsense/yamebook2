
from z100credential import *
from z110LoginToken import *
import datetime, time, json

token = getToken(host, id, password) #get the token using z110LoginToken

payload={}
headers = { 'Cookie': "APIC-cookie=" + token }

HOST_IP = input("Please, input HOST_IP to track? [default 10.193.101.2] ")
if len(HOST_IP) == 0:
    HOST_IP = "10.193.101.2"
HOST_IP = "\"" + HOST_IP + "\""


#Get the location information
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
            print (date, ip, mac, action, path, encap)









'''
{
    "totalCount": "2",
    "imdata": [
        {
            "troubleshootEpTransition": {
                "attributes": {
                    "action": "attached",
                    "ap": "Save_The_Planet",
                    "childAction": "",
                    "ctx": "",
                    "date": "2023-09-23T06:58:37.194+00:00",
                    "dn": "epts-[uni/tn-Heroes/ap-Save_The_Planet/epg-db/cep-43:CD:BB:C0:00:00]-1",
                    "encap": "vlan-202",
                    "epg": "db",
                    "esg": "",
                    "id": "1",
                    "ip": "10.193.101.2",
                    "lcOwn": "local",
                    "mac": "43:CD:BB:C0:00:00",
                    "modTs": "never",
                    "path": "topology/pod-1/paths-101/pathep-[Heroes_FI-2B]",
                    "rn": "epts-[uni/tn-Heroes/ap-Save_The_Planet/epg-db/cep-43:CD:BB:C0:00:00]-1",
                    "status": "created,modified",
                    "subj": "uni/tn-Heroes/ap-Save_The_Planet/epg-db/cep-43:CD:BB:C0:00:00",
                    "tenant": "Heroes"
                }
            }
        },
        {
            "troubleshootEpTransition": {
                "attributes": {
                    "action": "attached",
                    "ap": "Save_The_Planet",
                    "childAction": "",
                    "ctx": "",
                    "date": "2023-09-23T06:58:37.194+00:00",
                    "dn": "epts-[uni/tn-Heroes/ap-Save_The_Planet/epg-db/cep-43:CD:BB:C0:00:00]-2",
                    "encap": "vlan-202",
                    "epg": "db",
                    "esg": "",
                    "id": "2",
                    "ip": "2222::65:2",
                    "lcOwn": "local",
                    "mac": "43:CD:BB:C0:00:00",
                    "modTs": "never",
                    "path": "topology/pod-1/paths-101/pathep-[Heroes_FI-2B]",
                    "rn": "epts-[uni/tn-Heroes/ap-Save_The_Planet/epg-db/cep-43:CD:BB:C0:00:00]-2",
                    "status": "created,modified",
                    "subj": "uni/tn-Heroes/ap-Save_The_Planet/epg-db/cep-43:CD:BB:C0:00:00",
                    "tenant": "Heroes"
                }
            }
        }
    ]
}



'''




'''
{
    "totalCount": "3",
    "imdata": [
        {
            "fvCEp": {
                "attributes": {
                    "annotation": "",
                    "baseEpgDn": "",
                    "bdDn": "uni/tn-Heroes/BD-Hero_Land",
                    "childAction": "",
                    "contName": "",
                    "dn": "uni/tn-Heroes/ap-Save_The_Planet/epg-app/cep-43:CD:BB:C0:00:00",
                    "encap": "vlan-201",
                    "esgUsegDn": "",
                    "extMngdBy": "",
                    "fabricPathDn": "topology/pod-1/paths-101/pathep-[Heroes_FI-2B]",
                    "hostingServer": "",
                    "id": "0",
                    "idepdn": "",
                    "lcC": "learned",
                    "lcOwn": "local",
                    "mac": "43:CD:BB:C0:00:00",
                    "mcastAddr": "not-applicable",
                    "modTs": "2023-09-23T06:58:37.185+00:00",
                    "monPolDn": "uni/tn-common/monepg-default",
                    "name": "43:CD:BB:C0:00:00",
                    "nameAlias": "",
                    "reportingControllerName": "",
                    "status": "",
                    "uid": "0",
                    "userdom": "all",
                    "uuid": "",
                    "vmmSrc": "",
                    "vrfDn": "uni/tn-Heroes/ctx-Heroes_Only"
                },
                "children": [
                    {
                        "fvIp": {
                            "attributes": {
                                "addr": "10.193.101.2",
                                "annotation": "",
                                "baseEpgDn": "",
                                "bdDn": "uni/tn-Heroes/BD-Hero_Land",
                                "childAction": "",
                                "createTs": "2023-09-23T06:58:37.187+00:00",
                                "debugMACMessage": "Context: 2162688. First 3 fvCEps: uni/tn-Heroes/ap-Save_The_Planet/epg-web/cep-43:CD:BB:C0:00:00; uni/tn-Heroes/ap-Save_The_Planet/epg-db/cep-43:CD:BB:C0:00:00; uni/tn-Heroes/ap-Save_The_Planet/epg-app/cep-43:CD:BB:C0:00:00;",
                                "esgUsegDn": "",
                                "extMngdBy": "",
                                "fabricPathDn": "topology/pod-1/paths-101/pathep-[Heroes_FI-2B]",
                                "flags": "",
                                "lcOwn": "local",
                                "modTs": "2023-09-23T06:58:37.189+00:00",
                                "monPolDn": "uni/tn-common/monepg-default",
                                "rn": "ip-[10.193.101.2]",
                                "status": "",
                                "uid": "0",
                                "userdom": "all",
                                "vrfDn": "uni/tn-Heroes/ctx-Heroes_Only"
                            },
                            "children": [
                                {
                                    "fvRsToEpIpTag": {
                                        "attributes": {
                                            "childAction": "",
                                            "forceResolve": "yes",
                                            "lcOwn": "local",
                                            "modTs": "2023-09-23T06:58:37.185+00:00",
                                            "rType": "mo",
                                            "rn": "rstoEpIpTag",
                                            "state": "missing-target",
                                            "stateQual": "none",
                                            "status": "",
                                            "tCl": "fvEpIpTag",
                                            "tDn": "uni/tn-Heroes/eptags/epiptag-[10.193.101.2]-Heroes_Only",
                                            "tType": "mo"
                                        }
                                    }
                                },
                                {
                                    "fvReportingNode": {
                                        "attributes": {
                                            "childAction": "",
                                            "createTs": "1970-01-01T00:00:00.000+00:00",
                                            "id": "101",
                                            "lcC": "",
                                            "lcOwn": "local",
                                            "modTs": "2023-09-23T06:58:37.185+00:00",
                                            "rn": "node-101",
                                            "status": ""
                                        }
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        },
        {
            "fvCEp": {
                "attributes": {
                    "annotation": "",
                    "baseEpgDn": "",
                    "bdDn": "uni/tn-Heroes/BD-Hero_Land",
                    "childAction": "",
                    "contName": "",
                    "dn": "uni/tn-Heroes/ap-Save_The_Planet/epg-web/cep-43:CD:BB:C0:00:00",
                    "encap": "vlan-200",
                    "esgUsegDn": "",
                    "extMngdBy": "",
                    "fabricPathDn": "topology/pod-1/paths-101/pathep-[Heroes_FI-2B]",
                    "hostingServer": "",
                    "id": "0",
                    "idepdn": "",
                    "lcC": "learned",
                    "lcOwn": "local",
                    "mac": "43:CD:BB:C0:00:00",
                    "mcastAddr": "not-applicable",
                    "modTs": "2023-09-23T06:58:37.189+00:00",
                    "monPolDn": "uni/tn-common/monepg-default",
                    "name": "43:CD:BB:C0:00:00",
                    "nameAlias": "",
                    "reportingControllerName": "",
                    "status": "",
                    "uid": "0",
                    "userdom": "all",
                    "uuid": "",
                    "vmmSrc": "",
                    "vrfDn": "uni/tn-Heroes/ctx-Heroes_Only"
                },
                "children": [
                    {
                        "fvIp": {
                            "attributes": {
                                "addr": "10.193.101.2",
                                "annotation": "",
                                "baseEpgDn": "",
                                "bdDn": "uni/tn-Heroes/BD-Hero_Land",
                                "childAction": "",
                                "createTs": "2023-09-23T06:58:37.192+00:00",
                                "debugMACMessage": "",
                                "esgUsegDn": "",
                                "extMngdBy": "",
                                "fabricPathDn": "topology/pod-1/paths-101/pathep-[Heroes_FI-2B]",
                                "flags": "",
                                "lcOwn": "local",
                                "modTs": "2023-09-23T06:58:37.189+00:00",
                                "monPolDn": "uni/tn-common/monepg-default",
                                "rn": "ip-[10.193.101.2]",
                                "status": "",
                                "uid": "0",
                                "userdom": "all",
                                "vrfDn": "uni/tn-Heroes/ctx-Heroes_Only"
                            },
                            "children": [
                                {
                                    "fvRsToEpIpTag": {
                                        "attributes": {
                                            "childAction": "",
                                            "forceResolve": "yes",
                                            "lcOwn": "local",
                                            "modTs": "2023-09-23T06:58:37.189+00:00",
                                            "rType": "mo",
                                            "rn": "rstoEpIpTag",
                                            "state": "missing-target",
                                            "stateQual": "none",
                                            "status": "",
                                            "tCl": "fvEpIpTag",
                                            "tDn": "uni/tn-Heroes/eptags/epiptag-[10.193.101.2]-Heroes_Only",
                                            "tType": "mo"
                                        }
                                    }
                                },
                                {
                                    "fvReportingNode": {
                                        "attributes": {
                                            "childAction": "",
                                            "createTs": "1970-01-01T00:00:00.000+00:00",
                                            "id": "101",
                                            "lcC": "",
                                            "lcOwn": "local",
                                            "modTs": "2023-09-23T06:58:37.189+00:00",
                                            "rn": "node-101",
                                            "status": ""
                                        }
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        },
        {
            "fvCEp": {
                "attributes": {
                    "annotation": "",
                    "baseEpgDn": "",
                    "bdDn": "uni/tn-Heroes/BD-Hero_Land",
                    "childAction": "",
                    "contName": "",
                    "dn": "uni/tn-Heroes/ap-Save_The_Planet/epg-db/cep-43:CD:BB:C0:00:00",
                    "encap": "vlan-202",
                    "esgUsegDn": "",
                    "extMngdBy": "",
                    "fabricPathDn": "topology/pod-1/paths-101/pathep-[Heroes_FI-2B]",
                    "hostingServer": "",
                    "id": "0",
                    "idepdn": "",
                    "lcC": "learned",
                    "lcOwn": "local",
                    "mac": "43:CD:BB:C0:00:00",
                    "mcastAddr": "not-applicable",
                    "modTs": "2023-09-23T06:58:37.189+00:00",
                    "monPolDn": "uni/tn-common/monepg-default",
                    "name": "43:CD:BB:C0:00:00",
                    "nameAlias": "",
                    "reportingControllerName": "",
                    "status": "",
                    "uid": "0",
                    "userdom": "all",
                    "uuid": "",
                    "vmmSrc": "",
                    "vrfDn": "uni/tn-Heroes/ctx-Heroes_Only"
                },
                "children": [
                    {
                        "fvIp": {
                            "attributes": {
                                "addr": "10.193.101.2",
                                "annotation": "",
                                "baseEpgDn": "",
                                "bdDn": "uni/tn-Heroes/BD-Hero_Land",
                                "childAction": "",
                                "createTs": "2023-09-23T06:58:37.192+00:00",
                                "debugMACMessage": "Context: 2162688. First 3 fvCEps: uni/tn-Heroes/ap-Save_The_Planet/epg-web/cep-43:CD:BB:C0:00:00; uni/tn-Heroes/ap-Save_The_Planet/epg-db/cep-43:CD:BB:C0:00:00; uni/tn-Heroes/ap-Save_The_Planet/epg-app/cep-43:CD:BB:C0:00:00;",
                                "esgUsegDn": "",
                                "extMngdBy": "",
                                "fabricPathDn": "topology/pod-1/paths-101/pathep-[Heroes_FI-2B]",
                                "flags": "",
                                "lcOwn": "local",
                                "modTs": "2023-09-23T06:58:37.189+00:00",
                                "monPolDn": "uni/tn-common/monepg-default",
                                "rn": "ip-[10.193.101.2]",
                                "status": "",
                                "uid": "0",
                                "userdom": "all",
                                "vrfDn": "uni/tn-Heroes/ctx-Heroes_Only"
                            },
                            "children": [
                                {
                                    "fvRsToEpIpTag": {
                                        "attributes": {
                                            "childAction": "",
                                            "forceResolve": "yes",
                                            "lcOwn": "local",
                                            "modTs": "2023-09-23T06:58:37.189+00:00",
                                            "rType": "mo",
                                            "rn": "rstoEpIpTag",
                                            "state": "missing-target",
                                            "stateQual": "none",
                                            "status": "",
                                            "tCl": "fvEpIpTag",
                                            "tDn": "uni/tn-Heroes/eptags/epiptag-[10.193.101.2]-Heroes_Only",
                                            "tType": "mo"
                                        }
                                    }
                                },
                                {
                                    "fvReportingNode": {
                                        "attributes": {
                                            "childAction": "",
                                            "createTs": "1970-01-01T00:00:00.000+00:00",
                                            "id": "101",
                                            "lcC": "",
                                            "lcOwn": "local",
                                            "modTs": "2023-09-23T06:58:37.189+00:00",
                                            "rn": "node-101",
                                            "status": ""
                                        }
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
    ]
}

'''