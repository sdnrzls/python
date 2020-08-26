 
#예제 1
a = "Life is too short, you need phthon"
if "wife" in a:
  print("wife")
elif "python" in a and "you" not in a:
  print("python")
elif "shirt" not in a:
  print("shirt")
elif "need" in a:
  print("need")
else: print("none")

#예제 2
count = 1
sum = 0
while count < 1001:
  if count%3 == 0:
    sum+=count
  count+=1
print(sum)

#예제 3
for i in range(1,6):
  while i>0:
    print('*', end='')
    i -=1
  print()

for i in range(6):
  print('*'*i)

#예제 4
scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
conut = len(scores)
for score in scores:
  sum +=score
print(sum/conut)

#리뷰

#문제 1
print('Hello World')

#문제 2
print('월요일','화요일','수요일')
x = 1000
y = '일이삼사오'
z = 1.2345
print(x,y,z)

#문제 3
print('신씨가 소리질렀다. \"도둑이야\"')

#문제 4
print('안녕하세요.\n만나서\t반갑습니다')

#문제 5
x = 10
y = 3
print("%.2f"%(x/y)) # %f%사에이 .2는 소숫점 둘째자리까지

#문제 6
x = int(input("정수1:"))
y = int(input("정수2:"))
print(f'합은 : {x+y} 입니다')

#문제 7
a = 'x'
for i in range(1,11):
  print(a,end='')


#문제 8
x = int(input("first number:"))
y = int(input("second number:"))
print(f'add : {x+y}')
print(f'add : {x-y}')
print(f'add : {x*y}')
print(f'add : {x/y}')

#문제 9
aircon = 48584
month = 36
print(f'총금액은{aircon*month}원')

#문제 10
name = input("이름 : ")
color = input("색상 :")
print('안녕하세요. 제 이름은{}이고 좋아하는 색상은 {}입니다.'
.format(name,color))