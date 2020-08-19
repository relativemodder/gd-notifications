from itertools import cycle
import base64
import requests
import json

def loginGJAccount(server, userName, password):
	headers = {
		"Content-Type": "application/x-www-form-urlencoded"
    }
	response = requests.post(server+"/accounts/loginGJAccount.php", data={'userName': userName, 'password': password, 'udid':'00000000-4ca6-6280-ffff-ffffa6dc3355'}, headers=headers)
	return response.text.split(",")
def xor(data, key):
    return ''.join(chr(a ^ ord(b)) for (a, b) in zip(data, cycle(key)))
def gjp(password):
	gjp = password.encode()
	gjp = xor(gjp,'37526').encode()
	gjp = base64.b64encode(gjp).decode()
	return gjp
