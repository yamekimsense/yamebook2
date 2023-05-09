import requests, json
requests.packages.urllib3.disable_warnings()

def getToken (host, id, password):

  url = "https://" + host + "/api/aaaLogin.json"

  payload = {
    "aaaUser":
      {
        "attributes":
          {
            "name": id,
            "pwd": password
          }
      }
  }

  headers = {
    'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=json.dumps(payload), verify=False)

  print ( json.dumps( json.loads( response.text  ) , indent=4) )

  token = json.loads(response.text)['imdata'][0]['aaaLogin']['attributes']['token']

  return (token)
