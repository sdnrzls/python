#문자열 메소드
# 대 소문자
string1 = 'hello world'
print(string1.upper())
print(string1.lower())
print(string1)

print('title title'.title())

spam = '''
안촉촉한 초코칩 나라에 살던 안촉촉한 초코칩이 촉촉한 초코칩나라의 촉촉한 초코칩이 되고싶어서
촉촉한 초코칩나라에 갔는데'''
print(spam.count('초코칩'))
print(spam.count('촉촉'))


#알파벳,숫자,공백 인지 확인
print('hello'.isalpha())
print('hello123'.isalpha())
print('hello123'.isalnum())
print('123'.isdecimal())
print(' '.isspace())

#문자열의 시작과 끝을 체크
print('hello world!'.startswith('h'))

#문자열 삽입 join
print('!'.join('abcd'))
#리스트를 문자열로 만듬
print('=='.join(['1','2','3']))
print('-'.join(['2020','05','20']))

#문자열 나누기 split()
print("2020-05-20".split('-'))
print("2020 05 20".split())

#공백제거
print('   하이   ')
print('   하이   '.strip())

#문자열 바꾸기 replace
a = "인생은 짧다."
print(a.replace("인생은","하루가"))