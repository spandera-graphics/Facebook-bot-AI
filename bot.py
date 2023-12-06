import requests
import json
import os

from flask import Flask, request

bot = Flask(__name__)

PAGE_ACCESS_TOKEN='EAAODKttbnSoBOwhiUPgR6UJS6Wzo1IzPBcP4hZA0xjfgaIfFqGTQFKdbjZBh2xtvoFELjFQA2GZCWWnobR3f1cAZAIN5QLrcD4eK8CRt7kprl4bKRsCVPDxKFqoqSw0xFdYdCN0fZCNpiCiboT2pHanKChJwsng9NxBZCGNpEvoNkZAAeApZBhBEBA4507R7yhUxU6R3nUNh6e3ybsHjGMZAZAK7ZCh'
VERIFY_TOKEN = 'spandera77'

@bot.route('/', methods=['GET'])
def hub_challenge_verification():
	if request.args.get("hub.mode")=="subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.VERIFY_TOKEN") == VERIFY_TOKEN:
			return "Verification Invalid", 403
		return request.args.get('hub.challenge','')


@bot.route('/', methods=['POST'])
def webhook():
	data = json.loads(request.data)
	messaging_events = data["entry"][0]["messaging"]
	for event in messaging_events:
		sender = event['sender']['id']
		receiver = event['recipient']['id']
		message = event['message']['text']
		send_message(sender, "Hi")


def send_message(person_who_will_receive, message):

	# reply_object = Reply(message)
	# message_data = reply_object.get_reply()

	params = {"access_token": PAGE_ACCESS_TOKEN}
	headers = {"Content-Type": "application/json"}
	data = json.dumps({
		"recipient":{"id": person_who_will_receive},
		"message": {"text": message}
		})
	r=requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    # if r.status_code!=requests.codes.ok:
    # 	print(r.text)
