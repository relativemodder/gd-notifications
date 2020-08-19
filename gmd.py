import requests
import base64
import gjlogintools
import config

def check_new_messages(server, accountID, gjp):
	response = requests.post(server+"/getGJMessages20.php", data={'accountID':accountID, 'gjp':gjp, 'page':0})
	messages_array = response.text.split("|")
	latest_message=messages_array[0]
	return latest_message
def make_checked(server, accountID, message):
	gjp = gjlogintools.gjp(config.password)
	response = requests.post(server+"/downloadGJMessage20.php", data={'accountID':accountID, 'gjp':gjp, 'messageID':message.split(":")[7], 'isSender':'0', 'gameVersion':'21', 'binaryVersion':'34', 'gdw':'0', 'secret':'Wmfd2893gb7'})                        
	return response.text