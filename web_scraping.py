import os
from urllib.request import urlopen  
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

baseurl="http://pythonscraping.com"
downloaddirectory='downloaded'


def getabsoluteurl(url):
    if url.startswith('http://www.'): 
        url=url.replace('http://www.','http://')#必须注意url=，没有这个，url本身不变化。
    elif url.startswith("www."):
        url=url.replace('www.','http://')
    elif url.startswith("http://"):
        url=url
    elif url.startswith("/"):
        url=baseurl+url
    else:
        url=baseurl+"/"+url

    if baseurl not in url:
        return None
    return url
def downloadpath(url,baseurl,downloaddirectory):
    url=url.replace(baseurl,'')
    path=downloaddirectory+url
    directory=os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

html=urlopen(baseurl)
bs4=BeautifulSoup(html)
downloadedlist=bs4.findAll(src=True)#注意之前这里的用法，src=True or src=false
for downloaded in downloadedlist:
    # print(downloaded+'-----mark')
    url=getabsoluteurl(downloaded['src'])
    if url is not None:
        print(url)
        try:
            # if "jpg" not in  url.split('/')[-1]:#只要还用urlretrieve，就无法保存一些后缀不是文件名的链接对应的文件
            urlretrieve(url,downloadpath(url,baseurl,downloaddirectory))
        except OSError as e :
            # raise e #有这个好像会报错，没有就跳过继续执行
            print("osError")




