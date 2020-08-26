# 기본 데이터 타입
int # 정수
float # 실수
bool # 불린(참 ,거짓)
str # 문자
list
tuple
set
dict

None # null과 비슷 (값이없을때)


#숫자 (int,float): 정수,실수
#type() : 자료형 리턴
# print(type(2 + 4))
#  print(type(2 - 4))
#  print(type(2 * 4))
#  print(type(2 / 4))
#소수점 있으면 float

# print(type(0.00001))
# print(type(5.0001))
# print(type(0.))
# print(type(0))

# print(type(9.9+1.1))

# 제곱과 나누기
# 거듭 제곱**
print(2**4)

#나누기 몫 //
print(10 // 4)

#나누기 나머지 %
print(10 % 3)

# Math 수학 함수
# 반올림 round
print(round(3.123456, 5))

#절대값 abs
print(abs(-20))

#숫자 계산시 우선순위
print((20-3)+2**2)


#이진수 변환 bin()
print(bin(5))
print(int('0b101',2))

#변수
iq = 190  # 메모리에 숫자 190은 바이너리(2진수)로 저정됨
print(iq)

#여러개의 변수를 초기화
a,b,c = 1,2,3
print(a)
print(b)
print(c)

놀이기구 = "자이로드롭"
a,b,c,d = 1,2,3,4
이름 = "박써니"
my_Name = "홍길동"

x = 10
print(x)

x,y,z = 1,2,3
print(x)
print(y)
print(z)

print(type(x))
print(type(y+0.1))
print(type(bin(z)))

print('''-------------------------------''')

#문자형 데이터 str
# 쌍따옴표, 한 따옴표
print(type("문자열!"))
var1 = '한따옴표'
var2 = "쌍따옴표"
print("문자열은 "+var1+var2)
print("문자열은",var1,var2)
# 따옴표가 3개씩 쓸때 ''' """

var3 = '''
따옴표 3개는 문장 모두를 처리하는 문자열은
'''

print(var3)
# 문자열(+)연산
성 = '홍'
이름 = '길동'
name = 성 + '' + 이름
print(name)

#타입 변환 str(),int(),float()
# num = input("숫자하나 입력 : ")
# print(int(num)+10)

#이스케이프 시퀀스
날씨 = "\t\t It\'s \"kind of\" sunny \n Have a nice Day !"
print(날씨)

#예제
String1 ='''다스베이더가 말했다.
\"내가 니 애비다!\" 
그말을 들은 루크는 \'깜짝\' 놀랐다.
'''
print(String1)

#f-string 문자열 포맷
name = "홍길동"
age = 20 #정수

# print('안녕하세요'+name+"님 
#나이가"str(age)+"이군요")

print(f'안녕하세요 {name}님 나이가 {age}살 이군요')

#print f 방법
print("나는 도시락 %d 개를  %s 먹었다." % (7,'배터지게'))

#문자열 .format() 함수방법
number = 20
welcome = "환영합니다"
base = '{}번 손님 {}'

print(base.format(number,welcome))

#예제 1
name = "logan"
color = "blue"
print('안녕하세요. 제 이름은{}이고 좋아하는 색상은 {}입니다'.format(name,color))
print(f'안녕하세요. 제 이름은{name}이고 좋아하는 색상은 {color}입니다.')

#문자열의 인덱스
String2 = '01234567'
print(String2[2])

#문자열 슬라이싱 [시작:끝]
print(String2[1:5]) #1번째부터 5번째 전까지
print(String2[0:3]) 
print(String2[:3]) #처음부터
print(String2[3:]) #끝까지

#[시작:끝:증감]
print(String2[::2]) #0 2 4 6
print(String2[::-1]) #거꾸로

#슬라이싱 예제
rainbow = ["빨", "주", "노", "초", "파", "남", "보"]
red_colors = rainbow[0:3]
blue_clors = rainbow[4:]
print(red_colors)
print(blue_clors)

#문자열의 변경불가
# string1 = '123'
# string1[0] = '9'

#len(문자열) 문자
print(len("123456"))

print('''-----------------------''')

#bool 참 거짓 형
bool1 = True
bool2 = False
bool3 = 1 < 2 #T
bool4 = 1 == 2 #F

print(bool1)
print(bool2)
print(bool3)
print(bool4)

x,y = 1,2
print(x>y)
print(x == y)
print(x != y)

print(bool(1)) #T
print(bool(0)) #F
print(bool('True')) #T
print(bool('안녕')) #T
print('''-----------------------''')


#논리 연산자

#and
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#or
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#not
print(not True)
print(not False)