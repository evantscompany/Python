# import requests

# response=requests.get('https://hslohas.co.kr/?srsltid=AfmBOopmX1Rv7KN7GW6qPLi5xVND1kn0hRZDrocafikmTeeWDitWGZun')

# print('응답신호 : ', response.status_code)
# print()

# from bs4 import BeautifulSoup

# soup = BeautifulSoup(response.text,'html.parser')

# p_list= soup.select_one('#span_product_price_text')

# print(p_list[0])

# import requests
# from bs4 import BeautifulSoup

# response = requests.get('https://dshop.dietshin.com/main.asp')
# print(response.status_code)

# soup = BeautifulSoup(response.text ,'html.parser' )
# p_list=soup.select('.launch_price')
# print(len(p_list))
# print(p_list[1])


import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "ko-KR,ko;q=0.9",
}
response = requests.get('https://tonywack.com/category/men/327/',headers=headers)
print(response.status_code)

soup = BeautifulSoup(response.text ,'html.parser' )
p_list=soup.select_one('#anchorBoxId_3764 > div.description > ul > li > span:nth-child(2)')
print(p_list.string)