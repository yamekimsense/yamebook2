from flask import Flask, render_template, redirect, request, url_for
import requests, json, datetime, time, sys

app = Flask(__name__)

class DataStore():
    token1 = ""
data = DataStore()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST', 'GET'])
def calculate(num=None):

    list = []
    email = request.args.get('char1')
    token = request.args.get('char2')
    data.token1 = token
    data.email1 = email

    print ("email", email)
    print ("token", token)

    headers = {
        'Authorization': 'Bearer ' + token
    }

    response = requests.get('https://webexapis.com/v1/rooms?max=1000', headers=headers)

    json_load = json.loads(response.text)
    items = json_load['items']

    number = 1
    for each in items:
        if each['type'] == "group":
            #data = "," + each["id"] + "," + each['lastActivity'] + ",\"" + each['title'] + "\"\n"
            #print(data)
            each2 = []
            each2.append(each['lastActivity'])
            each2.append(each['title'])
            each2.append(each["id"])
            print("each2", each2)
            list.append(each2)
            number = number + 1

    list.sort(reverse=True)
    print ("####list", list)

    #return '<h1>list </h1>'
    return render_template('150.html', list = list)

@app.route('/get', methods=['POST', 'GET'])
def get(num=None):
    if request.method == "POST":
        room_list = request.form.getlist ('mycheckbox' )
        print (room_list)
        token1 = data.token1
        email1 = data.email1
        print ("token @ get", token1)
        print("email @ get", email1)

        headers1 = {
            'Authorization': 'Bearer ' + token1
        }

        for room_id in room_list:
            response2 = requests.get('https://webexapis.com/v1/memberships?roomId=' + room_id, headers=headers1)
            json_load2 = json.loads(response2.text)
            items2 = json_load2['items']

            for each2 in items2:
                if each2['personEmail'] == email1:
                    response3 = requests.delete("https://webexapis.com/v1/memberships/" + each2['id'], headers=headers1)
                    print(room_id, response2)

        return 'Maybe Done. Check again'
    return "hello"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="80", debug=True, threaded=True)
