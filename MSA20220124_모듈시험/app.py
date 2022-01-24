import json
import requests
from flask import Flask

app = Flask(__name__)
#함수 선언 
# 시작할 때 경로(route) 선언해야함

@app.route("/")
def FlaskData():#startPage, pageCount, address): # 요청 받음
    keyValue = "iQRdwNfyr4pUnPYTin2f07Wps5tqeblg1cA%2BihzCLinT63BwzOTOTdy63rJDOBIDBMjjaElmpWQb4X8Cdh2NDQ%3D%3D"   
    dataURL = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
    dataURL += "page=" + str(1) + "&perPage=" + str(10)
    #dataURL += "&returnType=JSON"
    dataURL += "&cond%5BorgZipaddr%3A%3ALIKE%5D=%EA%B4%80%EC%95%85%EA%B5%AC" # 또는 본인 사는 지역구
    dataURL += "&serviceKey=" + keyValue
    # tempURL = r"https://api.odcloud.kr/api/apnmOrg/v1/list?page=1&perPage=10
    # &cond=""
    # &serviceKey=""
    # https://api.odcloud.kr/api/apnmOrg/v1/list?페이지 그리고 인증 값 연결
    dataResult = requests.get(dataURL)
    #공공데이터 요청 후 데이터 받기 : flask - request / requests 기능 사용"
    return json.loads(dataResult) # 공공데이터 결과 값 응답

print(FlaskData())
