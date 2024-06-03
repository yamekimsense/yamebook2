#group11x 10.70.137.115 dd06f978-9737-57d9-b24c-1dd4496c5003
#group11x 10.70.137.116 cb7f7046-c9aa-5611-9da1-265c24a5461c
#group-10x 10.70.137.109 2f6391a4-d104-5303-8538-f1fbb3e62278

component_id_list = ["2f6391a4-d104-5303-8538-f1fbb3e62278", "cb7f7046-c9aa-5611-9da1-265c24a5461c", "dd06f978-9737-57d9-b24c-1dd4496c5003"]

import requests

center_port = "443"
center_base_url = "api/3.0"
center_token = "ics-9591546cceca88d78bd8b6d87241bd819128c14d-0b08250afd8dfca4b40094019540e65c0b2fcc81"
center_ip = "10.70.138.125"
headers = { "x-token-id": center_token }

for component_id in component_id_list:
    r_get = requests.get(f"https://{center_ip}:{center_port}/{center_base_url}/components/{component_id}",headers=headers,verify=False)
    raw_json_data = r_get.json()
    print (raw_json_data['userProperties'])

    for component in raw_json_data['userProperties']:
        print (component['id'])
        r_get = requests.delete(f"https://{center_ip}:{center_port}/{center_base_url}/components/{component_id}/usersProperties/{component['id']}",
                             headers=headers, verify=False)
        raw_json_data = r_get.json()
        print (raw_json_data)










'''
{'id': '2f6391a4-d104-5303-8538-f1fbb3e62278', 
'label': '10.70.137.109', 
'customLabel': '', 
'originalLabel': '10.70.137.109', 
'ip': '10.70.137.109', 'mac': '00:50:56:92:94:4d', 'icon': 'library/vmware.svg', 'firstActivity': 1714124687043, 'lastActivity': 1714124964114, 
'group': {'id': 'abcf9b55-80ef-4a53-affe-c4c4007605a6', 'label': 'HVAC', 'description': '', 'comments': '', 'color': '#06a2c9', 'locked': False, 'groupIds': None, 'centerID': ''}, 
'vulnerabilitiesCount': 0, 'flowsCount': 0, 'eventsCount': 1, 'variablesCount': 0, 'credentialsCount': 0, 'externalCommunicationsCount': 0, 'tags': [], 
'flowsTags': 
        [{'id': 'ARP', 
        'label': 'ARP', 'important': False, 
        'category': {'id': 'b6d3d12d-9e34-5afc-89e2-3fc32fdaf1a2', 'label': 'Protocol'}}, {'id': 'BROADCAST', 'label': 'Broadcast', 'important': False, 'category': {'id': '5cb3eeb7-b0eb-5553-8575-8f11d25de770', 'label': 'Network analysis'}}], 
'normalizedProperties': 
        [{'key': 'ip', 'value': '10.70.137.109'}, {'key': 'mac', 'value': '00:50:56:92:94:4d'}, {'key': 'name', 'value': '10.70.137.109'}, {'key': 'public-ip', 'value': 'no'}, {'key': 'vendor-name', 'value': 'VMware, Inc.'}], 
'otherProperties': [{'key': 'name-ip', 'value': '10.70.137.109'}, {'key': 'vendor', 'value': 'VMware, Inc.'}], 
'userProperties': 
        [{'id': 'bd314928-3b33-4863-9ef0-9c2bc2823b96', 'key': 'Type', 'value': 'PLC'}, 
        {'id': 'da56b19d-080d-4581-9229-1392c35788f5', 'key': 'Host_Name', 'value': 'H-PLC-15-Pri'}, 
        {'id': '631a5388-b302-4368-b9d4-d40ed595a1b3', 'key': 'Location', 'value': 'DC-1-Rack-3'}, 
        {'id': 'f5ad7f2a-c1e6-4a10-a618-4c3e384bb530', 'key': 'Owner', 'value': 'Richard'}, 
        {'id': 'dfb0df1c-e567-43e0-b649-53af14c2b1df', 'key': 'Phone', 'value': '203-534-2598'}], 
'aggregation': {'type': 'none', 'components': None}, 
'sensorNames': ['CENTER-ETH1']}

'''