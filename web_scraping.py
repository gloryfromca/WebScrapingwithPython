from bs4 import BeautifulSoup
import unittest
from urllib.request import urlopen
import re

class TestWikipedia(unittest.TestCase):
    url=None
    bs4=None

    def test_Pageproperties(self):
        global url
        global bs4
        url="http://en.wikipedia.org/wiki/Monty_Python"
        for i in range(1,10):
            titles=self.titleMatchurl()
            self.assertEquals(titles[0],titles[1])
            self.assertTrue(self.contentExists())
            url=self.nextUrl()
            print("Done!")
    def titleMatchurl(self):
        global url 
        global bs4
        bs4=BeautifulSoup(urlopen(url))
        title=bs4.find("h1").get_text()
        urltitle=url[(url.index('/wiki/')+6):]
        urltitle=urltitle.replace("_"," ")
        return [title.lower(),urltitle.lower()]
    def contentExists(self):
        global bs4

        content = bs4.find("div",{"id":"mw-content-text"})
        if content is not None:
            return True
        return False
    def nextUrl(self):
        global bs4
        url="http://en.wikipedia.org"+bs4.find("div", {"id":"bodyContent"}).find("a",href=re.compile("^(/wiki/)((?!:).)*$"))['href']
        print(url)
        return url
if __name__ == '__main__':
    unittest.main()



        


