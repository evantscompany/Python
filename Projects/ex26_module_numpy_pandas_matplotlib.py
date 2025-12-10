# 데이터 분석에 많이 사용되는 외부모듈 : numpy, pandas , matplotlib

#1) numpy ( numberic python ) : 리스트 같은 데이터에 대해 행렬 수학계산을 해주는  모듈

#1. 일반적인 파이썬의 리스트 연산 특징 

aaa = [10,20,30]
bbb = [4,5,6]

print(aaa)
print(bbb)

# 파이썬의 리스트 데이터를 덧셈하면 수학의 덧셈이 아니라 concat() 이 되어 결합됨. 

ccc=aaa+bbb
print()

# 위와 같은 리스트의 덧셈 특징을 수학적으로 계산해주는 모듈을 사용.. 나중에 머신러닝이나 데이터 분석에 사용 가능

#numpy 모듈 설치 
import numpy as np

#넘파이 전용 리스트 (배열)로 생성

aa= np.array([10,20,30])
bb= np.array([4,5,6])

print(aa)
print(bb)

# 리스트와 차이점. 산수 덧셈을 하면 배열의 요소끼리 덧셈을 수행함 

cc= aa+bb
print(cc)


#넘파이 배열을 본인의 요소개수를 볼 수 있는 값을 이미 보유하고 있음. len 사용 안함. 
print(aa.shape)
print(bb.shape) 

# 2차원 배열 ( 행렬 - 표 구조)

aaaa= np.array([
    
    [100,200,300,400],
    [500,600,700,800 ]
    
    ] )


print(aaaa.shape)

bbbb=np.array([
    [3,4,5,6],
    [7,8,9,0]
    ])

print(bbbb.shape)

#행렬의 수학연산.. (각 자리에 해당하는 요소끼리 산술연산)
cccc = aaaa+bbbb

print(aaaa-bbbb)
print(aaaa*bbbb)
print(aaaa/bbbb)

# 연산할때 주의.. 행렬 요소끼리 연산이기에 개수가 다르면.. ? 안됌.
# dddd=np.array([[10,20,30],[40,50,60]])
# print(dddd)

print('-'*30)
print()

#----------------------------------------------------------

#2) pandas -  데이터분석할 때 n차원 행렬(2차원 구조 표형태가 가장 흔함)의 구조를 용이하게 만들어주는 모듈
# excel, csv,tsv 등의 데이터 처리에 용이함.

import pandas as pd

#1차원 배열 구조 : [액셀의 한 열(column) 데이터들 - 세로줄]
aa= pd.Series(['sam','robin','hong'])

print(aa)
print()

#자동으로 부여되는 인덱스 번호를 원하는 식별자로 변경가능
bb = pd.Series(['seoul','tokyo','paris'], index=['korea','japan','france'])
print(bb)
print()

#2차원 배열 구조(표구조) : DataFrame 이라고 부름.
cc = pd.DataFrame([ 
    ['aa','bb','cc','dd'],
    ['11','22','33','44'] 
    ])

print(cc)
print()
# key:value 형태의 딕셔너리 타입으로 데이터 프레임을 생성하면 key 식별값이 column의 이름이 됨
dd=pd.DataFrame({'aa':[10,20,30],'bb':[100,200,300],'cc':[1000,2000,3000]})

print(dd)
print()

#csv파일을 읽어와서 dataframe 으로 만들기. 

ee= pd.read_csv('./files/scores.csv') # 읽어온 결과가 dataframe 객체임
print(ee)
print()

print(ee.head()) # 상위 다섯줄만 나옴 

print(ee.tail()) # 하위 다섯줄만 나옴
print(ee.head(3)) # 상위 세줄만

#행열모양 확인 변수
print()
print(ee.shape)


#컬룸 명도 확인 가능
print(ee.columns)
print(type(ee.columns))
print()

#컬룸명 변경하여 지정할 수도 있음. 
# ee.columns = ['aa','bb','cc','dd']
# print(ee)

#데이터프레임의 구조정보를 한번에 알려주는 기능함수
print(ee.info())

#특정한 컬룸데이터만 보기  -- 한 컬룸의 Series
print(ee['국어'])
print(sum(ee['국어'])/len(ee['국어']))
print(max(ee['국어']))
print(min(ee['국어']))
print(len(ee['국어']))
print('korea average : ', ee['국어'].mean())

#데이터분석(숫자데이터)에 많이 사용되는 평균, 최대, 최소값, 개수 등의 계산 정보를 한번에 볼 수 있는 기능
print()
print(ee.describe())
print()

#여러개의 컬룸을 동시에 보기 - 결과를 dataframe 으로 줌. 

print(ee[['영어','수학']]) 
print()


#데이터 프레임에서 특정 줄 (row) 데이터 가져오기. -- 첫번째 줄(행row)

row = ee.loc[0]
print(row)
print(type(row))
print()

#특정 범위의 행 데이터 가져오기 2~5번 행까지 데이터 가져오기

rows = ee.loc[2:5]
print(rows)
print(type(rows))

# 특정 범위 이후 모든 줄 .. 즉 끝까지. 
rows=ee.loc[2:]
print(rows)
print(type(rows))

rows = ee.loc[:4]
print(rows)
print(type(rows))

rows = ee.loc[:]
print(rows)
print(type(rows))

# 행과 열 모두를 지정 
rows = ee.loc[2:,'이름']
print(rows)
print()

rows = ee.loc[4:,['이름','수학']]
print(rows)

#데이터 전처리 할때 용이한 연산문법..
# 예) 모든 국어점수에 2배를 해야함. 

ee['국어']=ee['국어']*2 # 모든 각각의 요소들에 *2 연산 수행. 
#이것을 broadcast 브로드캐스팅 기법이라고 부름. 
print(ee)
ee['국어']=ee['국어']/2
print(ee)
print()

# 엑셀파일 읽기!!!!!

# 예전 버전에서는 xlrd 라는 모듈을 이용하여 엑셀을 읽어들였음.
# 현재 버전에서는 openpyxl 라는 모듈을 기본으로 사용함.
# openpyxl 는 별도 설치가 필요함
# import 안해도 판다스가 openpyxl 모듈을 import 하여 읽어들임.


gg = pd.read_excel('./files/scores.xlsx',engine='openpyxl')
print(gg)
print()

#특정 sheet의 표를 데이터 프레임으로 읽어오기
hh= pd.read_excel('./files/scores.xlsx',sheet_name='Scores')
print(hh)

ww=pd.read_excel('./files/seoul_weather_2025.xlsx')
print(ww)

print(ww.columns)
print(ww['강수량(mm)'].max())
print(ww['강수량(mm)'].mean())
print()

# 이후 수업은 머신러닝/데이터분석 수업에 만날예정. -> web수업 이후.

print('='*50)

# 데이터 분석을 용이하게 하려면 시각화를 해야함. 이를 위한 모듈
#3) matplotlib  모듈을 이용해 그래프 가능
# 숫자 데이터들에 대한 그래프를 쉽게 그려줌 [선 그래프, 막대 그래프, 원 그래프, 산점도 그래프 등 제공]


import matplotlib.pyplot as plt

#한글 깨지면, 한글 글꼴로 지정
plt.rcParams['font.family']='Malgun Gothic'


#1. 예제1) 하루 동안의 온도 변화 그래프(선 그래프)
# 시간별 온도 데이터셋 필요

#예제1: 하루 동안의 온도 변화 그래프 [ 선 그래프 plot() ]
# 시간(시)별 온도
hours = [6, 9, 12, 15, 18, 21, 24]           # 그래프의 x 축 데이터
temperature = [10, 14, 18, 20, 17, 13, 11]   # 그래프의 y 축 데이터


#plt.plot(hours,temperature)
# plt.plot(hours,temperature,marker='o'/
# plt.plot(hours,temperature,marker='x')
# plt.plot(hours,temperature,marker='v')/
# plt.plot(hours,temperature,marker='o',linestyle = '-')
# plt.plot(hours,temperature,marker='o',linestyle = '--')
# plt.plot(hours,temperature,marker='o',linestyle = ':')
# plt.plot(hours,temperature,marker='o',linestyle = '-',color='orange')



plt.title('하루 동안의 온도 변화')
plt.xlabel('시간(시)')
plt.ylabel('온도(°C)')
# plt.show()/

#----------------------------------------------------------------------------

#예제2: 학생 수학 점수 비교  [ 막대 그래프 ]
# 데이터 준비
students = ["홍길동", "손흥민", "류현진", "박세리"]
scores = [85, 60, 72, 92]

# plt.bar(students,scores,color='skyblue')

colors = ['orange','green','red','yellow']
plt.bar(students,scores,color=colors)



plt.title('학생별 수학 점수')
plt.xlabel('학생 이름')
plt.ylabel('점수')
plt.ylim(0,100)
plt.grid(axis='y')

# plt.show()




# 예제3: 롯데리아 월별 매출 데이터 시각화  [ 산점도 그래프 ]
# 롯데리아 월별 매출 데이터 준비 (가상)
data = {
    '월': ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
    '매출액(만원)': [4200, 3900, 4500, 4700, 5200, 5800, 6100, 6400, 5900, 5500, 5300, 5000]
}

# 판다스로 딕셔너리를 처리

df=pd.DataFrame(data)
print('롯데리아 월별 매출 데이터')
print(df)

plt.figure(figsize=(8,5)) # 너비 8인치, 높이 5인치 -- 그래프 여러개가 그려지는 도화지
plt.scatter(df['월'],df['매출액(만원)'],marker='o',color='tomato')

plt.title('롯데리아 2025년 월별 매출 변화')
plt.xlabel('월')
plt.ylabel('매출액')
plt.grid(True)

# 각 점 위에 매출 숫자 표시
for i,value in enumerate(df['매출액(만원)']):
    plt.text(i, value+50, f'{value}',ha='center',fontsize=14)

plt.show()





