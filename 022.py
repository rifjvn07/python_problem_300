# 문자열 나누기
# 여러개의 종목코가 구분";"로 연결된 문자열이 있다. 구분자를 기준으 각 종목 코드를 나누고 이를 파이썬 리스트로 저장하.

companies = '000660;060310;0133340;095570;068400;006840'
codes = companies.split(sep=';')
print(codes)
