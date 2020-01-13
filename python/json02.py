import requests
import json
import cx_Oracle as oci

conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
cursor = conn.cursor()

url = "http://ihongss.com/json/exam2.json"
str1 = requests.get(url).text
data1 = json.loads(str1) #str -> dict

ret = data1['ret']
ret1 = data1['ret1']

print(type(ret))
print(ret)

sql = """
    INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
    VALUES(:id, 'a', :name, :age, SYSDATE)
    """    

cursor.execute(sql, ret)
conn.commit()

sql = """
    INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
    VALUES(:id, 'a', :name, :age, SYSDATE)
    """    

cursor.execute(sql, ret1)
conn.commit()

