import json

try:
    with open("datalab\\mydata.json", "rb") as jsonFile:
        tempData = json.loads(jsonFile)
       #tempData = json.loads(jsonFile)#오류
        reusltData1 = tempData["name"]
        reusltData2 = tempData["age"]
        reusltData3 = tempData["address"]
        reusltData4 = tempData["email"]
        reusltData5 = tempData["empcheck"]
except TypeError as ex:
    error = ex

jsonData1 = {
        "empid": 12345678,
        "name" : "홍길동",
        "info" : [
            {"date1": "2022-01-21", "home": "서울시"},
            {"dep": "개발", "email": "aaa@aaa.co.kr"}
        ]
    }


try:
    with open("datalab\\mydata2.json", "w") as writeFile1: #변수 오류
        json.dump(jsonData1, writeFile) 
except NameError as ex:
    error1 = str(ex)


#json.dumps 타입오류냄
try:
    with open("datalab\\mydata3.json", "w", encoding="utf-8") as writeFile:
        json.dumps(jsonData1, writeFile, ensure_ascii=False) # 옵션으로 indent=숫자 , 한글을 완벽히 처리  
except TypeError as ex:
    error2 = str(ex)

# writeFile__ 변수를 다르게 설정하여 오류
try:
    with open("datalab\\mydata4.json", "w") as writeFile:
        json.dumps(jsonData1, writeFile__, ensure_ascii=False, indent=4) # 옵션으로 indent=숫자   # 한글이 문제가 있음
except NameError as ex:
    error3 = str(ex)

# sonData1__변수를 다르게 설정하여 오류
try:
    with open("datalab\\mydata5.json", "w", encoding="utf-8") as writeFile:
        json.dump(jsonData1__, writeFile, ensure_ascii=False, indent=4) # 옵션으로 indent=숫자 , 한글을 완벽히 처리  
except NameError as ex:
    error4 = str(ex)

#디버깅 변수 선언함(임시)
temp = 0
