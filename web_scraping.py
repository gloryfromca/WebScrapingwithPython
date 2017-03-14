import pymysql
from urllib.request import urlopen 
from bs4 import BeautifulSoup
import re
import random
import datetime
import csv
from io import StringIO ,BytesIO,open
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager , process_pdf
from pdfminer.layout import LAParams
from zipfile import ZipFile

wordfile=urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()#type:bytes
wordfile=BytesIO(wordfile)#type:io.BytesIO object
document=ZipFile(wordfile)#type:zipfile.ZipFile file=<_io.BytesIO object at 0x0000000003582990> mode='r'
xml_content=document.read('word/document.xml')#type:bytes

s=xml_content.decode('utf-8')#type:str

# print(s)

bs4=BeautifulSoup(s)
textelems=bs4.findAll('w:t')
for textelem in textelems:
    closetag=''
    try:
        style=textelem.parent.previousSibling.find("w:pstyle")
        if style is not None and style['w:val']=='Title':
            print('<h1>')
            closetag="</h1>"
    except  AttributeError:
        pass
    print(textelem.text)
    print(closetag)


            


