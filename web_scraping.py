import pymysql
from urllib.request import urlopen 
from bs4 import BeautifulSoup
import re
import random
import datetime
import csv
from io import StringIO ,open
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager , process_pdf
from pdfminer.layout import LAParams

def readpdf(pdffile):
    rsrcmgr=PDFResourceManager()
    retstr=StringIO()
    laparams=LAParams()
    device=TextConverter(rsrcmgr,retstr,laparams=laparams)

    process_pdf(rsrcmgr,device,pdffile)
    device.close()

    content=retstr.getvalue()
    retstr.close()
    return content

pdffile=urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
output=readpdf(pdffile)
print(output)#输出结果为str
pdffile.close()

