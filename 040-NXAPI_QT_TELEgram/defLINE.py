import requests, json, logging
from datetime import datetime

line_token = 'Q0x4ydz84cpWGSgo5AkZI2q1uwoNgGQJZM+avwqHDhy2QXpbP02eZ40htdv2ugQ3QRGhfrkMwHyCAqxZhDl2du9/NjWnjsjD4oLJ8Gl+rL62sA9ZV7kpfa+5WiSRpfckvA1VbzpNiifUZpLcDyA1VQdB04t89/1O/w1cDnyilFU='

logging.basicConfig(filename="defLINE.log", level=logging.INFO)


def LINE_NAVER(message):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + line_token,
    }

    json_data = {
        'messages': [
            {
                'type': 'text',
                'text': message,
            }
        ],
    }

    response = requests.post('https://api.line.me/v2/bot/message/broadcast', headers=headers, json=json_data)
    logging.info ( f"line 1000 response {response}")
    logging.info ( f"line 2000 response {response.text}")
    if response.status_code == 200:
        print (f"@naver line message {message} was sent to all users.")

if __name__ == "__main__":
    now = datetime.now()
    clock = now.strftime('%Y-%m-%d %H:%M:%S')
    print("message is ", clock)  # 2022-12-27 09:38:13
    LINE_NAVER(clock)

'''
wankim@WANKIM-M-P1E1 040-NXAPI_QT_TELEgram % python3 defLINE.py
message is  2023-01-02 09:48:35
@naver line message 2023-01-02 09:48:35 was sent to all users.


curl -v -X POST https://api.line.me/v2/bot/message/broadcast \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer Q0x4ydz84cpWGSgo5AkZI2q1uwoNgGQJZM+avwqHDhy2QXpbP02eZ40htdv2ugQ3QRGhfrkMwHyCAqxZhDl2du9/NjWnjsjD4oLJ8Gl+rL62sA9ZV7kpfa+5WiSRpfckvA1VbzpNiifUZpLcDyA1VQdB04t89/1O/w1cDnyilFU=' \
-d '{
    "messages":[
        {
            "type":"text",
            "text":"Hello, world1"
        },
        {
            "type":"text",
            "text":"Hello, world2"
        }
    ]
}'

'''