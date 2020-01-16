from bs4 import BeautifulSoup
import requests
import pymongo

"""
<div class="tit3">
	<a href="/movie/bi/mi/basic.nhn?code=135874" title="스파이더맨: 홈커밍">스파이더맨: 홈커밍</a>
</div>
"""

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date=20170714"
str = requests.get(url)
#print(str.text)

# HTML 문서 검색
# soup.find_all   => 여러개 
# soup.find       => 첫번째 거 세개 
# soup.select     => 여러개 (=find_all)

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("movie")
coll = db.get_collection("Naver")

soup = BeautifulSoup(str.text, 'html.parser')
all_div_tit3 = soup.find_all('div',{"class":"tit3"})
# => <div class+"tit3"></>
for tmp in all_div_tit3:
    # <a href="#", id="aaa">가나다</a> 태그 사이에 있는 '가나다' 찾기 = .text
    print(tmp.find("a").text)  
    print(tmp.find("a").attrs)  



