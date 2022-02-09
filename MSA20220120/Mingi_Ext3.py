'''
1. 4개의 과목을 합계(전체 합계, 개인 합계) + 평균 (개인 평균/ 전체 평균)
홍길동1 '국어 : 95, '영어' : 90, '수학': 80, '과학':50  홍길동 1의 합계, 평균
홍길동2 '국어 : 100, '영어' : 50, '수학': 90, '과학':90 홍길동 2의 합계, 평균
홍길동3 '국어 : 99, '영어' : 60, '수학': 100, '과학':40 홍길동 3의 합계, 평균
홍길동4 '국어 : 55, '영어' : 80, '수학': 80, '과학':60  홍길동 4의 합계, 평균
 - 전체 4명의 합계, 평균

for/ while / if / elif
7가지 방법으로 코드를 작성: 결과는 모두 같아야 함
'''
gildong1 = {"국어" : 95, "영어" : 90, "수학" : 80,"과학" : 50}
gildong2 = {'국어' : 100, '영어' : 50, '수학' : 90, '과학' : 90}
gildong3 = {'국어' : 99, '영어' : 60, '수학' : 100, '과학' : 40}
gildong4 = {'국어' : 99, '영어' : 60, '수학': 100, '과학':40}

all_data = [
    {"국어" : 95, "영어" : 90, "수학" : 80,"과학" : 50},
    {'국어' : 100, '영어' : 50, '수학' : 90, '과학' : 90},
    {'국어' : 99, '영어' : 60, '수학' : 100, '과학' : 40},
    {'국어' : 99, '영어' : 60, '수학': 100, '과학':40}
]

def average(list):
    data = 0
    for i in list:
        data = data + i
    aver = data / len(list)
    return aver

values1 = gildong1.values()
values2 = gildong2.values()
values3 = gildong3.values()
values4 = gildong4.values()


#길동1 합계, 평균
gildong1_sum = sum(values1)
gildong1_average = average(values1)

#길동2 합계, 평균
gildong2_sum = sum(values2)
gildong2_average = average(values2)

#길동3 합계, 평균
gildong3_sum = sum(values3)
gildong3_average = average(values3)

#길동4 합계, 평균
gildong4_sum = sum(values4)
gildong4_average = average(values4)

