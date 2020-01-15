from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()

options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

driver.get("https://www.banharu.com/shop/member.html?type=login")

driver.find_element_by_name("id").send_keys('jwjy13')
driver.find_element_by_name("passwd").send_keys('ehrehrdl@6')

# classname > selector > xpath > full xpath
# driver.find_element_by_css_selector('#login > div.page-wrap > div > form > fieldset > a.btn_none.btn_03.btn_login > input').click() 
driver.find_element_by_xpath('//*[@id="login"]/div[2]/div/form/fieldset/a[1]').click() 
#login > div.page-wrap > div > form > fieldset > a.btn_none.btn_03.btn_login

driver.get("http://www.banharu.com")
html = driver.page_source
soup = BeautifulSoup(html, 'html_parser')

driver.close()