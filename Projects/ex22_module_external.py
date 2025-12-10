#외부 모듈 - 파이썬팀이 아닌 개인 또는 회사에서 별도로 개발한 파이썬 코드들의 집합체 (모듈)

#파이썬 팀에서 개발한 모듈이 아니기에.. 파이썬 설치할때 같이 설치되어 있지 않음. 
#그래서 사용하려면 그 모듈을 다운로드 하여 컴퓨터에 설치 후 import 해서 사용해야 함. 
#이를 외부모듈을 서버에 가지고 있으면서 필요할 때 컴퓨터에 설치해주는 도구(프로그램) : pip ( package installer for python)
#pip 는 CLI 설치도구임. 

#1. requests - 자동디코딩, 자동 예외처리,json 모듈 이미 연동
# HTTP 요청 작업이 용이함. 쿠키, 세션, 파일 업로드 등 많은 작업이 편하게 구현가능.
# 설치방법) vs code 에서 터미널(cmd,명령프롬프트) 창을 열고 설치명령어 입력
# > pip3 install 모듈명

#설치완료되었으면.. 마치 표준모듈처럼 import 해서 사용하면 됌.

import requests
address = 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/aaa.txt'
response = requests.get(address) # 서버의 데이의 요청한 결과정보를 가진 객체를 리턴
#응탑객체 response 를 통해 데이터와 상태정보를 알 수 있음.

print('응답 코드 번호 : ', response.status_code)
print('읽어 들인 데이터 : ', )
print(response.text)
print()

# json 모듈 기능도 이미 포함한 상태


address = 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/hhh.json'
response = requests.get(address)
print(response.status_code)
print(response.text)

aa=response.json() # 알아서 json 문자열을 분석하여 dictionary 로 만든것..
print(aa['data'][0]['name'])
print()
print('-'*30)


#[간단하게 open Api 실습] 영화진흥위원회 open api 데이터 다루기
# 조회날짜가 고정되면 안됨. 변수여야함. 
import datetime

now = datetime.datetime.now()
#날짜의 차를 계산해주는 객체가 존재함. 
now = now - datetime.timedelta(days=1)



#yyyymmdd 형식만들기 
yesterday = str(now.year)+str(now.month)+str(now.day)
print(yesterday)
yesterday="{:04d}{:02d}{:02d}".format(now.year,now.month,now.day)
print(yesterday)
print(type(yesterday))



print()

address = 'https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=2845261cca5f1e3e03c60c3bbe28bbfd&targetDt='+str(yesterday)
response= requests.get(address)
print(response.status_code)
print(response.text)

aa = response.json()
print(aa['boxOfficeResult']['boxofficeType'])

items = aa['boxOfficeResult']['dailyBoxOfficeList']

print()
print(items)
print()

for item in items:
    rank = item["rank"]
    movie_name = item['movieNm']
    open_date=item['openDt']
    audience_acc=item['audiAcc']

    print('랭킹 : ', rank)
    print('제목 : ', movie_name)
    print('개봉일 : ', open_date)
    print('누적 관객 수 : ', audience_acc)
    print('-'*20)

print()


with open("movie.csv",'w',encoding='utf-8'):
    
