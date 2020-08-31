import json
import difflib

data = json.load(open('data.json')) # json 파일을 불러옴

def translate(word): #data 안에 있는 단어가 있으면 value를 리턴
    word = word.lower()
    if word in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]    
    else:
        match = difflib.get_close_matches(word, data.keys())
        if len(match) > 0:
            print(f'혹시 입력한 단어가 {match[0]}인가요?')
            answer = input('맞으면 y 아니면 n 입력 : ')
            if answer=='y':
                return data[match[0]]
        return "그런 영단어는 없습니다. 철자를 확인해주세요"

word = input("영어단어 입력: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)