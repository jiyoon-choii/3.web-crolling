import csv #csv 형식 사용 위해 불러들임
import readline 
import pandas as pd  

f = open('./mini_project/k_kangreung.csv','r', encoding="euc-kr") 
#1. 파일 열기 : 변수 f 로 지정

rdr = csv.reader(f)
#2. 파일 읽기(csv 형식으로) : 변수 rdr 로 지정

column = next(rdr)
#3. 첫 행 칼럼 지정 : 변수 column 으로 지정

for line in rdr :
#4. rdr(읽은 파일) 안에서 for 문 으로 한 줄 한 줄 돌리기 
    dict1 = dict()
    #5. 딕셔너리 형태로 만들기 위해 빈 딕셔너리 만들기 : 변수 dict1 로 지정
    for idx, val in enumerate(line): 
        #5-1. 딕셔너리 만들기 위해 안에서 for문 다시 돌리기 
        if val == "":
            val = "0"
        #5-2. value 에 값이 없을 경우를 생각하여 '0'으로 지정해주기  
        dict1[column[idx]] = val 
        #6. 딕셔너리 idx(key), val 값 지정하여 넣어주기 

    dict2 = dict()
    #7. 원하는 형태의 딕셔너리 만들기 위해 빈 딕셔너리 만들기 : 변수 dict2 로 지정 
    for i in dict1 :
    #8. dict2 만들기 위해 dict1 에서 for문 돌리기 
        if i == "시설종류" or i == "CCTV설치여부" or i == "CCTV설치대수" or i == "보호구역도로폭" :
            dict2[i] = dict1[i]
            #8-1. dict1의 원하는 값 dict2에 넣기  

    print(dict2)


