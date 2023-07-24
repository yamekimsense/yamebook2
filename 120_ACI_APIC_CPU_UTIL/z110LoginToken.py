import requests, json
requests.packages.urllib3.disable_warnings()

def getToken (host, id, password):

  url = "https://" + host + "/api/aaaLogin.json"
  payload = json.dumps({"aaaUser": {"attributes": {"name": id ,"pwd": password }}})
  headers = {'Content-Type': 'application/json'}
  response = requests.request("POST", url, headers=headers, data=payload, verify=False)

  token = json.loads(response.text)['imdata'][0]['aaaLogin']['attributes']['token']
  #print (token)

  return (token)