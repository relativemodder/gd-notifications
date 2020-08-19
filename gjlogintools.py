from itertools import cycle
import base64
import requests
import json
import urllib3
import urllib
from urllib import request as urlrequest
import config
def GetAccID(server, name):
    accUrl = server+"/getGJUsers20.php"
    accParams = "gameVersion=21&binaryVersion=34&gdw=0&str="+name+"&total=0&page=0&secret=Wmfd2893gb7"
    accParams = accParams.encode()
    req = urlrequest.Request(accUrl, accParams)
    data = urlrequest.urlopen(req).read().decode()
    print(data)
    data = data.split(':')[19]
    return data
def loginGJAccount(server, userName, password):
	headers = {
		"Content-Type": "application/x-www-form-urlencoded"
    }
	response = requests.post(server+"/accounts/loginGJAccount.php", data={'udid':'S15212421141421881533668863058509500', 'userName': userName, 'password': password, 'sID': '76561197992015823', 'secret':'Wmfv3899gc9'})
	return response.text.split(",")
def xor(data, key):
    return ''.join(chr(a ^ ord(b)) for (a, b) in zip(data, cycle(key)))
def gjp(password):
	gjp = password.encode()
	gjp = xor(gjp,'37526').encode()
	gjp = base64.b64encode(gjp).decode()
	return gjp

#print(GetAccID(config.server, config.userName))