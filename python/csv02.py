import csv
import pandas as pd
import pymongo

conn = pymongo.MongoClient('192.168.99.100',32766)
db = conn.get_database("db3")
coll = db.get_collection("20200116")

f = open('./resources/exam1.csv','r')
rdr = csv.reader(f)
for line in rdr : 
    print(type(line))
    print(line)
    dict1 = dict()
    dict1[line[0]] = line
    print(dict1)
    coll.insert_one(dict1)

conn.close()

# # csv 구분자 : \t
# df = pd.read_csv('./resources/exam1.csv', delimiter=",")
# print(df)
# # NaN = 값 없음

# df = df.dropna() # NaN제거 : 결측치(빈 거) 제거 
# print(df)

# list1 = df.values.tolist() # DF -> list
# print(list1)
# dict1 = df.to_dict() # DF -> dict로 변경
# print(dict1)
