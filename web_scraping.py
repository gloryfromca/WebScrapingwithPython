from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import re
import datetime
import random
from math import  log
random.seed(datetime.datetime.now())



def get_address(startpage):
    return startpage.replace("http://","").split('/')[0]

def get_internal(s,internal_url_piece,startpage):
    links=[]
    for link in s.findAll("a",href=re.compile("^(/|.*"+internal_url_piece+"/"+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in links:
                if re.compile("^/.*").match(link.attrs['href']):
                    links.append(startpage+link.attrs['href'])
                else:
                    links.append(link.attrs['href'])
    return  links

def get_external(s,internal_url_piece):
    links=[]
    for link in s.findAll("a",href=re.compile("^(http|www)((?!pdf)(?!linkedin)(?!"+internal_url_piece+").)*(?!(\.[a-z]+))$")):
    #linkedin可能需要加uer-agent才行
    #except .+字母 的文件
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in links:
                links.append(link.attrs['href'])
    return  links

def get_random_external(startpage):
    internal_url_piece=get_address(startpage)
    html=urlopen(quote(startpage,safe='/:?='))#quote 解决url非英文编码问题
    s=BeautifulSoup(html)
    links=get_external(s,internal_url_piece)
    if len(links)==0:
        links=get_internal(s,internal_url_piece,startpage)
        if len(links)==0:
            print("nothing!no internal and no external")
            return ""
        else:
            new_internal_link=links[random.randint(0,len(links)-1)]
            external_link=get_random_external(new_internal_link)
            return external_link
    else:
        return links[random.randint(0,len(links)-1)]

i=1
deep=5
def followexternallonly(startpage):
    global i
    global deep
    i=i+1
    external_link=get_random_external(startpage)
    print("external_link:"+external_link)
    while i<deep:
        if external_link=='':
            print('no way to find follow external')
            return 
        else:
            followexternallonly(external_link)

startpage="http://oreilly.com"
# followexternallonly(startpage)

#---------------------------------------------------------------------#
# collect a list of all external or internal  urls found on this page #
#---------------------------------------------------------------------#

allexternal=set()
allinternal=set()
def get_all_external(site):
    global allexternal
    global allinternal

    html=urlopen(site)
    s=BeautifulSoup(html)
    site_piece=get_address(site)

    internal_links=get_internal(s,site_piece,startpage)
    for link in internal_links:
        if link  not in allinternal:
            print('about to get link:'+link)
            allinternal.add(link)
            # get_all_external(link) #如果使用可能需要限制深度

    external_links=get_external(s,site_piece)
    for link in external_links:
        if link  not in allexternal:
            allexternal.add(link) 

startpage="http://oreilly.com"
# get_all_external(startpage)     

print(allexternal)
print(allinternal)
#观察获取效果




