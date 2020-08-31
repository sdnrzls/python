#리스트[ , , ]
print('리스트')
spam = ['개','고양이','박쥐','곰']
print(spam)
print(spam[0])
print(spam[3])

ham=[['고양이','강아지'],[10,20,30,40,50]]
print(ham)
print(ham[0])
print(ham[1])
print(ham[0][0])
print(ham[0][0][0]) # 고(고양이)
print(ham[1][4])

#음수 인덱스번호
print(spam[-1])
print(spam[-2])
print(spam[-4])

#슬라이싱
#첫번째 숫자(포함) : 두번째 숫자(포함안됨,이전)
print(spam[0:2])
print(spam[1:3])
print(spam[2:])
print(spam[:2])

#문자열
str = '가나다라마바사'
print(str[3])
print(str[:3])
print(str[2:5])

#예제1)
myList = [10,20,30,40],[1.1, 2.1, 3.1, 4.1],'ABCDEFG'
print(myList[2][:4])

print('-------------리스트-------------\n')

print('튜플')
#튜플(Tuple) ( , , )
#리스트와 비슷
#값을 변경할수 없으며 순서가 있음
#()괄호로 표현

list1 = [1, 2, 3]
list1[0] = 9
print(list1)

tuple1 = (1,2,3)
#tuple1[0] = 9 #에러
print(tuple1[2])

t1 = (1,3,'logan')
t2 = ('king','queen','jack')
print(t1+t2)
print(t2*3)
print(len(t1))

print('-------------튜플-------------\n')

#리스트의 메소드
print('리스트의 메소드')
list2 = ['개','고양이','박쥐','곰']

#추가 append()
#리스트의 맨마지막에 추가하는 메소드
list2.append('코뿔소')
print(list2)

# 빼기 pop()
list2.pop(0)
print(list2)

#삽입 insert
list2.insert(1,'호랑이')
print(list2)

#제거 remove
#아이템의 값으로 제거
list2.remove('박쥐')
print(list2)

#리스트의 정렬 sorted
#리스트의 요소를 순서대로 정렬
#(reverse = felse/true)
list2.sort()
print(list2)

list2.sort(reverse = True)
print(list2)