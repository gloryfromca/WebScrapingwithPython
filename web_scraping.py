import requests
params={'username': 'zhanghui', 'password': 'password'}
r=requests.post("http://pythonscraping.com/pages/cookies/welcome.php", data=params)
print('Cookie is set to:')
print(r.cookies.get_dict())
print('-------------')
print('Now go to the profile page...')
new_r=requests.get("http://pythonscraping.com/pages/cookies/profile.php",cookies=r.cookies)
print(new_r.text)
