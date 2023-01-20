#create the bot with BotFather
#get the token
#import telegram as tel

#python module for telegram
#pip install python-telegram-bot
# bot = tel.Bot(token="5756874451:AAEkZHCMDis7k0P1_hgXpjVqE8aY-zX-AZw")
# bot.sendMessage(chat_id=chat_id_each, text=message)

from datetime import datetime
import requests, json, logging

token = '5756874451:AAEkZHCMDis7k0P1_hgXpjVqE8aY-zX-AZw'

logging.basicConfig(filename="defTELEgram.log", level=logging.INFO)

def TELEgram(message):
    response_chat_id = requests.get(f"https://api.telegram.org/bot{token}/getUpdates")
    logging.info (f"1000 response_chat_id {response_chat_id}" )
    logging.info (f"1010 response_chat_id.status_code {response_chat_id.status_code}")
    logging.info (f"2000 response_chat_id.text {response_chat_id.text}", )
    logging.info ( json.dumps( json.loads( response_chat_id.text  ) , indent=4) )

    if response_chat_id.status_code == 200:
        response_chat_id = json.loads(response_chat_id.text)['result']
        logging.info ("3000 response_chat_id {response_chat_id}" )
        logging.info ( json.dumps(  response_chat_id , indent=4) )
        logging.info (type (response_chat_id))

        chat_id = list()

        for each in response_chat_id:
            logging.info ( f"3100 ID {each['message']['chat']['id']}")
            chat_id.append(each['message']['from']['id'])
            logging.info (f"3300 chat_ID print {chat_id}")

        chat_id.append(5805584681) #my chat id / add manually to prevent expire
        logging.info (f"3500 before set { chat_id}")
        chat_id = list(set(chat_id))
        logging.info (f"3600 after set { chat_id}")

        for chat_id_each in chat_id:
            json_data = {
                'chat_id': chat_id_each,
                'text': message
            }

            response = requests.post(f'https://api.telegram.org/bot{token}/sendMessage', json=json_data)

            logging.info (response.text)

            if response.status_code == 200:
                print (f"Message \"{message}\" is sent to chat id {chat_id_each}.")


if __name__ == "__main__":
    now = datetime.now()
    clock = now.strftime('%Y-%m-%d %H:%M:%S')
    logging.info (clock)  # 2022-12-27 09:38:13
    TELEgram(clock)



'''

https://api.telegram.org/bot5756874451:AAEkZHCMDis7k0P1_hgXpjVqE8aY-zX-AZw/getUpdates

wankim@WANKIM-M-P1E1 040-NXAPI_QT_TELEgram % python3 defTELEgram.py
2022-12-31 19:11:32
1000 response_chat_id <Response [200]>
2000 response_chat_id.text {"ok":true,"result":[{"update_id":323717435,
"message":{"message_id":13,"from":{"id":5805584681,"is_bot":false,"first_name":"Wansoo","last_name":"Kim","language_code":"en"},"chat":{"id":5805584681,"first_name":"Wansoo","last_name":"Kim","type":"private"},"date":1672481490,"text":"a"}}]}
{
    "ok": true,
    "result": [
        {
            "update_id": 323717435,
            "message": {
                "message_id": 13,
                "from": {
                    "id": 5805584681,
                    "is_bot": false,
                    "first_name": "Wansoo",
                    "last_name": "Kim",
                    "language_code": "en"
                },
                "chat": {
                    "id": 5805584681,
                    "first_name": "Wansoo",
                    "last_name": "Kim",
                    "type": "private"
                },
                "date": 1672481490,
                "text": "a"
            }
        }
    ]
}
3000 response_chat_id [{'update_id': 323717435, 'message': {'message_id': 13, 'from': {'id': 5805584681, 'is_bot': False, 'first_name': 'Wansoo', 'last_name': 'Kim', 'language_code': 'en'}, 'chat': {'id': 5805584681, 'first_name': 'Wansoo', 'last_name': 'Kim', 'type': 'private'}, 'date': 1672481490, 'text': 'a'}}]
[
    {
        "update_id": 323717435,
        "message": {
            "message_id": 13,
            "from": {
                "id": 5805584681,
                "is_bot": false,
                "first_name": "Wansoo",
                "last_name": "Kim",
                "language_code": "en"
            },
            "chat": {
                "id": 5805584681,
                "first_name": "Wansoo",
                "last_name": "Kim",
                "type": "private"
            },
            "date": 1672481490,
            "text": "a"
        }
    }
]
<class 'list'>
5805584681
wankim@WANKIM-M-P1E1 040-NXAPI_QT_TELEgram % 

'''