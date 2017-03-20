from bs4 import BeautifulSoup
import unittest
from urllib.request import urlopen
class TestWikipedia(unittest.TestCase):
    bs4=None
    def setUpClass():
        global bs4
        url="http://en.wikipedia.org/wiki/Monty_Python"
        bs4=BeautifulSoup(urlopen(url))
    def test_titletext(self):
        global bs4
        pageTitle = bs4.find("h1").get_text()
        self.assertEqual("Monty Python", pageTitle)
    def test_contentExists(self):
        global bs4
        content = bs4.find("div",{"id":"mw-content-text"})
        self.assertIsNotNone(content)
        
if __name__ == '__main__':
    unittest.main()