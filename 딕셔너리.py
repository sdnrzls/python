#딕셔너리 {}
#키와 값의 쌍
print(type({}))
dict1 = {}
dict1[1] = 'a'
dict1['b'] = 2
dict1['c'] = 'd'

#myCat 만들기
myCat = {
  '사이즈' : '소형',
  '색' : '연한갈색',
  '특기' : '잠자기'}
print('내 고양이 색깔은 '+myCat['색'])
#딕셔너리는 인덱스가 없고 대신 key값으로 해당 value값을 얻음

#key값과 value값 구분
print(list(myCat.keys()))
print(list(myCat.values()))

#반복문을 사용해서 출력
for k in myCat.keys():
  print(k)
for v in myCat.values():
  print(v)
for k,v in myCat.items():
  print(k,v)

#get() 메소드
#key값이 있는 경우 리턴 없을경우 None 리턴
print(myCat.get('이름'))
print(myCat.get('색'))

#문자 카운트
count = {} #딕셔너리 생성
message = "할일을 하자 !"
for char in message:
  count.setdefault(char, 0)
  count[char]= count[char]+1
print(count)