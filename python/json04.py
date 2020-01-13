import requests
import json

url = "http://ihongss.com/json/exam4.json"
str1 = requests.get(url).text
data1 = json.loads(str1) #str -> dict

ret = data1['ret']

print(type(ret))
print(ret)

