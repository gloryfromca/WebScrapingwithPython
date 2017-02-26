
#https://en.wikipedia.org/w/index.php?title=Jadunath_Singh&offset=&action=history
#https://en.wikipedia.org/wiki/Jadunath_Singh
import datetime 
from bs4 import BeautifulSoup
from urllib.request import urlopen
import random
import re
import json

random.seed(datetime.datetime.now())

def getCountry(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json/"
        +ipAddress).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get("country_code")


def getlinks(link):#whole url  input and  whole url  output
    html=urlopen(link)
    bs4=BeautifulSoup(html)
    links=set()
    if bs4.find("div",{"id":"mw-content-text"})  is not None:
        for link in bs4.find("div",{"id":"mw-content-text"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
            link="https://en.wikipedia.org"+link.attrs['href']
            if link not in links:
                links.add(link) 
        return links
    else:
        return []

def gethistoryips(link):
    history_url=link.replace("/wiki/","/w/index.php?title=")+"&limit=250&action=history"
    html=urlopen(history_url)
    bs4=BeautifulSoup(html)
    ips=set()
    if  bs4.find("ul",{"id":"pagehistory"}) is not None:
        for ip in bs4.find("ul",{"id":"pagehistory"}).findAll("a",{"class":"mw-userlink mw-anonuserlink"}):#findAll可能是一个list或者set
            ip=ip.get_text()
            if ip  not in ips:
                ips.add(ip)
        return ips
    else:
        return []


deep=1
i=0
links=getlinks('https://en.wikipedia.org/wiki/Python_(programming_language)')
while(len(links)>0 and i<deep):
    for link in links:
        print('----------------')
        historyips=gethistoryips(link)
        for historyip in historyips:
            if ":" not in historyip:
                print(historyip +"  is from  "+ getCountry(historyip))
    newlink=links[random.randint(0,len(links)-1)]
    links=getlinks(newlink)
    i=i+1