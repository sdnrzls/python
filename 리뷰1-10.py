#01 함수만들기
def add(a,b):
  result= a+b
  print("{}+{}={}".format(a,b,result))
add(10,5)

#02 함수의 리턴
def quiz2(a,b):
  return a+b
print(quiz2(10,5))  

#03 List 리스트
rainbow=['빨','주','노','초','파','남','보']
first_color = rainbow[0]
print('무지개의 첫번째 색은 {}이다'.format(first_color))

#4 리스트 사용하기
last_color=rainbow[-1]
print('무지개의 첫번째 색은 {}이다'.format(last_color))

#5 리스트 추가하기
list1=[1,2,3]
list1.append(4)
print(list1)
list2=[1,2,3]
list2 += [4]
print(list2)

#6 리스트 수정
numbers = [1,2,3,4,5]
n = 5
if n in numbers:
  print('{}가 리스트에 있다'.format(n))

#7 리스트 지우기
list1=[1,2,3]
list1.remove(2)
print(list1)

#8 딕셔너리 만들기
days_in_month = {
  '1월':'31일',
  '2월':'28일',
  '3월':'31일'
}
print(days_in_month)

#9 딕셔너리 입력 자료형
dict = {
  '이름' : '홍길동',
  '번호' : 1010,
  '취미' : ['낮잠','숨쉬기','커피']
}
print(dict)

#10 딕셔너리 수정하기
days_in_month = {
  '1월':'31일',
  '2월':'28일',
  '3월':'31일'
}
days_in_month['2월']='29일'
print(days_in_month)
