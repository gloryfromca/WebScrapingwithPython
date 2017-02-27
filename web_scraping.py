import pymysql
from urllib.request import urlopen 
from bs4 import BeautifulSoup
import re
import random
import datetime



#连接数据库，使用数据库scraping，生成游标
conn = pymysql.connect(host='127.0.0.1', 
user='root', passwd='password', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE scraping")

random.seed(datetime.datetime.now())
start_url="http://en.wikipedia.org"


def get_links(url):# whole url input and whole url output 
    html=urlopen(url)
    bs4=BeautifulSoup(html)
    links=[]
    for link in  bs4.find("div",{"class":"mw-body-content"}).findAll("a",href=re.compile('^(/wiki/)((?!:).)*')):
        link=link.attrs['href']
        links.append(start_url+link)
    return links

def store(title,content):
    cur.execute('insert into pages(title,content) values(\"%s\",\"%s\")',(title,content))
    cur.connection.commit()

def store_title_content(url):
    html=urlopen(url)
    bs4=BeautifulSoup(html)
    title=bs4.find("h1",{"class":"firstHeading"}).get_text()
    #<h1 id="firstHeading" class="firstHeading" lang="en">Kevin Bacon</h1>
    content=bs4.find("div", {"id":"mw-content-text"}).find("p").get_text()
    store(title,content)


links=get_links(start_url)
try:
    while len(links)>0:
        link=links[random.randint(0,len(links)-1)]
        store_title_content(link)
        print('storing is OK!')
        links=get_links(link)
finally:
    cur.close()
    conn.close()

