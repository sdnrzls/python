#11 딕셔너리 삭제하기
day_in_momth={'1월':31,'2월':28,'3월':31,'-1월':9545454}
day_in_momth.pop('-1월')
print(day_in_momth)

#12 딕셔너리와 반복문
day_in_momth={'1월':31,'2월':28,'3월':31,'4월':30,'5월':31}
for key in day_in_momth.keys():
  print(key)

#13 문자열 출력
day_in_momth={'1월':31,'2월':28,'3월':31,'4월':30,'5월':31}
for k,v in day_in_momth.items():
  print('{}은{}일이 있습니다'.format(k,v))

#14 random 
import random
list = ['빨','주','노','초','파','남','보']
random_element = random.choice(list)
print(random_element)

#15 random
random_number = random.randint(2,6)
print(random_number)

#16 문자열 출력하기
abc = ['빨','주','노','초','파','남','보']
random.shuffle(abc)
print(abc)

#17 datetime 실습
import datetime
print(datetime.date.today())

#18 문자열 실습
string1 = '''
 다스베이더가 말했다. 
 \"내가 니 애비다!\"
 그 말을 들은 루크는 \'깜짝\' 놀랐다.
 '''
list1 = string1.split()
print(list1[4])

#19 반복문 사용하기
days =[31,29,31,30,31,30,31,31,30,31,30,31]
for i in range(1,13):
  print('{}월의 날짜 일수는{}일 입니다.'.format(i,days[i-1]))

#20 정수와 실수
a=23
b=5

div = a//b
print("a를 b로 나눈 몫은{}입니다.".format(div))