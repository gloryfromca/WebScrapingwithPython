import pymysql
from urllib.request import urlopen 
from bs4 import BeautifulSoup
import re
import random
import datetime


html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bs=BeautifulSoup(html)
text=bs.find('div',{'id':'mw-content-text'}).get_text()
content=bytes(text,'utf-8')
content=content.decode('utf-8')
print(content)