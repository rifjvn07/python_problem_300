#문자열 분리 및 합치기
#'spam egg' 문자열을 'egg spam'으로 변경하라.

res = 'spam egg'
print(res)
re_res = res.split()
#print(re_res)
result = re_res[1] +' '+ re_res[0]
print(result)