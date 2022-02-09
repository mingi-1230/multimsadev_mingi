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

def sum(list):
    data = 0
    for i in list:
        data = data + i
    return data

def average(list):
    data = 0
    for i in list:
        data = data + i
    aver = data / 4
    return aver

#길동1의 합계와 평균
gildong1_sum = sum([95, 90, 80, 50])
gildong1_average = average([95, 90, 80, 50])

#길동2의 합계와 평균
gildong2_sum = sum([100, 50, 90, 90])
gildong2_average = average([100, 50, 90, 90])

#길동3의 합계와 평균
gildong3_sum = sum([99, 60, 100, 40])
gildong3_average = average([99, 60, 100, 40])

#길동4의 합계와 평균
gildong4_sum = sum([55, 80, 80, 60])
gildong4_average = average([55, 80, 80, 60])

# 총 합계
all_sum = gildong1_sum + gildong2_sum + gildong3_sum + gildong4_sum

# 총 평균
all_average = all_sum / 16
