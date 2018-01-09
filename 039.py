# 문자열 개수 확인
# 'Python python pYthon java JAVA'
res = 'Python python pYthon java JAVA'
print(res)
check = res.lower()
print(check)
spcheck = check.split(sep=' ')
print(spcheck)
python = 'python'
num = 0
for i in range(0,len(spcheck)):
    if spcheck[i] == python:
        num += 1
    else:
        pass

print(num)
