import pymysql
from urllib.request import urlopen 
from bs4 import BeautifulSoup
import re
import random
import datetime

textpage=urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
# print(type(textpage.read()))
# print(textpage.read())#好像只能read（）方法只能读取一次，所以先调用后赋值
s=textpage.read().decode('utf-8')
# s=str(textpage.read(),'utf-8')#equal to one above  

