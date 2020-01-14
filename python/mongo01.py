# pip install pymongo
import pymongo

conn = pymongo.MongoClient('192.168.99.100',32766)
db = conn.get_database("db1") #db생성
table = db.get_collection("table1") #colloection 생성

dict1 = {"순위":"a","출판사명":35}

table.insert_one(dict1) #추가하기
data1 = table.find()
for tmp in data1 :
    print(tmp)
conn.close()
