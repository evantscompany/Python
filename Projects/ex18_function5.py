# 파이썬의 표준(내장)함수 중 활용이 많은 15개 정도 소개. 


#1. print() : 데이터를 화면에 출력
#2. input() : 키보드로부터 문자열로 데이터를 입력
#3. type () : 데이터 또는 변수의 타입을 리턴. 

#4.len() : 문자열이나 리스트 등의 길이를 알려주는 함수. 
message = 'hello python'
print(len(message)) 

#5. sum() : 반복 가능한 데이터의 모든 요소 합을 리턴
#6. min(), max() : 최소값, 최대값

#7. abs() : 절대값 함수. 
num = 100
print(abs (num))

#8. range() 지정된 범위의 숫자 시퀀스를 만들어줌. 
aa= range(5)
print(aa)

#9. list() : 다른형태의 iterable(반복할 수 있는) 객체들을 모두 list 타입으로 변환하거나  빈 리스트 생성도 가능

aa= []
print(aa)

bb= list()
print(bb)

cc=list({'name':'s','age':'20'})
print(cc) #key 값 만으로 리스트 생성. 

#[별외] 문자열의 연산자 +,* --> 리스트도 있음. 
ee = [10,20,30] +[4,5,6]
print(ee)

ee=[10]*5 # 요소값 10을 5개...
print(ee)

ee=[100,200,300]*4
print(ee)


#10. map() : 반복 가능한 객체의 각 요소에 특정 함수를 적용한 결과 리스트를 리턴.
aaa = [10,20,30]
bbb = map(lambda n:n*2,aaa) # 반복문을 쓰지 않아도 각 요소별로 만들어줌
print(bbb)
print(list(bbb))

#11. filter() : 반복 가능한 객체의 각 요소에 특정 함수의 조건값이 True 인 결과 요소만 뽑아서 리스트를 리턴
aaa= [10,5,4,8,60,85,90]
bbb= filter(lambda n:n>=60,aaa)
print(bbb)
print(list(bbb))

#12. sorted() : 반복 가능한 객체의 정렬된 새로운 리스트를 반환
aaa=[40,23,78,5,64,1600,3,4,5,1,6,1,2,3,5,5,1,23]
bbb=sorted(aaa)
print(bbb)
ccc=sorted(aaa,reverse=True)

print(list(ccc))

#13. enumerate () : 순서가 있는 자료(리스트,튜플)의 인덱스 값을 포함하는 (튜플)index,value로 리턴해주는 기능 
aaa= [10,20,30]
for v in aaa:
    print(v)

print()

for t in enumerate(aaa):
    print(t[0],t[1]) # index,value

#14. zip() : 여러 리스트의 요소들을 병렬로 묶어서 튜플의 반복자를 만들어냄.
name_list=['sam','robin','hong','park']
age = [20,23,28,15]

people=zip(name_list,age)
print(list(people))

#튜플데이터를 사전(dict)타입으로 바꿀 수 있음.

vvv=dict(people)


#15. any(), all()
# any : 요소 중에 하나라도 조건에 맞으면 True
limit = 3
ccc=[1,3,6,5]
#요소들 중에 하나라도 limit 보다 작은 값이 있는 가? [예)소요시간이 기준시간보다 짧게 걸린 데이터가 있는가?]
print(any(n<limit for n in ccc ))

#all :  모든요소가 조건에 맞아야 True
print(all(n<limit for n in ccc ))


#16. 형변환 연산자, int , float, str, bool, list, set ,tuple,

#---------------------------------------------------------------------------

#[완전 별외 수업...] 기초타입의 변수와 참조타입 변수의 차이 그리고 조심할점

# 파이썬의 타입 2종류
# 1. 기초타입 : int, float, str,bool                                    [데이터를 저장하는 변수]
# 2. 참조타입 : 기초 제외한 모두가 참조 타입. list,tuple,dict,set,object    [객체의 주소를 저장하는 변수]

# 기초타입 .. 상황
a=10
b=a
print('a: ',a)
print('b: ',b)
print()

b=50
print('a: ',a)
print('b: ',b)
print()

# 참조타입 .. 상황

aaa= [100,200,300]
bbb=aaa

print(aaa)
print(bbb)

bbb[1] = 5000

print(aaa)
print(bbb)
