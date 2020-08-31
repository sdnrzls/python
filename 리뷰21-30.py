#21 while
numbers = [1,2,3]
length = len(numbers)
i = 0
while i<length:
  print(numbers[i])
  i= i+1

#22 enumarate
sizes = [33,35,34,37,32,35,39,32,35,29]
for i,size in enumerate(sizes):
  if size ==32:
    print("사이즈 32인 바지는 {}번째에 있다.".format(i+1))
    break

#23 try Except
try :
  a= 3/0
except :
  print("0으로 나눌 수 없습니다.")

#24 예외의 이름을 알고싶을때
try:
  a=5
  b=0
  c= a/b
except Exception as ex:
  print('다음과 같은 에러가 발생했습니다 : {}'.format(ex))

#25 딕셔너리 중복
shops = {
  "송일문방구":{"가위":500,"크레파스":3000},
  "알파문구":{"풀":800,"도화지":300,"A4용지":8000},
  "다이소":{"풀":500,"목공본드":2000,"화분":3000}
}
for shop, products in shops.items(): 
  for product, price in products.items():
    if product == "풀":
      print("{}: {}원".format(shop,price)) 

#26 bool 논린연산        
if []:
  print("[]은 True입니다.")
if[1,2,3]:
  print("[1,2,3]은/는 True입니다")
if{}:
  print("{}은 True입니다")
if{'abc':1}:
  print("{'abc':1}은 true입니다.")
if 0:
  print("0은/는 True입니다.")
if 1: 
  print("1은 true입니다.")

#27 논리연산자 or
a = 1 or 10
b = 0 or 10
print("a:{}, b:{}".format(a,b))

#28 리스트 실습
list3 = [1,2,3,4]
list3.insert(1,8)
print('첫 번째 자리에 8을 넣은 결과 : {}'.format(list3))
list3.sort()
print('list3을 작은 수 부터 큰 수로 정렬한 결과 : {}'.format(list3))
list3.reverse()
print('list3을 거꾸로로 정렬한 결과 : {}'.format(list3))

#29 문자열과 리스트
str1 = '오늘은 날씨가 흐림'
words = str1.split(' ')
print(words)

position = words[2].replace('흐림','맑음')
words[2] = position
print(words[2])

new_str = ' '.join(words)
print(new_str)



#30 리스트 slice
rainbow = ["r","o","y","g","b","n","p"]
red_colors = rainbow[0:3]
blue_colors = rainbow[4:]

print("red_color의 값 : {}".format(red_colors))
print("blue_color의 값 : {}".format(blue_colors))