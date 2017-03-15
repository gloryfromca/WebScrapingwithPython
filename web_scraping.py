import pymysql
from urllib.request import urlopen 
from bs4 import BeautifulSoup
import re

def ngrams(content,n):
    content=re.sub('\n+'," ",content)
    content=re.sub(' +'," ",content)
    content=bytes(content,'utf-8')
    content=content.decode('ascii','ignore')

    content=content.split(' ')
    output=[]
    for i in range(len(content)+n-1):
        output.append(content[i:i+n])
    return output

html=urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")#type:class http.client.HTTPResponse
bs4=BeautifulSoup(html)
content = bs4.find("div", {"id":"mw-content-text"}).get_text()
n=2
ngrams = ngrams(content, n)   
print(ngrams)
print(str(n)+'-grams count is '+str(len(ngrams)))


