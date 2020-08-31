# 파일 읽기,닫기
# f = open("fruits.txt",encoding='utf-8')
# content = f.read() #변수에 저장 (여러번 사용시)
# f.close
# print(content) 

#자동으로 close
# with open("fruits.txt",encoding='utf-8') as f:
#     content = f.read()

# print(content)

#파일쓰기 (파일명이 없을경우 생성)
# with open("vegi.txt", "w", encoding='utf-8') as myFile:
#     myFile.write('무\n')
#     myFile.write('배추\n')
#     myFile.write('토마토\n')
#     myFile.write('브로콜리\n')

#파일 내용 아래에 덧 붙이기 (업데이트 + 읽기)
# with open("vegi.txt", "a+", encoding='utf-8') as myFile:
#     myFile.write('붙여쓰기\n')
#     content = myFile.read()
#     print(content)

#예제
f = open("fruits.txt",encoding='utf-8')
content = f.read()
v = open("vegi.txt",encoding='utf-8')
content2 =v.read()
f.close
v.close
with open("fruitVegi.txt", "+a", encoding='utf-8') as fv:
    fv.write(content)
    fv.write(content2)
    fv.seek(0)
    content3 = fv.read()
print(content3)

