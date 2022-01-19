import statistics #통계형함수를 불러옴

#딕셔너리 설정
data = {
    "국어": 95,
    "영어": 90,
    "수학": 80,
    "과학": 50,
}

#딕셔너리의 values 값만 불러옴
values = data.values()

#data 딕셔너리의 values 값을 value변수에 선언
value = list(values)

#평균을 내는 함수를 사용하여 average에 저장
average = statistics.mean(value)

#디버깅용
data = 0
