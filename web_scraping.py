import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("https://en.wikipedia.org/wiki/Comparison_of_text_editors")
bs4=BeautifulSoup(html)
trs=bs4.find('table',{"class":"wikitable"}).findAll('tr')# a little hard code
#class="wikitable sortable jquery-tablesorter" class just use "wikitable"attribute 
csvFile = open("csv/editors.csv",'wt',encoding='UTF-8')
#Python 3 opens text files in the locale default encoding
writer = csv.writer(csvFile)
try:
    for tr in trs:
        row=[]
        for th in tr.findAll(['td','th']):
            th=th.get_text()
            row.append(th)#"add" is usage of set
            print(th)
        writer.writerow(row)
finally:
    csvFile.close()



