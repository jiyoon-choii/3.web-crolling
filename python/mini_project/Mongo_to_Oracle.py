from xml.etree.ElementTree import parse
import pymongo

import cx_Oracle as oci
conn_o = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
cursor = conn_o.cursor()

conn = pymongo.MongoClient('192.168.99.100',32766)

##강원도_양양
table = db.get_collection("강원도_양양")
k_yy = parse('./mini_project/k_yangyang.xml')
coll = db.get_collection("20200115") #colloection 생성

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