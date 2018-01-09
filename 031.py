#문자열 자르기
#사용자로부터 파일명을 입력받은 후 확장자만 출력하는 프로그을 작성하라

file_name = input("filename: ")
check_file = file_name.split(sep='.')
result = check_file[1]
print(result)