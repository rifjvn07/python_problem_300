#문자열 잘라내기
#종목코드에 공백과 줄바꿈 기호가 포함되어 있다. 공백과 줄바꿈 기호를 제거하고 종목코드을 추출하라.

code = '        000660\n        '
strip_code = ''
for i in code:
    if i != ' ':
        if i != '\n':
            strip_code += i

print(strip_code)
