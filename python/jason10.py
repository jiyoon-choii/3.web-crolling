import requests
import pymongo
import json

conn = pymongo.MongoClient('192.168.99.100',32766)
db = conn.get_database("db1") #db생성
table = db.get_collection("exam10") 

url = "http://ihongss.com/json/exam10.json"
str1 = requests.get(url).text
data1 = json.loads(str1)

data = data1['data']

print(type(data))
print(data)

for tmp in data :
    print(tmp['id'])
    print(tmp['name'])
    print(tmp['age'])
    print(tmp['score']['math'])
    print(tmp['score']['kor'])

    dict1 = dict() #{}
    dict1['id'] = tmp['id'] 
    dict1['name'] = tmp['name'] 
    dict1['age'] = tmp['age']
    dict1['score'] = tmp['score']['math']
    dict1['score'] = tmp['score']['kor']
    table.insert_one(dict1)

conn.close()
