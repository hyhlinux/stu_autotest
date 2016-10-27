from selenium import webdriver

# browser = webdriver.Chrome()
# # browser.get('http://seleniumhq.org/')
#
# browser.get('http://127.0.0.1:8000/')
#

import os
from selenium import webdriver
from pyvirtualdisplay import Display

# display = Display(visible=0, size=(800, 600))
# display.start()
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
print driver.page_source.encode('utf-8')
# driver.quit()
# display.stop()