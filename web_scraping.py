#AIzaSyA_J5Ba4pA_A6pvYe-f2JzT4en-iiyTj18 google maps elevation API key
import json
from urllib.request import urlopen
def getcountry(ipaddress):
	response=urlopen("http://freegeoip.net/json/"+ipaddress).read().decode('utf-8')
	responsejson=json.loads(response)
	return responsejson.get("country_code")
print(getcountry("45.78.33.186"))
