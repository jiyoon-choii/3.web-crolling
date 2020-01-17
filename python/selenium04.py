#20200117

from selenium import webdriver #selenium : 필요한 사이트 정보 가져오기 
import urllib.request
import time
from selenium.webdriver.common.keys import Keys 
import os # 파일 열기, 경로 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(os.path.join(BASE_DIR,'python'))

options = webdriver.ChromeOptions() #

# options.add_argument('headless') # 창 안 뜨게 하기 
options.add_argument("disable-gpu")   #add_argument 옵션 넣기 
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

driver = webdriver.Chrome(os.path.join(BASE_DIR,'python','chromedriver.exe'), options=options)
#driver 변수 생성 시 chromedriver의 위치 + (chrome_)options 인자를 함께 넘겨줘야 함 : chrome 사용할 때 추가적인 옵션 넘겨줌 
driver.get('https://www.naver.com')

driver.find_element_by_xpath('//*[@id="query"]').send_keys('케이크')
driver.find_element_by_xpath('//*[@id="query"]').send_keys(Keys.ENTER)
# from selenium.webdriver.common.keys import Keys 

driver.find_element_by_xpath('//*[@id="lnb"]/div/div[1]/ul/li[2]/a').click()

link = []
# '이미지' 카테고리
for i in range(1,30):
    try :
        img = driver.find_element_by_xpath('//*[@id="_sau_imageTab"]/div[2]/div[1]/div['+ str(i) +']/a[1]/img')
    except :
        img = driver.find_element_by_xpath('//*[@id="_sau_imageTab"]/div[2]/div[2]/div['+ str(i) +']/a[1]/img')

    link.append(img.get_attribute("src"))
    # get_attribute() :  selenium에서 추출한 요소의 속성값을 확인
    # src : 태그이름 

for idx,tmp in enumerate(link) :
    urllib.request.urlretrieve(tmp, os.path.join(BASE_DIR,'python','download',"n"+ str(idx) + ".jpg"))
    # urlretrive : url을 통해 이미지를 다운받는 코드 
    # / 사용 : urlretrieve(address, 저장될 이름) 
