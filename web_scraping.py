from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
from math import  log
random.seed(datetime.datetime.now())

i=1

def get_address(startpage):
    return startpage.replace("http://","").split('/')[0]

def get_internal(s,internal_url_piece):
    links=[]
    for link in s.findAll("a",href=re.compile("^(/|.*"+internal_url_piece+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in links:
                links.append(link.attrs['href'])
    return  links

def get_external(s,internal_url_piece):
    links=[]
    for link in s.findAll("a",href=re.compile("^(http|www)((?!pdf)(?!linkedin)(?!"+internal_url_piece+").)*((\.[a-z]+))$")):
    #linkedin可能需要加uer-agent才行
    #except .+字母 的文件
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in links:
                links.append(link.attrs['href'])
    return  links

def get_random_external(startpage):
    internal_url_piece=get_address(startpage)
    html=urlopen(startpage)
    s=BeautifulSoup(html)
    links=get_external(s,internal_url_piece)
    if len(links)==0:
        links=get_internal(s,internal_url_piece)
        if len(links)==0:
            print("nothing!no internal and no external")
            return []
        else:
            new_internal_link=links[random.randint(0,len(links)-1)]
            external_link=get_random_external(origin_url+new_internal_link)
            print("i'm here")
            return external_link
    else:
        return links[random.randint(0,len(links)-1)]
    
def followexternallonly(startpage):
    global i
    i=i+1
    external_link=get_random_external(startpage)
    if len(external_link)==0:
        print('no way to find follow external')
        return "sss"
    else:
        print("external_link:"+external_link)
        while i<5 :
            if followexternallonly(external_link)=="sss":
            #如果no way to find follow external,则不再继续
                break
            else:
                followexternallonly(external_link)

origin_url="http://oreilly.com"
followexternallonly(origin_url)

