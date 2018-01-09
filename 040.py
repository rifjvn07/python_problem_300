#문자열 분리
#사용자로부터 '10:00:01'와 같은 형태로 시간을 입력 받은  해당 시간이 00:00:00으로부터 몇 초가 지났는지 출력하라.

time = input('시분초를 xx:xx:xx 꼴로 입력하세요: ')
check = time.split(sep=':')
hour = int(check[0])*3600
min = int(check[1])*60
sec = int(check[2])

delta_time = hour+min+sec
print('00:00:00으로부터 총 지난 시간초는 ',delta_time,'입니다.')