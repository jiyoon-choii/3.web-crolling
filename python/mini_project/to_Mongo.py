from xml.etree.ElementTree import parse
import pymongo

conn = pymongo.MongoClient('192.168.99.100',32766)
db = conn.get_database("mini_project") #db생성

##강원도_양양
table = db.get_collection("강원도_양양")
k_yy = parse('./mini_project/k_yangyang.xml')

#print(k_yy)

all = k_yy.findall("Row")
# #print(all)

for tmp in all :
#     # print(tmp.findtext("시설종류"))
#     # print(tmp.findtext("CCTV설치여부"))
#     # print(tmp.findtext("CCTV설치대수"))
#     # print(tmp.findtext("보호구역도로폭"))

    kind = tmp.findtext("시설종류")
    cctv = tmp.findtext("CCTV설치여부")
    cctv_no = tmp.findtext("CCTV설치대수")
    wide = tmp.findtext("보호구역도로폭")

    dict1 = dict()
    dict1['시설종류']=kind
    dict1['CCTV설치여부']=cctv
    dict1['CCTV설치대수']=cctv_no
    dict1['보호구역도로폭']=wide
    table.insert_one(dict1)
conn.close()


##강원도_삼척
