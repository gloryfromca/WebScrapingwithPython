import pdb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.PhantomJS(executable_path='C:/Users/Administrator/Downloads/phantomjs-2.1.1-windows/bin/phantomjs.exe')
# print(type(driver))#type:class 'selenium.webdriver.phantomjs.webdriver.WebDriver'
# pdb.set_trace()
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
try:
    element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'loadedButton')))#使driver等待EC后抓取，返回的是element located（这里是：A button to click!）
    # 也可以不用返回element
finally:
    print(driver.find_element_by_id('content').text)
    driver.close()


