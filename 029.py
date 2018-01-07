# 도메인 추출
# 사용자로부터 웹 페이지 주소를 입력 받은 후 도메인을 출력하라. 도메인은 com, net, org만 지원한다. www는 반드시 포함한다.

# 도메인 입력
ad = input("adress: http://")
ad += '/'
adlist = ad.split(sep='/')
check_ad = adlist[0]
check = ['.com', '.net', '.org']
# 1.www체크
# 2. .com or .net or .org 체크

if ad[:3] == 'www':
    for i in range(0, 3):
        if check_ad[-4:] == check[i]:
            print("domain:", check_ad[-3:])
            break
        else:
            print("Enter .com or .net or .org")
else:
    print("Enter www")
