# 연산자 : 산술, 비교, 논리, 비트, 복합대입, 형변환

#1. 산술
a=10
b=4

print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(a%b) # 나머지 연산자
print(a//b) # 몫

#no=int(input('수험번호 입력 : '))

# 홀수 짝수 찾기

# if no%2==1:
#     print('홀수')
# else:
#     print('짝수')

# 그 숫자의 1의 자리 값을 뽑아오기.
#n_1=no%10
#print(n_1) #1의 자리 값을 나누기로 빼올 수 있음.
#n_100=n//100
#print(n_100) # 100의 자리 숫자 빼오기

#. 나눗셈의 몫, 나머지 값을 한번에 연산하여 결과를 주는 기능함수를 제공함.divmod()
x,y = divmod(a,b)
print('몫 : ' , x)
print('나머지 : ', y)

# 부호 변경 연산자 - [단항 연산자]
c=10
print(-c)
c=-10
print(-c)

#제곱연산 연산자  **
a=3
print(a**2) #3의 제곱
print(a**3) #3의 세제곱
print(a**(1/2)) #3의 제곱근 [루트 구하기]
print()

#2. 비교연산자
a=10
b=4

print(a>b) #True
print(b>a) #False
print(a>=b)
print(b>=a)
print(a==b)
print(a!=b)

# a 변수가 특정 범위 안에 있는지 여부
# a가 0~100 사이의 숫자인가
a=150
print(0<a<100)
# 나이가 20대 인가요?
age = 25
print(20<=age<30)


#3. 논리연산자 : and, or, not

#하나의 변수에 대한 범위조건이 아니라, 2개 변수의 조건을 동시에 체크하는 경우도 많음.
#[예] (놀이기구 탈때) 나이가 10살 이상 키가 150 이상인 경우

age = 15
height = 160
print(age>=15 and height>=150) # 두 비교 연산의 결과가 모두 true 인 경우만 true가 되는 논리연산

#나이가 10살 이하이거나, 키가 150보다 작다면
print(age<15 or height<150) # 두 비교연산의 결과 중 하나라도 true 면 true결과를 주는 논리연산

#미성년자가 아니면.. 이라는 조건..
age = 25
#print(age>=20)
print(not age<20)

#비트 연산자 (거의 사용 안함. 한번만 살펴보기) 
# 연산에 사용된 피연사들을 2진수로 바꾸어 각 비트 자리끼리 연산 수행
print(7&4) # and 비트연산
print(7|4) # or 비트연산
print(7^4) # exclusive or 비트연산
print(8>>2) #shift 연산 .. 비트를 오른쪽으로 2칸 밀기
print(8<<2) 
print( ~10) # 0->1,1->0 (숫자의 부호도 바뀌어버림)

#5. 복합대입 연산자 (산술 + 대입)
a=20

#a변수가 가진 값을 1 증가시켜보세요
a+=1
print('a: ', a)

a+=2
print('a: ', a)

#만약 변수 이름이 길면...
character_age=20
print("age :", character_age)

character_age=character_age+1
print("age: " , character_age)

#변수명을 2번씩 쓰는게 은근 짜증..
character_age+=1
print("age: " , character_age)

character_age+=5
print("age: " , character_age)

character_age-=3
print("age: " , character_age)

character_age*=10
print("age: " , character_age)

character_age/=2
print("age: " , character_age)

character_age%=2
print("age: " , character_age)


character_age+=1
print("age: " , character_age)
print()


#6. 형변환 연산자
a='10'
print(type(a))
#print(a+3)#error : str + int 이기 때문.
#'10' -> 10 변환하기
a= int(a)
print(type(a))

a='3.14'
print(float(a)+5.12)

#str()형변환 가능 -- 문자열로 변환
print(5+3) #숫자 +숫자 는 산술 더하기
print(str(5)+str(3))

# bool() :  단순히 "true" 문자열을 true 논리값으로 변환하는 것은 아님.
# 파이썬은 값이 없는 것(0, "", [], None,False) 을 제외하고 모두 참(True)

a='True'
print(type(a))

a=bool(a)
print(type(a))

a=10
print(bool(a)) #True

a=0
print(bool(a)) #False

a= "Hello"
print(bool(a))

a= ""
print(bool(a))

a= "  "
print(bool(a))

# 나중에 조건문 if 문법을 사용할때 조건에 대해 확인할때 위의 개념을 사용함.
#예) 엑셀파일을 읽어들여서.. 그 데이터를 출력할때..
# df=pandas.read_exel(aaa.xls)

# if table :
#     print("테이블 값 출력")
# else:
#     print("테이블에 데이터가 없어요")

# 일반 산수에도 연산자 우선순위가 있듯이.. 파이썬에도 존재함.
print(3+5*6)

# 사실.. 아래 코드도 연산자 우선순위와 관련있는 내용.
num=3+6
print("========================================")
print()

# 프로그램에서 사용하는 대부분의 데이털는 문자열이 많음 [이름,제목, 리뷰, 메모, 아이디 등]
# 문자열 데이터를 다루기 위한 연산자와 기능함수들 소개.

# 1) 문자열 연산자 3개 (+,*,[])

#1] + 결합 연산자
print( 'aa' + 'bb')
#2] * 반복연산자
print( 'aa'*3) # aa 를 3번 반복하여 문자열 생성
s="Good" *5 # ==>"GoodGoodGoodGoodGood"
print(s)
#3] []문자열에 인덱싱 .. 슬라이싱
s="Hello world"
print(s)
# 문자열(문자가 여러개인 것..)의 특정 위치 글자를 뽑아올 수 있음.
print(s[1]) # 인덱스 번호가 1번인 위치의 값 0포함으로 시작임.
print(s[1:7]) # 1번부터 ~ 7번 전까지 [1~6]의 글씨를 뽑아오기
print(s[1:]) # 1번부터 ~ 끝까지
print(s[:7]) #처음부터 7번 전까지[0~6]
print(s[-1]) #뒤에서 첫번째 요소의 글씨..
print(s[-5]) #뒤에서 다섯번째 요소의 글씨..
print(s[-5:]) #뒤에서 5번째 요소의 글씨부터 끝까지
print()




# 2) 문자열이 가진 유용한 기능함수들()

#1] len() -> 문자열의 길이(글자수)를 알려주는 내장함수 len() : length
s="hello world"
print(len(s))

#2] '문자열데이터'.format()기능  -- 특정서식모양을 만들어 사용하는 기능
money=500
print(money,"만원")
print('{}만원'.format(money))
name = 'sam'
age = 20
print('이름 : {}   나이={}'.format(name,age))
aaa="{}님 반가워요".format(name)
print('만들어진 문자열 : ' , aaa)
print('글자 수는 : ',len(aaa))

#format()의 {}에 들어갈 데이터의 종류를 미리 고정할 수 있음. 코드 실수 방지!
#print("{:d}    {:d}".format(10,20)) #d (d: decimal -> 10진수) 10진수 숫자만 쓰게 할때.
print('실수 : {:f}'.format(3)) #실수형만 넣을수 있음.
print("문자열 : {:s}".format("nice")) #문자만 오게 할때


# 데이터를 출력할 때 표시되는 칸 수를 지정할 수 있음.
hour = 13
min=24
sec=30
print("{:02d}:{:02d}:{:02d}".format(hour,min,sec))
hour = 1
min=2
sec=3
print("{:02d}:{:02d}:{:02d}".format(hour,min,sec))

#정수일때.. 칸수 지정
print("[{}]".format(100))
print("[{:5d}]".format(100))
print("[{:05d}]".format(100))
print("[{:15d}]".format(100))

#부호가 표시되었으면 좋겠다면.
print("[{:+d}]".format(30))
print("[{:+d}]".format(-30))

#부호가 표시되는 영역을 비워놓고 싶다면.
print("[{: d}]".format(30))
print("[{: d}]".format(-30))

#부호를 칸의 왼쪽 끝으로 배치하기
print("[{:=+8d}]".format(30))
print("[{:=+8d}]".format(-30))



#실수일때.. 칸수 지정
print('[{}]'.format(3.14))
print('[{:f}]'.format(3.14)) # float 을 쓰면 무조건 소수점 아래 6자리까지 출력됨.
print('[{:10f}]'.format(3.14)) # float 을 쓰면 무조건 소수점 아래 6자리까지 출력됨.

#소수점 아래의 칸수를 지정
print('[{:10.2f}]'.format(3.14)) # float 을 쓰면 무조건 소수점 아래 6자리까지 출력됨.
print('[{:.2f}]'.format(3.14)) #데이터 갯수만큼만 나오되, 소수점 2자리까지만 출려됨

#정수를 소수점으로 표시하기
print("{:.1f}".format(100))

#소수점이 필요하면 찍고, 아니면 찍지 않았으면 좋겠다면(정수인지 실수인지 모를때)
print("{:g}".format(100))
print("{:g}".format(3.14))



#문자열일때.. 칸수 지정
print("이것은 [{}]입니다".format('aaa'))
print("이것은 [{:s}]입니다".format('aaa'))
print("이것은 [{:10s}]입니다".format('aaa'))

#남은 공간의 오른쪽으로 배치
print("이것은 [{:>10s}]입니다".format('aaa'))

#진법 표시
print("{:d}".format(10)) #10진수 - decimal
print("{:o}".format(10)) #8진수 - octal
print("{:x}".format(10)) #16진수 - hexadecimal
print("{:b}".format(10)) #2진수 - binary

#파이썬 코드로 2진수, 8진수, 16진수를 표기해보기.
print("{:d}".format(0o10)) #8진수 표기법
print("{:d}".format(0x10)) #16진수 표기법
print("{:d}".format(0b10)) #2진수 표기법








