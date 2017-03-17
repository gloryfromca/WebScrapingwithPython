import requests
session=requests.Session()

params={'username': 'zhanghui', 'password': 'password'}
s=session.post("http://pythonscraping.com/pages/cookies/welcome.php", data=params)
print('Cookie is set to:')
print(s.cookies.get_dict())
print('-------------')
print('Now go to the profile page...')
new_s=session.get("http://pythonscraping.com/pages/cookies/profile.php",cookies=s.cookies)
print(new_s.text)
