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


data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
datafile=StringIO(data)
csvReader=csv.DictReader(datafile)
for row in csvReader:
    print(row)

