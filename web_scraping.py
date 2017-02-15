from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
from math import  log
#-------------scrapy descendants of a wiki page---------------#
random.seed(datetime.datetime.now())
pages=set()#收集全部的条目地址
deep=1
def getlink(url,deep,i=0):#i控制遍历深度
    global pages 
    if i < deep:
        i=i+1
        html = urlopen("http://en.wikipedia.org"+url)
        s = BeautifulSoup(html)
        try:
            print(s.h1.get_text())
            print(s.find(id="mw-content-text").findAll("p")[0])
            print(s.find(id="ca-edit").find("span").find("a").attrs['href'])
        except AttributeError:
            print("This pages is missing something!")
        for link in  s.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
            # if 'href' in link.attrs:
            page=link.attrs['href'] 
            if page not in pages:#排重，重复的不再进行子内容的查询
                print('---------\n'+page)
                pages.add(page)
                getlink(page,deep,i)

links = getlink("",deep)
print(pages)
print(len(pages))
