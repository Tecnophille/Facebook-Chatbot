from flask import Flask, request
import requests
from pymessenger import Bot

app = flask(__name__)

VERIFY_TOKEN = 'chatnow'
PAGE_ACCESS_TOKEN = 'v'
bot = Bot(PAGE_ACCESS_TOKEN)

def handling_message(text):
    adjusted_msg = text
    if adjusted_msg == 'Hi' or adjusted_msg == 'hi':
        response = 'Hello'

    elif adjusted_msg == "What's up" or adjusted_msg == "what's up":            
                response = "Im great"

            else:
                response = "Its a pleasure to chat with you today, thank you."

                return response

@app.route('/', methods=["POST", "GET"])

def web_hook();
if request.method == 'GET';
if request.args.get('hub.verify_token') == VERIFY_TOKEN:
    return request.args.get('hub.challenge')

else:
    return 'Unable to connect to FB'

elif request.method == 'POST':
    data = request.json
    process = data['entry'][0]['messaging']
    for msg in process:
        try:
        text = msg['message']['text']
        except:
            keyerror
        sender_id = msg['sender']['id']
        response = handling_message(text)
        bot.send_text_message(sender_id, response)

    return 'message_posted'


else:
    return Okay

if __name__ == '__main__':
    app.run()
