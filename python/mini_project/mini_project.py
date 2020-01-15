import csv
import readline
import pandas as pd

f = open('./mini_project/1.강원도_삼척.csv', 'r')
rdr = csv.reader(f)
column = next(rdr) #[컬럼명 읽기]
print(column)

