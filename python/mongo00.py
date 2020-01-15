from bs4 import BeautifulSoup
import requests
import pymongo

conn = pymongo.MongoClient('192.168.99.100',32766)
db = conn.get_database("book") #db생성
table = db.get_collection("table1") #colloection 생성

"""
<div class="rank_brand_box">
    <div class="ranking_num"><span class="num">1</span>위</div>
    <div class="ranking_tt">
        <div class="bd_tt"><span class="big_tt">문학동네</span> <br /> 
       브랜드지수 2,620,536점 <a href="javascript:void(0)" onclick="fn_LayerPublisherScore('#help_PublisherBrandScore1728'); return false;"><img src="//image.aladin.co.kr/img/shop/2012/blet_question.gif" align="absmiddle" ></a><div id="help_PublisherBrandScore1728"></div><br/>
        </div>      
    </div>
"""

url = "https://www.aladin.co.kr/publisher/wbest.aspx?CID=50993"
str = requests.get(url)
#print(str.text)

soup = BeautifulSoup(str.text, 'html.parser')

all_divs = soup.find_all("div")
soup.find_all("div",{"rank_brand_box"})
all_divs_tit4 = soup.find_all("div",{"rank_brand_box"})

#print(all_divs_tit4)
for tmp in all_divs_tit4 :        
    all_p = tmp.find("div",{"ranking_num"})    
    all_p1 = tmp.find("div",{"ranking_tt"})    
    find_all_p1 = all_p1.find("span")
    print(all_p.text)
    #print(all_p1.text)
    print(find_all_p1.text)
    dict1 = dict()
    dict1['순위']=all_p.text
    dict1['출판사명']=find_all_p1.text    
    table.insert_one(dict1)

conn.close()

    
