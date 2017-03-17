import requests
params={'firstname':"zhang","lastname":"hui"}
r=requests.post("http://pythonscraping.com/files/processing.php", data=params)
print(r.text)