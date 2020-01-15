import pymongo

import cx_Oracle as oci
conn_o = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
cursor = conn_o.cursor()

conn = pymongo.MongoClient('192.168.99.100',32766)
db = conn.get_database("db1") #db생성
coll = db.get_collection("20200115") #colloection 생성
#coll.insert_one({"id":"a", "name":"b","age":3})

# SELECT * FROM 20200115
data1 = coll.find({})
for tmp in data1:
    del tmp['_id']
    print(tmp)
    sql = """
        INSERT INTO TABLE1(NO, ID, NAME, AGE)
        VALUES(SEQ_TABLE1_NO.nextval, :id, :name, :age)
    """
    cursor.execute(sql, tmp)
    conn_o.commit()

conn_o.close()  # 오라클 연결 끊기
conn.close()    # 몽고 DB 연결 끊기 


# # SELECT * FROM 20200115 WHERE ID='a'
# data2 = coll.find({"id":"a"})

# # SELECT ID, NAME FROM 20200115 WHERE ID='a'
# data3 = coll.find({"id":"a"},{'id':1, 'name':1})
# for tmp in data3:
#     print(tmp)

# # SELECT * FROM TABLE WHERE age > 10 
# data4 = coll.find({'age':{"$gt":40}})
# for tmp in data4:
#     print(tmp)

# # SELECT * FROM TABLE ORDER BY name ASC
# data5 = coll.find().sort('name',1) # 1(ASC), -1(DESC)
# for tmp in data5:
#     print(tmp)

# #SELECT * FROM TABLE WHERE age>=10 AND age<=30 
# data6 = coll.find({"age":{"$gte":10, "$lte":30}})

# # SELECT COUNT(*) FROM TABLE
# data7 = coll.find().count()
# print(data7)

# # SELECT * FROM TABLE WHERE ID='a' or name = 'b'
# data8 = coll.find({'$or':[{"id":'a'},{"name":'b'}]})