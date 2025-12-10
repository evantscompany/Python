# 네트워크 상의 이미지파일을 다운로드 하는 프로그램

#requests [외부모듈 - 별도 설치필요 (터미널 > pip install requests)]

import requests

address = 'https://cdn.pixabay.com/photo/2021/02/12/12/19/starbucks-6008411_1280.jpg' # 이미지 파일의 인터넷경로(URL)
address =  input('다운로드를 원하는 이미지의 URL을 입력 : ')
response = requests.get(address)
print('응답코드 : ' , response.status_code)

#print(response.text)  #이미지는 글씨가 아님. 당연히 알 수 없는 글씨들이 표시됨. 
#이미지는 2진수의 픽셀 정보를 가지고 있는 데이터 파일임. 
#response 응답 객체는 본인이 읽어온 바이너리 데이터를 16진수로 보여줄 수 있음. 

print(response.content)
print()

# 읽어온 이미지 파일데이터 덩어리를 내 컴퓨터에 파일로 저장하기. (파일 처리 표준함수 open())



#file= open('Projects/download/aaa.jpg','wb') # wb는 write binary
#파일명이 같으면 기존의 파일이 덮어쓰기 되기에.. 중복되지 않는 파일명을 만들어야 함. 
# 가장 많이 활용되는 방법은 날짜와 시간 정보를 이용하여 파일명을 생성. 
import datetime

now = datetime.datetime.now()

# file_name = 'IMG_' + str(now)
# file_name = file_name.replace(' ','')
# file_name = file_name.replace('-','')
# file_name = file_name.replace(':','').replace('.','')
# file_name +=".png"

# 날짜를 이용한 특정 서식모양(format)으로 만들어주는 기능이 now 시간 객체에 이미 존재함.
file_name = now.strftime('%Y%m%d%H%M%S')+'.png'

print(file_name)

file = open('Projects/download/'+file_name,"wb")
file.write(response.content) #바이너리 데이터를 파일에 쓰기!
file.close()







































































