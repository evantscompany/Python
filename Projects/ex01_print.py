100
#이렇게 그냥 값만 쓰면 그 값이 자동으로 출력되지 않음.shell 환경에서는 출력됨.

#1. 파이썬의 기본적인 출력기능 print(Data)

# 프로그램은 데이터를 다루는 것임.
# 1)사용자이름, 리뷰글, 게시판 제목 --- 문자열
# 2)나이, 성적, 상품가격 등 ---------- 숫자
# 3)로그인 여부, 미성년자 여부 등 ----- 논리값


# 각각의 데이터 유형 (자료형 data type)을 출력해보기.


print(100)
print(3.14)
#print(Hello) --- 에러.. why? 문자열 Data는 반드시 따옴표와 함께 써야 함.
print("Hello")
#문자열을 쓸 때 작은 따옴표로 감싸도 됨.
print('hello')
#논리값을 출력해보기

print(True,False)
print('True')

print(3<5) 
print(3>5)
print(        200     )
print(       '         good        ')    

print()  #print()만 쓰면 한줄 건너띄기
print("aaa")

#Data를 써야 하는 자리에.. 연산식(계산식)을 쓰면 식이 출려되는 것이 아니라, 결과 값이 출력됨
print(3+5)
print("3+5")


#문자열 안에 특수문자도 사용가능함. 단, 사용 못하는 것이 2개.. [큰따옴표],[역슬래시\]
print("")

#큰따옴표가 나오게 하려면.. 작은 따옴표의 문자열로 만들면 됨.
print("'hello'")
print('"나는 홍길동" 입니다')

#만약, 한 문장안에 큰 따옴표와 작은 따옴표를 같이 사용하고 싶다면..
print("나는 \"홍길동\" 입니다")

print("hello w" \
"world")

#이스케이프 문자의 사용법. 줄바꿈을 해주는 특수문자.
# \n [new line]
print("hello \nworld")
print("hello\nnice\ngood")

#\t [tab]

print("hello\tnice")

#여러개의 Data를 출력하는 것이 가능함
print(10,20)
print(3,"+",5,"=",3+5)