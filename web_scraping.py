from selenium import webdriver
driver = webdriver.PhantomJS('C:/Users/Administrator/Downloads/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.get('http://www.pythonscraping.com/')
driver.get_screenshot_as_file('pythonscraping.png')