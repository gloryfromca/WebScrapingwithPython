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

cur.execute("create database if not exists wikipedia")
cur.execute("USE wikipedia")
cur.execute("create table if not exists wikipedia.pages (id int not null AUTO_INCREMENT,url varchar(255) not null,created timestamp not null default current_timestamp, primary key(id)) ")
cur.execute("create table if not exists wikipedia.links (id int not null AUTO_INCREMENT, frompageid int null,topageid int null,created timestamp not null default current_timestamp,primary key(id ))")

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


def insert_to_links(frompageid,topageid):
    cur.execute('select * from links where frompageid=%s and topageid=%s',(int(frompageid),int(topageid)))
    if cur.rowcount==0:
        cur.execute("INSERT INTO links (frompageid,topageid) VALUES (%s,%s)",(int(frompageid),int(topageid))) 
        cur.connection.commit()
    
pages=set()#可以改写为从数据库中查询
def get_links(url,recursionlevel):# whole url input and whole url output 
    global pages
    if  recursionlevel>2:#not 5 cause saving time
        return ;

    pageid=insert_page_if_not_exists(url)
    html=urlopen(start_url+url)
    bs4=BeautifulSoup(html)

    for link in  bs4.findAll("a",href=re.compile('^(/wiki/)((?!:).)*')):
        link=link.attrs['href']
        insert_to_links(pageid,insert_page_if_not_exists(link))
        pages.add(link)
        if link not in pages:
            get_links(link,recursionlevel+1)

get_links("/wiki/Kevin_Bacon",0)
cur.close()
conn.close()