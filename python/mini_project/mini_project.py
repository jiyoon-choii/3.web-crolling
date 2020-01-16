import csv
import readline
import pandas as pd
# import pymongo

# conn = pymongo.MongoClient('192.168.99.100', 32766)
# db = conn.get_database("mini_project")
# coll = db.get_collection("k_samcheock") 

f = open('./mini_project/k_samcheock.csv', 'r', encoding="euc-kr")

rdr = csv.reader(f)

column = next(rdr)
# print(column)
# ['시설종류', '대상시설명', '소재지도로명주소', '소재지지번주소',


for line in rdr:    
    # print("====================")
    # print(line)
    # ['초등학교', '삼척초교', '강원도 삼척시 교동로 43', '강원도 삼척시 당저동 45-1', '37.449424', '
    dict1 = dict()
    for idx, val in enumerate(line): #[1,2,3,4,5,6] # enumerate ->index, value
        # 0, '초등학교'   / 1, tccc
        # { "시설종류": '초등학교',    ...  }
        if val == "":
            val = "0"
        dict1[column[idx]] = val 
    #print(dict1)

    dict2 = dict()
    for i in dict1 :
        if i == '시설종류' or i == 'CCTV설치여부' or i == 'CCTV설치대수' or i == '보호구역도로폭' :
            dict2[i] = dict1[i]
    print(dict2)


    # dict2 = dict()
    # for 



    # 전체 딕셔너리 생성
    # 해야할 것
    # 1. 원하는 형태의 딕셔너리 = 몽고디비에 넣을 수 있는 형태의 딕셔너리
    # 2. 데이터베이스에 넣는 것
    # 한 것
    # 1. 필요한 정보만 가져오는 것 확인






               



#     coll.insert_one(dict1)
# conn.close()