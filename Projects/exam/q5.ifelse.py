# # import datetime

# # greet= input("입력하세요>> ")
# # greet= greet.replace(" ","")
# # greet= greet.replace("\n","")

# # now= datetime.datetime.now()
# # if "안녕" in greet:
# #     print("안녕하세요")

# # elif "몇시" in greet:
# #     print(f"지금은 {now.hour}시{now.minute}분{now.second}초입니다.")
# # else:
# #     print(greet)


# num=int(input("정수를 입력하세요 >>"))

# if num%2==0:
#     print(f"{num}은 2로 나누어 떨어지는 숫자입니다.")
#     print(f"{num}은 3으로 나누어 떨어지는 숫자가 아닙니다.")
#     print(f"{num}은 4으로 나누어 떨어지는 숫자가 아닙니다.")
#     print(f"{num}은 5으로 나누어 떨어지는 숫자가 아닙니다.")

# elif num%3==0:    
#     print(f"{num}은 3로 나누어 떨어지는 숫자입니다.")
#     print(f"{num}은 2로 나누어 떨어지는 숫자가 아닙니다.")
#     print(f"{num}은 4으로 나누어 떨어지는 숫자가 아닙니다.")
#     print(f"{num}은 5으로 나누어 떨어지는 숫자가 아닙니다.")

# elif num%4==0:    
#     print(f"{num}은 4로 나누어 떨어지는 숫자입니다.")
#     print(f"{num}은 2로 나누어 떨어지는 숫자가 아닙니다.")
#     print(f"{num}은 3으로 나누어 떨어지는 숫자가 아닙니다.")
#     print(f"{num}은 5으로 나누어 떨어지는 숫자가 아닙니다.")

# elif num%5==0:    
#     print(f"{num}은 5로 나누어 떨어지는 숫자입니다.")
#     print(f"{num}은 2로 나누어 떨어지는 숫자가 아닙니다.")
#     print(f"{num}은 3으로 나누어 떨어지는 숫자가 아닙니다.")
#     print(f"{num}은 4으로 나누어 떨어지는 숫자가 아닙니다.")
    

# else:
#     print("정수를 입력하세요")

#1. 사용자로부터 정수 하나 입력 받은 후 입력받은 정수의 절대값 출력 프로그램
# num= float(input("아무 정수나 입력하세요 >>"))

# if int(num<0):
#     print(f"{num}의 절대값은 {num*-1}입니다. ")
# elif int (num >0):
#     print(f"{num}의 절대값은 {num}입니다. ")    
# elif num == 0:
#     print(f"입력하신 값은 {num}입니다. ")
# else:
#     print("정수를 입력하세요")
    


# num1=int(input("첫번째 정수 입력 >>"))
# num2=int(input("두번째 정수 입력 >>"))

# if num1<num2:
#     print(f"더 큰 값은{num2}입니다." )
# elif num1>num2:
#     print(f"더 큰 값은 {num1}입니다" )
# elif num1==num2:
#     print(f"두 값은 {num1}으로 같습니다")        

# a=int(input("첫번째 정수 a : "))
# b=int(input("두번째 정수 b : "))
# c=int(input("세번째 정수 c : "))


# if a>b and a>c :
#     max=a
#     print(f"셋중 가장 큰 값은 a = {max}입니다. ")
# elif b>a and b>c:
#     max=b
#     print(f"셋중 가장 큰 값은 b = {max}입니다. ")
# elif c>a and c>b:
#     max=c
#     print(f"셋중 가장 큰 값은 c = {max}입니다. ")


# num1=int(input("첫번째 정수를 입력하세요"))
# num2=int(input("두번째 정수를 입력하세요"))
# result = num1-num2

# if result<0:
#     print(result*-1)
# else:
#     print(result)    

# print(result*-1) if result<0 else print(result)

# saved_id="python"
# saved_pw="1234"

# log_id=input("아이디를 입력하세요")
# log_pw=input("비밀번호를 입력하세요")

# if saved_id==log_id and saved_pw==log_pw:
#     print("로그인 성공")
# elif not saved_id==log_id or not saved_pw==log_pw:
#     print("아이디 혹은 비밀번호가 틀렸습니다.") 


# num=int(input("하나의 정수를 입력하세요"))

# if 0<=num<50 :
#     print("낮음")
# elif 50<=num<80 :
#     print("보통")   
# elif 80<=num<100 :
#     print("높음")
# else:
#     print("범위를 벗어남")

# sentence=input("error가 포함된 문장을 쓰면 'error'이라고 출력됩니다. 없으면 정상으로 출력됩니다>>")
# sentence_ch= sentence.lower().replace(" ","")
#
# if "error" in sentence_ch:
#    print(f"입력하신 문장은 {sentence}이며 그 안에 '오류'가 포함되어 있음")
# else :
#    print(f"입력하신 문장은 {sentence}이며 '정상' 입니다")    

#num1 = int(input("첫번째 정수 입력 : "))
#num2 = int(input("두번째 정수 입력 : "))
#num3 = int(input("세번째 정수 입력 : "))

#average= (num1+num2+num3)/3


#if num3<num1>num2:
#    result_max=num1
#    print(f"가장 큰 수는 {num1}입니다. ")
#elif num3<num2>num1:
#    print(f"가장 큰 수는 {num2}입니다. ")
#else :
#     print(f"가장 큰수는 {num3}입니다.")

# print(f"평균 값은 {average} 입니다.")

# if average>=70:
#     print("통과 입니다.")
# else:
#     print("불합격 입니다.")

# if (type(average))==float:
#     print("해당 평균값은 실수인 {:2f} 입니다.".format(average))
# else:
#     print(f"해당 평균값은 정수인 {average} 입니다.")


file=input("파일명을 확장자 포함하여 입력하시오>>")

if "2025"in file:
    print(end="올해 생성된 파일,")
else:
    print("")
if "report" in file:
    print(end="보고서 유형, ")   
else:
    print("")
if ".csv" in file:
    print(end="csv 데이터 파일")
else:
    print("") 

# visited = '오늘 방문자 수는 350명이었고, 어제는 280명이었다.'

# if "350" in visited and "280" in visited:
#     num1= int("350")
#     num2= int("280")
#     print("두 수의 차는= ", num1-num2)
#     if num1>num2:
#         print("증가")
#     else:
#         print("감소")



sentence = input("문장을 입력하세요")

length = print("긴문장") if len(sentence)>30 else ""
wonder = print("감탄사") if "?"in sentence else ""


    













