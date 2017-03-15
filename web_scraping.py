import pymysql
from urllib.request import urlopen 
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict,Counter

def cleaninput(content):
    content=re.sub('\n+'," ",content)
    content=re.sub('\[[0-9]*\]',"",content)
    content=re.sub(' +'," ",content)
    content=bytes(content,'utf-8')
    content=content.decode('ascii','ignore')
    cleaninput=[]
    content=content.split(' ')
    for item in content:
        item=item.strip(string.punctuation)
        if len(item)>1 or (item.lower=='a' or item.lower=='i'):
            cleaninput.append(item)
    return cleaninput

def ngrams(content,n):
    content=cleaninput(content)
    output=[]
    for i in range(len(content)+n-1):
        output.append(content[i:i+n])
    return output

html=urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")#type:class http.client.HTTPResponse
bs4=BeautifulSoup(html)
content = bs4.find("div", {"id":"mw-content-text"}).get_text()
n=2
ngrams = ngrams(content, n)  

def count_ngrams(ngrams): 
    s=[]
    for item in ngrams:
        s.append(str(item).lower())
    a=dict(Counter(s))#type:class 'collections.Counter' 
    return a #type:dict

#first#
s=sorted(count_ngrams(ngrams).items(), key=lambda t: t[1], reverse=True)
# print(s)#type:list
print('-----------------------')
#second#
ngrams = OrderedDict(sorted(count_ngrams(ngrams).items(), key=lambda t: t[1], reverse=True))
print(type(ngrams))#type:class 'collections.OrderedDict'
print(str(n)+'-grams count is '+str(len(ngrams)))

