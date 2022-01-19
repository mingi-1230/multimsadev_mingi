multiple_3 = []
multiple_5 = []
#3의 배수와 
for i in range(1, 101):
    if i % 3 == 0:
        multiple_3.append(i)

#5의 배수를 구한다.
for i in range(1, 101):
    if i % 5 == 0:
        multiple_5.append(i)

#set으로 변환한다
setdata1 = set(multiple_3)
setdata2 = set(multiple_5)

#셋 합집합
data = setdata1 | setdata2 

#셋 교집합 3과 5의 공배수가 나온다
common_multiple = setdata1 & setdata2

print(data)
print(common_multiple)
