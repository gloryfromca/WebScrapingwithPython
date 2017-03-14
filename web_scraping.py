import pymysql
from urllib.request import urlopen 
from bs4 import BeautifulSoup
import re
import random
import datetime
import csv
from io import StringIO


data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
print(type(data))
print(data)#也是可以的，类型是字符串str
print('-----------------')
datafile=StringIO(data)
print(type(datafile))
print(datafile)#打印出来的是object，一个对象
print('-----------------')
csvReader=csv.reader(datafile)
for row in csvReader:
    # print(row)#打印出来的是一行行list对象
    print('the album \"'+row[0]+"\" was released in"+row[1])

