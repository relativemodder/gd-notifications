import requests
import json
from config import ACCESS_TOKEN
import config
import gjlogintools
import time
import gmd
import base64


#go to config py

url = 'https://api.pushbullet.com/v2/pushes'
		
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
logindata = gjlogintools.loginGJAccount(server=config.server, userName=config.userName, password=config.password)
while 1:
	#checking for new messages, just logging into the account
	latest = gmd.check_new_messages(config.server, logindata[0], gjlogintools.gjp(config.password))
	print(latest)
	if(latest.split(":")[11] == "0"):
		print("new message")
		print(gmd.make_checked(config.server, logindata[0], latest))
		data = {
			"body": "Title: "+base64.b64decode(latest.split(":")[9]).decode(),
			"title": "Message from "+latest.split(":")[1],
			"type": "note",
		}
		ler = requests.post(url, data=json.dumps(data), headers=headers)
	#response = requests.post(url, data=json.dumps(data), headers=headers)
	time.sleep(0.1)
print(response.text)