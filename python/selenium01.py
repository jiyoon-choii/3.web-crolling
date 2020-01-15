# 서버-> 크롬 -> 파이썬 
# 이유 : 1. 로그인 이후 페이지 처리 2. javascript 처리 

from selenium import webdriver
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
#options.add_argument('headless') #화면표시 안됨 -> 원래 표시 안돼야 함 

options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

driver.get("http://ihongss.com/webboard")

driver.execute_script("document.getElementsByName('email')[0].value='20191216'")
#driver.find_element_by_name("email").send_keys('20191216')
driver.find_element_by_name("pw").send_keys('20191216')
driver.find_element_by_css_selector('#form1 > div:nth-child(4) > input').click() 
#selector

time.sleep(3)
driver.execute_script("alert('hello')")

# driver.get("http://ihongss.com/webboard") # 로그인 이후의 페이지
# html = driver.page_source
# soup = BeautifulSoup(html, 'html_parser')

# driver.close()


