#문자열 변경
#파이썬 문자열은 변경할 수 없는 객체이다. Slicing 메서드를 이용하여 'python'을 'Python'으로 변경하라.

lang = "python"
print(lang)
lang = 'P' + lang[1:]
print(lang)