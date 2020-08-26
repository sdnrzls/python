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
    if product =='_': 
     print("{}: {}원".format(shop,price)) 

