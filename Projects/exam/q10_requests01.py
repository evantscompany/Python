import requests
import csv
from datetime import date, timedelta

yesterday = (date.today() - timedelta(1)).strftime('%Y%m%d')

#API 주소 설정
address = f'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=2845261cca5f1e3e03c60c3bbe28bbfd&targetDt={yesterday}'

#API요청 및 JSON 파싱
response = requests.get(address)
if response.status_code !=200:
    print(f"API 요청에 실패했습니다. 상태코드 : {response.status_code}")
    exit()

try:
    aa= response.json()
    items=aa['boxOfficeResult']['dailyBoxOfficeList']
except KeyError:
    print("JSON 구조가 예상과 다릅니다. 데이터를 찾을 수 없습니다.")
    exit()


movie_chart = f"일별박스오피스{yesterday}.csv"
header = ['랭킹', '제목', '개봉일', '누적 관객 수']

with open("files/movie_chart.txt","w",newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    print(f" ----{yesterday} 박스오피스 데이터 ({len(items)}) ----")
    for item in items :
        row = [
            item["rank"],
            item['movieNm'],
            item['openDt'],
            item['audiAcc']
        ]
        writer.writerow(row)
        print(f'[{item['rank']}위] {item["movieNm"]} (누적 :{item["audiAcc"]}명)')
print(f'\n 데이터 저장 완료! 파일명 : **{movie_chart}**')
print(f'파일은 현재 코드가 실행된 폴더에 저장되었습니다.')