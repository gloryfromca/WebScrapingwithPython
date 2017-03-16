import pymysql
from urllib.request import urlopen 
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict,Counter
from  random import randint

def textdict(text):
    text=text.replace("\n","")
    text=text.replace("\"","")
    punctuation=[';','.',':',',']
    for symbol in punctuation:
        text=text.replace(symbol," "+symbol+" ")
    words=[word for word in text.split(' ') if word!='']
    textdict={}
    for i in range(1,len(words)): 
        if words[i-1]  not in textdict:
            textdict[words[i-1]]={}
        if words[i] not in textdict[words[i-1]]:
            textdict[words[i-1]][words[i]]=0
        textdict[words[i-1]][words[i]]+=1
    return textdict


text = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
textdict=textdict(text)

def retrieve_most_word(currentword):
    return sorted(textdict[currentword].items(),key=lambda t:t[1],reverse=True)[0][0]

chain=''
length=100
currentword='I'
for i in range(0,length):
    chain=chain+currentword+' '
    currentword=retrieve_most_word(currentword)
print(chain)

