from flask import Flask
import json
import requests

app = Flask(__name__) # flask 프로그램 시작 기본 값은 = app.py 파일을 생성

#함수 선언 
# 시작할 때 경로(route) 선언해야함
@app.route("/hello") # 웹 사이트 경로를 지정 - 앞에서 선언한 app 변수를 사용
def FlaskLab(): # 요청 - 메서드(함수) 이름 요청에서 사용하는 것
    return "Flask 데이터 응답" # 응답 -  return 에서 돌려주는 데이터가 응답



@app.route("/data1")
def data(): #(page1, page2, address):
    end_point = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
    key = "iQRdwNfyr4pUnPYTin2f07Wps5tqeblg1cA%2BihzCLinT63BwzOTOTdy63rJDOBIDBMjjaElmpWQb4X8Cdh2NDQ%3D%3D"
    parameters = "page=" + str(1)
    parameters += "&perPage=" + str(10)
    parameters += "&returnType=JSON"
    parameters += "&cond%5BorgZipaddr%3A%3ALIKE%5D=" + "관악구"
    parameters += "&serviceKey=" + key
    url = end_point + parameters

    content = requests.get(url).content

    return json.loads(content, encoding = "utf-8")


#a = data(1, 10, "관악구")

if __name__ == '__main__':
    app.run(debug=True)