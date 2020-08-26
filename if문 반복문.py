#if 문
name = 'Alice'
if name == 'Alice':
  print('반가워요'+name)
  print('종료')

#if else
name = 'logan'
if name == 'jay':
  print('당신이 jay 이군요.')
elif name == 'logan':
  print('당신이 '+name+'이군요')
else :
  print('누구신가요')

#예제
#name = input("당신의 이름?")

if bool(name) :
  print(f'당신의 이름은 {name} 입니다')
else : 
  print('이름을 입력하지 않았군요!') 


print('''----------/분리선/-----------''')

#while
count = 0
while count<3: #count 가 3보다 작을때 계속
  print('횟수: ',count)
  count += 1 #1씩 증가

treeHit = 0
while treeHit < 10 :
  treeHit += 1
  print(f"나무를 {treeHit}번 찍었습니다.")
  if treeHit == 10 :
    print("나무가 넘어 갑니다.")

#continue break
count = 0
while count < 10:
  count += 1
  if count < 4:
    continue
  if count == 8:
    break
print(count)

#coffee.py
#coffee = 10
# while True:
#   money = int(input("돈을 넣어 주세요 : "))
#   if(money) == 300:
#     print("커피를 줍니다.")
#     coffee = coffee -1
#   elif money > 300:
#     print(f"거스름돈 {money -300}를 주고 커피를 줍니다")
#     coffee = coffee -1
#   else:
#     print("돈을 다시 돌려주고 커피를 주지않습니다.")
#     print(f"남은 커피의 양은 {coffee}개 입니다")
#   if coffee == 0:
#     print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#     break  


print('''----------/분리선/-----------''')

#for 반복문
for num in [1,2,3]:
  print(num)

for ch in '홍길동':
  print(ch)

animals = ["개","고양이","스컹크","코끼리","아나콘다"
,"바다코끼리"]
for animal in animals:
  print(animal)

# range()
# () 괄호안의 숫자 0~숫자-1까지
for n in range(3):
  print(n)
#(start,end) start~end-1
for n in range(4, 6):
  print(n)

#구구단
for i in range(1,10):
  print('{}x{}={}'.format(2,i,2*i))

for i in range(2,10):
  for j in range(1,10):
    print('{}x{}={}'.format(i,j,i*j),"",
    end="")
    