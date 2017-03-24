import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# time.sleep(5)
searchbox = driver.find_element_by_name('wd')
searchbox.send_keys('python怎么使用selenium')
searchbox.submit()
time.sleep(5)

driver.quit()