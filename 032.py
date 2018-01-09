#count 메서드
#다음 문자열에서 'python'문자열의 빈도수를 출력하라.

introduce = "python is widely used high-level language, python was conceived in the late 1980s"
check = 'python'
num = 0

a = introduce.split()
for i in a:
    if i == check:
        num += 1
    else:
        pass

print(num)