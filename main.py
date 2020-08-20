import requests
import json
from config import ACCESS_TOKEN
import config
import gjlogintools
import time
import gmd
import base64
import urllib3
import urllib
import gd
import gd
extID = 0

url = 'https://api.pushbullet.com/v2/pushes'
		
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
if(config.switcher==0):
	client = gd.Client()
	client.sync_login(config.userName, config.password)
	print(client.account_id)
	extID=client.account_id
else:
	logindata = ""
	isConnectedLogin = 0
	while isConnectedLogin == 0:
		try:
			logindata = gjlogintools.loginGJAccount(server=config.server, userName=config.userName, password=config.password)
			extID = logindata[0]
		except Exception:
			isConnectedLogin = 0
			print('networkIsUnstable')
		else:
			isConnectedLogin = 1
			if(logindata!="-1"):
				print('Logged in')
			else:
				print("error")
		time.sleep(2)
print(extID)
if(config.switcher==1):
	while 1:
		#checking for new messages, just logging into the account
		isNetworkStable = 0
		while isNetworkStable == 0:
			try:
				latest = gmd.check_new_messages(config.server, extID, gjlogintools.gjp(config.password))
				isNetworkStable = 0
			except:
				print("networkIsUnstable")
				time.sleep(2)
			else:
				isNetworkStable = 1
				print("checked messages")
		isNetworkStable = 0
		print(latest)
		if(latest.split(":")[11] == "0"):
			print("new message")
			while isNetworkStable == 0:
				try:
					print(gmd.make_checked(config.server, extID, latest))
					isNetworkStable = 0
				except:
					print("networkIsUnstable")
					time.sleep(1)
				else:
					isNetworkStable = 1
					print("made messages checked")
			isNetworkStable = 0
			data = {
				"body": "Title: "+base64.b64decode(latest.split(":")[9]).decode(),
				"title": "Message from "+latest.split(":")[1],
				"type": "note",
			}
			if(latest.split(":")[1] not in config.mutelist):
				ler = requests.post(url, data=json.dumps(data), headers=headers)
		#response = requests.post(url, data=json.dumps(data), headers=headers)
		time.sleep(0.1)
else:
	print("robtop servers")
	client = gd.Client()
	
	client.sync_login(config.userName, config.password)
	
	
	
	@client.listen_for("message")
	async def on_message(message: gd.Message):
		notifydata = {
			"body": "Title: "+ message.subject,
			"title": "Message from "+message.author.name,
			"type": "note"
		}
		if(message.author.name not in config.mutelist):
			ler = requests.post(url, data=json.dumps(notifydata), headers=headers)
			print('message! check push!')
	friend_client = gd.Client()
	friend_client.sync_login(config.userName, config.password)
	@friend_client.listen_for("friend_request")
	async def on_friend_request(friend_request: gd.FriendRequest):
		notifydata = {
			"body": "Request from "+ friend_request.author.name,
			"title": "GD Friend Request!",
			"type": "note"
		}
		if(friend_request.author.name not in config.mutelist):
			ler = requests.post(url, data=json.dumps(notifydata), headers=headers)
			print('friend! check push!')
	gd.events.run()
print(response.text)