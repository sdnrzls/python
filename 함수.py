# 내장 함수

# dir 객체가 가진 메소드를 보여준다
# print(dir('1'))

# len()
print(len([1,2,3]))
print(len("1234"))

# max() min()
print(max([1,2,3]))
print(max("한글이다"))

# sum()
A = [70,60,50]
print(sum(A))
print(sum(A)/len(A))

# 함수만들기
def hello():
  print('Hi')
  print('안녕!')
  print('니하오')

hello()
hello()

# 매개변수가 있는 함수
def hello2(name):
  print('하이'+name)

hello2('길동')
hello2('펭수')

# 매개변수와 리턴값이 있는 함수
print(len("문자열길이"))

def hello3(name):
  print('Hi '+name)
  return len(name)

print(hello3("logan"))

#예제 1
def is_odd(num):
  if(num%2==0):
    return("짝수")
  elif(num%2!=0):
    return("홀수")

print(is_odd(1))
print(is_odd(2))

#예제 2
def avgNums(*num):
  return(sum(num)/len(num))

print(avgNums(1,2,3,4,5,6,7,8,9,10))

#전역변수와 지역변수
x = 10 #전역변수
def foo():
  print(x) #전역변수

foo()
print(x) #전역변수

def foo2():
  y=20 #지역변수
  print(y)

foo2()
# print(y) 에러. foo2의 지역변수는 출력불가능 

def spam():
  eggs = 99
  bacon()
  print(eggs)

def bacon():
  ham = 101
  eggs = 0

spam()

def div10(num):
  try:
    return 10/num
  except:
    print('에러발생')

print(div10(2))
print(div10(0)) #에러발생
print(div10(5))

#숫자 맞추기 놀이
import random

name = input("당신의 이름은?")
print("안녕하세요"+name+"님",
"1에서 20까지 숫자중 하나를 생각합니다")

rannum = random.randint(1,20)
count=0
for dap in range(10):
  if(dap==6):
   print('틀렸네요. 정답은{}입니다'.format(rannum))
   break
  num = int(input("맞춰보세요"))
  if(num<rannum):
    print('그 숫자보다 큰수')
    count += 1
    continue 
  elif(num>rannum):
    print('그 숫자보다 작은수')
    count += 1
    continue
  elif(num==rannum):
    print('잘맞췄어요 {}님 {}번째 만에 맞췄습니다'.format(name,count))
    break 