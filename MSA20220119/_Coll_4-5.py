# list(range(7, -8, 2))는 왜 안될까...
listdata = list(range(7, -8, -2))

#자료의 타입을 확인한다.
print(type(listdata))

#listdata를 튜플로 변환
tupledata = tuple(listdata)

#튜플로 변환되었는지 타입 확인
print(type(tupledata))
