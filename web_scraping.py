import pymysql
from urllib.request import urlopen 
from bs4 import BeautifulSoup

def ngrams(input,n):
    input=input.split(' ')
    output=[]
    for i in range(len(input)+n-1):
        output.append(input[i:i+n])
    return output

html=urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")#type:class http.client.HTTPResponse
bs4=BeautifulSoup(html)
content = bs4.find("div", {"id":"mw-content-text"}).get_text()
n=2
ngrams = ngrams(content, n)   
print(ngrams)
print(str(n)+'-grams count is '+str(len(ngrams)))


