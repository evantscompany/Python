# # #변수 선언과 할당
# # pi = 3.14159265
# # r=10

# # #변수 참조

# # print("원주율 =", pi)
# # print("반지름 =", r)
# # print("원의 둘레 =", 2*pi*r) #원의 둘레
# # print("원의 넓이 =", pi*r*r) #원의 넓이
 
# # string_a = input("입력A>")
# # int_a= int(string_a)

# # string_b=input("입력B>")
# # int_b=int(string_b)

# # print("문자열 자료 :", string_a+string_b)
# # print("숫자자료 :", int_a+int_b)



# #--------------------------------------------------------------------------------

# #문제 1.  자기소개 출력하기.

# print("문제 1. print() 함수를 사용해 아래 내용을 출력해보세요")
# print()
# print("안녕하세요! 저는 [이름] 입니다.")
# print("좋아하는 음식은 [음식] 입니다.")
# print()
# print("-"*50)
# print()

# print("문제 2. 변수로 문장 만들기")

# print('이름,나이,취미를 \'변수\'로 저장한 후, print()로 다음과 같이 출력해보세요.')
# print()

# name = '홍길동'
# age = 25
# hobby = "수영,달리기"

# print("제 이름은",name,'이고', '나이는',age,"살 입니다" '\n'"제 취미는",hobby,"입니다." )
# print()
# print('-'*50)
# print()

# print('문제3. 자료형 확인하기'"\n""다음 변수를 만들고, 각각의 자료형을 출력해보세요.")
# print()

print('name = 철수'"\n"'age = 15'"\n"'height = 165.3'"\n"'is_student = True')
# print()

# name='철수'
# age=15
# height=165.3
# is_student = True

# print("각 데이터의 자료형은 다음과 같습니다")
# print(type(name))
# print(type(age))
# print(type(height))
# print(type(is_student))
# print()
# print("-"*50)
# print()

# # print('문제 4. 간단한 계산기 만들기'"\n"'두 숫자를 변수로 저장한 뒤, 덧셈,뺄셈,곱셈,나눗셈 결과를 각각 출력해보세요')
# # print()
# # num1=10
# # num2=3

# # print("덧셈결과 :",num1+num2 )
# # print("뺄셈결과 :",num1-num2 )
# # print("곱셈결과 :",num1*num2 )
# # print("나눗셈결과 :",float(num1)/float(num2) )
# # print()
# # print('-'*50)
# # print()

print("문제5. 변수 활용 문장 완성하기""\n""아래 변수를 이용해서 문장을 완성해보세요")
print("country = \"한국\""   '\n'  "city = \"서울\""   '\n'  "year = 2025")

country='한국'
city='서울'
year=2025

print(str(year)+"년에","저는",country+"에","살고있습니다.")
print()
print('-'*50)
print()

print('문제6. 프로그램 사용자로부터 두개의 정수를 입력 받아서 두수의 뺄셈과 곱셈의 결과를 출력하는 프로그램')

print()

num_1=input("첫번째 정수를 입력하세요 : ")
num_2=input("두번째 정수를 입력하세요 : ")
print("두수의 합은",f"{num_1}+{num_2}={int(num_1)+int(num_2)}")
print("두수의 차는",f"{num_1}-{num_2}={int(num_1)-int(num_2)}")
print()
print('-'*50)
print()

print('문제7. 프로그램 사용자로부터 세 개의 정수 num1,num2,num3을 순서대로 입력받은후에')
print('      다음 연산의 결과를 출력하는 프로그램(입력문은 세번 사용) \n      num1*num2+num3'"\n"
"      단, 입력받은 세개의 정수가 2,4,6 이라면 다음의 형태로 출력을 해야한다"     )

num1=int(input("첫번째 정수 입력"))
num2=int(input("두번째 정수 입력"))
num3=int(input("세번째 정수 입력"))

print(f"{num1}*{num2}+{num3}={num1*num2+num3}")

print("하나의 정수를 입력 받아, 그 수의 제곱의 결과를 출력하는 프로그램")

multi=int(input("정수를 입력하세요"))
print(f"{multi}의 제곱은 {multi*multi}")

print("두 개의 실수를 입력 받아서 2개의 변수 저장. 사칙 연산결과 출력")
print()
num1=float(input("첫번째 실수를 입력하세요"))
num2=float(input("두번째 실수를 입력하세요"))

print(f"덧셈 결과 : {num1}+{num2}={num1+num2}")
print(f"뺄셈 결과 : {num1}-{num2}={num1-num2}")
print(f"곱셈 결과 : {num1}x{num2}={num1*num2}")
print(f"나눗셈 결과 : {num1}/{num2}={num1/num2}")

print("문제10. 마일을 킬로미터로 변환하는 프로그램. 1마일 = 1.609킬로미터")

mile=float(input("마일을 입력하세요>>"))
print(f"{mile}마일은 {mile*1.609}km입니다")





