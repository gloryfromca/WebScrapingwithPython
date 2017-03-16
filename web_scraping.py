import pymysql
from urllib.request import urlopen 
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict,Counter

def cleaninput(content):
    content=re.sub('\n+'," ",content).lower()
    content=re.sub('\[[0-9]*\]',"",content)
    content=re.sub(' +'," ",content)
    content=bytes(content,'utf-8')
    content=content.decode('ascii','ignore')
    cleaninput=[]
    content=content.split(' ')
    for item in content:
        item=item.strip(string.punctuation)
        if len(item)>1 or (item.lower=='a' or item.lower=='i'):
            if iscommon(item) is False:
                cleaninput.append(item)
    return cleaninput
    
def iscommon(ngram_item):
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it",
"i", "that", "for", "you", "he", "with", "on", "do", "say", "this",
"they", "is", "an", "at", "but","we", "his", "from", "that", "not",
"by", "she", "or", "as", "what", "go", "their","can", "who", "get",
"if", "would", "her", "all", "my", "make", "about", "know", "will",
"as", "up", "one", "time", "has", "been", "there", "year", "so",
"think", "when", "which", "them", "some", "me", "people", "take",
"out", "into", "just", "see", "him", "your", "come", "could", "now",
"than", "like", "other", "how", "then", "its", "our", "two", "more",
"these", "want", "way", "look", "first", "also", "new", "because",
"day", "more", "use", "no", "man", "find", "here", "thing", "give",
"many", "well"]
    if ngram_item in commonWords:
        return True
    return False


def ngrams(content,n):
    content=cleaninput(content)
    output={}
    for i in range(len(content)+n-1):
        ngram_item=" ".join(content[i:i+n])
        if ngram_item not in output :
            output[ngram_item] =0#initialize an unappeared string's count
        output[ngram_item] +=1
    return output


content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(),'utf-8')
n=2
ngrams=ngrams(content, n)  
sortedngrams = sorted(ngrams.items(), key=lambda t: t[1], reverse=True)
#sortedNGrams = sorted(ngrams.items(), key = operator.itemgetter(1), reverse=True)#be analogous to previous line

print(sortedngrams)
print(str(n)+'-grams count is '+str(len(ngrams)))

