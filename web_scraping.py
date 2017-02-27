import csv
csvfile=open('csv/test.csv','w+')#open方法
try:
    writer=csv.writer(csvfile)
    writer.writerow(("first column","second column","third column"))
    for i in range(10):
        writer.writerow((i,i+2,i*2))
finally:
    csvfile.close()#open打开的文件关掉
