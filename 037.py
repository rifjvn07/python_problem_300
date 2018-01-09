#037 경로 분리
#사용자로부터 윈도우 디렉터리 경로를 입력받은 후 가장 최종 디렉터리를 출력하라.

path = input('경로: ')
check_path = path.split(sep='\\')
print(check_path)

result = check_path[-1:]
print(result)