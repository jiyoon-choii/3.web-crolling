# pip install cx_oracle
import cx_Oracle as oci

# 접속하기
conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
print(conn)
# 커서 생성
cursor = conn.cursor()

#SELECT
sql = "SELECT * FROM MEMBER"
cursor.execute(sql)
data = cursor.fetchall()
print(data)

# INSERT 
sql = """
    INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
    VALUES(:1, :2, :3, :4, SYSDATE)
    """
arr = ['a1','a1','홍길동',33]
cursor.execute(sql, arr)
conn.commit()