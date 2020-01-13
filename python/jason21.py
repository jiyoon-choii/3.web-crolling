import requests
import json
import pymongo

conn = pymongo.MongoClient('192.168.99.100',32766)
db = conn.get_database("db1") #db생성
table = db.get_collection("exam21") 

url = "http://ihongss.com/json/exam21.json"
str1 = requests.get(url).text
data1 = json.loads(str1)

data1=data1['boxOfficeResult']
print(data1['showRange'])
movie = data1['dailyBoxOfficeList']
print(type(movie))
print(movie)

for tmp in movie :
    print(tmp['rank'])
    print(tmp['movieNm'])
    print(tmp['openDt'])
    print(tmp['salesAmt'])   

    dict1 = dict()
    dict1['rank'] = tmp['rank']
    dict1['movieNm'] = tmp['movieNm']
    dict1['openDt'] = tmp['openDt']
    dict1['salesAmt'] = tmp['salesAmt']
    table.insert_one(dict1)

conn.close()




