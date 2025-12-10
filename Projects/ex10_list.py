# 파이썬에서 대량의 데이터를 다루는 문법[List,Tuple,Dictionary,{Set}]

# 대량의 데이터를 다루는 문법이 별도로 등장한 이유.. 알아보기..

# 학생 3명의 성적데이터를 저장..

#이때 리스트 같은 대량의 데이터를 다루는 문법이 있다면..
aaa=[70,80,50]
print(aaa)
print(aaa[0])
total=0

for e in aaa:
    print(e)
    total=total+e
print()

#1. List []- 요소의 값 변경 및 추가/삭제 가능
aaa=[10,20,30,40]
#리스트를 저장한 변수를 출력하면 그 안에 있는 값들을 모두 보여줌.
print(aaa)
print(type(aaa))

# 요소값 개별사용 - 인덱스 번호
print(aaa[0])
print(aaa[1])
print(aaa[2])
print(aaa[3])
#print(aaa[4]) #4번은 에러. 값이 없기 때문.


print()
print()
# 요소의 개수가 많으면.. 인덱스 번호를 직접 쓰기 짜증.. 반복문으로 인덱스 번호를 자동으로 증가되도록
for n in range(4): #0~3
    print(aaa[n])    
print()

#for 문법의 대량의 데이터에서 요소를 반복적으로 뽑아오는 것임. 인덱스 번호를 뽑지말고.. 그냥 바로 aaa리스트의 요소를 뽑으면 더 간단

for n in aaa:
    print(n)
    

#역순으로 출력하고 싶다면..
for n in range (3,-1,-1):
    print(aaa[n])

#역순 2번째 방법
for n in range(4):
    print(aaa[3-n])

print()

#1~3번 방의 요소만 출력 [범위 출력]
for n in range(1,4,1): #1,2,3
    print(aaa[n])
print()

for n in range(1,4,1): #1,2,3
    print(aaa[n])
print()

# 모든 요소값들에 1을 더한 값을 출력하세요.. 요청

for e in aaa:
    print(e+1)

#모든 요소값을 더한 총합계산도 가능
#total=aaa[0]+aaa[1]+....
total=0
for e in aaa:
    total=total+e
print('총합 : ',total)

#리스트의 요소들 중에서 가장 큰 값 출력.

# m = aaa[0]
# if m < aaa[1]: m=[1]
# if m < aaa[2]: m=[2]
# if m < aaa[3]: m=[3]
# print(m)

m= aaa[0]
for n in range(1,4):
    if m<aaa[n]: m=aaa[n]
print(m)

print("-"*50)

# 요소값 변경 - 인덱스 번호 사용

aaa[0]=100
print(aaa)

# 요소 추가 - append(), insert()
# aaa[4]=50 error

aaa.append(50) # 50 이라는 값을 리스트 마지막에 추가
print(aaa)
print(aaa[1])

aaa.insert(1,600)
print(aaa)
print(aaa[1])


#요소 삭제 - remove() , del 연산자, clear()

aaa.remove(100) # 100이라는 값을 가진 요소를 제거
print(aaa)

del aaa[2] # aaa[2]요소를 제거
print(aaa)

aaa.clear() # 모두 삭제
print(aaa)

# 요소의 개수를 알려주는 파이썬의 내장 기능함수 len()
print('요소 개수 : ' , len(aaa))

# 요소들의 자료형이 달라도 상관없음. - 다른 언어는 안되지만 파이썬은 됌
aaa=[10, 3.14 , False , 'sam']
print(type(aaa[2]))


#반복문으로도 접근 가능
for e in aaa:
    print(e)
print()


# 리스트가 가진 유용한 여러 기능함수들 소개..
#1) 요소의 순서를 뒤집기
aaa.reverse() # 원본 리스트가 변경됨.
print(aaa)

#2) 요소 정렬
aaa=[4,15,7,2,3,4,5,8,3,6,2,3,4,1,1,1,4,5,2,4,5]
aaa.sort()
print(aaa)

#3) 요소 중 특정 값의 인덱스 번호(위치) 얻어오기
idx= aaa.index(15) #15라는 숫자가 있는 위치번호
print(idx)

#4) 특정 값이 리스트안에 있는지 여부.. in 연산자
print( 7 in aaa)
print(70 in aaa)
[print(5 not in aaa)] #있지 않니.

#5) 특정 값이 리스트 안에 몇개인지.. 
print(aaa.count(1),"개")

#6) 특정 값을 꺼내오기 .. 원본에서 없어지는 것임.
n=aaa[2] # 사용하는거지 꺼내오는게 아님
print(n)
print(aaa)

n=aaa.pop(2) # 이건 아예 끄집어 내는것.
print(n)

#7) 다른 리스트를 한방에 추가하기. [리스트의 확장]
aaa=[10,20,30]
bbb=[4,5,6]

aaa.extend(bbb)
print(aaa)
aaa.sort()
print(aaa)
#.extend() 기능 잘 사용 안함. 왜? + 연산을 하면 리스트 확장 기능 발동 

print(aaa+bbb)

#-----------------------------------------------------

# 2차원 리스트 -- 리스트의 요소가 또 다른 리스트인 것..
aaa = [ [10,20,30],['aa','bb'],[3.14,12.2,300,500] ]

aaa = [ 
    [10,20,30],
    ['aa','bb'],
    [3.14,12.2,300,500] 
    ]

print(aaa)
print(aaa[0])
print(aaa[0][0])
print(aaa[1][0])

#len() 기능은 리스트의 요소개수를 알려줌

print(len(aaa[2]))

# 각 요소값들 접근 하여 사용
print(aaa[0][0],end="\t")
print(aaa[0][1],end="\t")
print(aaa[0][2],end="\t")
print()

print(aaa[1][0],end="\t")
print(aaa[1][1],end="\t")
print()

print(aaa[2][0],end="\t")
print(aaa[2][1],end="\t")
print(aaa[2][2],end="\t")
print(aaa[2][3],end="\t")
print()

print()

#반복문으로 위 작업 처리.

a=len(aaa[0])
for n in range(a) : 
    print(aaa[0][n], end="\t")
print()

a=len(aaa[1])
for n in range(a) : 
    print(aaa[1][n], end="\t")
print()

a=len(aaa[2])
for n in range(a) : 
    print(aaa[2][n], end="\t")


print()
print()
print()

# 각 줄을 출력하는 3개의 덩어리를 반복문으로 줄이기
for k in range(len(aaa)):
    a=len(aaa[k])
    for n in range(a) : 
        print(aaa[k][n], end="\t")
    print()

print()

#[row : 행(줄), column:열(칸)]
for row in aaa:
    for col in row:
        print(col,end="\t")
    print()
print()
print()
#-------------------------------------------------------------

# 리스트를 사용하여 여러 데이터를 다루는 예제. 2개.
# 예제1) 학생 성적들의 총 합과 평균

score_list = [80,75,64,90,50]
total = 0
for score in score_list:
    total = total + score
print('총합 : ',total)
print('평균 : ',total/len(score_list))

#예2) 일주일의 온도 중에서 가장 더운날의 온도와 요일
#(데이터의 순서 : 월,화,수,목,금,토,일)

week_temparature= [15,8,16,9,7,6,10]
heighest = week_temparature[0] # 일단 제일 높은게 얘로 치고, 계속 큰놈 만나면 바꾸기
for temp in week_temparature:
    if heighest<temp: heighest=temp

print('최고온도 : ', heighest)

idx=week_temparature.index(heighest)
print(idx)

if idx==0:
    print('월요일')
elif idx==1:
    print('화요일')
elif idx==2:
    print('수요일')
elif idx==3:
    print('목요일')
elif idx==4:
    print('금요일')
elif idx==5:
    print('토요일')
elif idx==6:
    print('일요일')

#-----------------------------------
week=['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
print(week[idx])


















