from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import subprocess
import requests
from PIL import Image,ImageOps

def clean_pic(filename):
    image=Image.open(filename)
    image=image.point(lambda x: 0 if x<143 else 255)
    image=ImageOps.expand(image,border=20,fill='white')
    image.save(filename)



url="http://www.pythonscraping.com/humans-only"
html=urlopen(url)
bs4=BeautifulSoup(html)

imageLocation = bs4.find("img", {"title": "Image CAPTCHA"})["src"]
formBuildId = bs4.find("input", {"name":"form_build_id"})["value"]
captchaSid = bs4.find("input", {"name":"captcha_sid"})["value"]
captchaToken = bs4.find("input", {"name":"captcha_token"})["value"]

captchaurl="http://www.pythonscraping.com"+imageLocation
urlretrieve(captchaurl, "captcha.jpg")
clean_pic("captcha.jpg")

p = subprocess.Popen(["tesseract", "captcha.jpg", "captcha"], stdout=
subprocess.PIPE,stderr=subprocess.PIPE)
p.wait()
f=open("captcha.txt", "r")
captcha_response=f.read().replace(" ","").replace('\n',"")
if len(captcha_response)==5:
    params = {"captcha_token":captchaToken, "captcha_sid":captchaSid,
    "form_id":"comment_node_page_form", "form_build_id": formBuildId,
    "captcha_response":captcha_response,
    "name":"Ryan Mitchell",
    "subject": "I come to seek the Grail",
    "comment_body[und][0][value]":
    "...and I am definitely not a bot"}
    r = requests.post("http://www.pythonscraping.com/comment/reply/10",
    data=params)
    reponse=BeautifulSoup(r.text)
    if reponse.find("div",{"id":"message"}) is not None:
        print(reponse.find("div",{"id":"message"}).get_text())
    else:
        print("the number of the solutions of captcha is right,but later someting is wrong!")
else:
    print("the number of the solutions of captcha is wrong!")

