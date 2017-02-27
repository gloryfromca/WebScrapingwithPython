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
cur.execute("USE wikipedia")

random.seed(datetime.datetime.now())
start_url="http://en.wikipedia.org"


def insert_page_if_not_exists(url):
    cur.execute("select * from pages where url= %s",(url))
    if cur.rowcount==0:
        cur.execute("INSERT INTO pages (url) VALUES (%s)", (url))
        cur.connection.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]


def insert_to_links():
    cur.execute()
    
links=set()#可以改写为从数据库中查询
def get_links(url,recursionlevel):# whole url input and whole url output 

    global links
    pageid=insert_page_if_not_exists(url)

    if  recursionlevel>5:
        return ;
    html=urlopen(url)
    bs4=BeautifulSoup(html)

    for link in  bs4.find("div",{"class":"mw-body-content"}).findAll("a",href=re.compile('^(/wiki/)((?!:).)*')):
        link=start_url+link.attrs['href']
        insert_to_links(pageid,insert_page_if_not_exists(link))
        links.add(link)
        if link not in links:
            get_links(link,recursionlevel+1)

get_links(start_url,0)