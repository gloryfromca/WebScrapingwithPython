import pymysql
from urllib.request import urlopen 
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict,Counter
from  random import randint

conn=pymysql.connect(host='127.0.0.1',user='root',passwd='password',charset='utf8')
cur=conn.cursor()
cur.execute('use wikipedia')

class SolutionFound(RuntimeError):
    def __init__(self, message):
        self.message = message
        
def getlinks(currentid):
    cur.execute('select topageid from links where frompageid=%s',(currentid))
    if cur.rowcount==0:
        return None
    else:
        return [x[0] for x in cur.fetchall()]
def constructDict(currentid):
    links_list=getlinks(currentid)
    if links_list is None:
        return {}
    a=dict(zip(links_list,[{}]*len(links_list)))
    return a


def searchDepth(targetPageid,currentid,linkTree,depth):
    if depth==0:
        return linkTree
    if not linkTree:
        linkTree=constructDict(currentid)
        if not linkTree:
            return {}
    if targetPageid in linkTree.keys():
        print('target_id: '+str(targetPageid)+' FOUND!')
        raise SolutionFound("process_id:"+str(currentid))
    for key,value in linkTree.items():
        try:
            linkTree[key]=searchDepth(targetPageid,key,linkTree[key],depth-1)
        except SolutionFound as e:
            print(e.message)
            raise SolutionFound("page:"+str(currentid))
    return linkTree
try:
    s=searchDepth(156,2,{},4)
    print('NO solution found')
except SolutionFound as e:
    print(' start_id: '+e.message.split(':')[1])
#错误的层层抛出来<-->找到结果后search过程经过的id层层抛出