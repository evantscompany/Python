#1번 문제
# 다음과 같은 형태로 본인의 이름을 출력하는 프로그램 작성
# 홍길동
# 홍 길 동
# 홍    길    동

print("홍길동")
print("홍 길 동")
print("홍   길   동")

print()
#2번 문제
#print()기능을 한번만 사용하여 문제 1과 같은 결과를 출력하도록 하자

print("홍길동\n홍 길 동\n홍   길   동")

#문제3
#본인의 [이름, 나이, 주소]를 다음의 출력형태로 보이도록 코드를 작성
#단 위 3개의 데이터를 print()의 여러개 데이터 출력방식으로 만들어보자
print()
print("제 이름은 홍길동 입니다\n제 나이는 20살이구요\n제가 사는 곳은 seoul 입니다")
print()
#문제4. 문제3의 이름,나이,주소 출력을 "format()" 출력 기능을 사용하여 출력
# - f" 포멧 출력 기능을 사용하여 출력해보자
print("제 이름은 {} 입니다\n제 나이는 {} 이구요, \n제가 사는 곳은 {} 입니다".format("홍길동",20,"seoul"))
print()
print(f"제 이름은 {"홍길동"} 입니다\n제 나이는 {20} 이구요, \n제가 사는 곳은 {"seoul"} 입니다")
print()

#문제 5. 다음의 출력 결과를 보이도록 예제 작성

print(f"{4}+{5}={4+5}")
print(f"{7}x{9}={7*9}")
print()

#문제 6. 문제 5번의 방식을 이용해서 구구단 5단을 출력해보자
print(f"{5}x{1}={5*1}")
print(f"{5}x{2}={5*2}")
print(f"{5}x{3}={5*3}")
print(f"{5}x{4}={5*4}")
print(f"{5}x{5}={5*5}")
print(f"{5}x{6}={5*6}")
print(f"{5}x{7}={5*7}")
print(f"{5}x{8}={5*8}")
print(f"{5}x{9}={5*9}")
print()
#문제 7 문제 6의 구구단 출력을 format 기능을 사용하여 출력해보자

print("{}x{}={}".format(5,1,5*1))
print("{}x{}={}".format(5,2,5*2))
print("{}x{}={}".format(5,3,5*3))
print("{}x{}={}".format(5,4,5*4))
print("{}x{}={}".format(5,5,5*5))
print("{}x{}={}".format(5,6,5*6))
print("{}x{}={}".format(5,7,5*7))
print("{}x{}={}".format(5,8,5*8))
print("{}x{}={}".format(5,9,5*9))

#문제 8 다음의 모양을 출력해보자

print('''
      *
     ***
    *****
   *******''' )

print()

#문제 9. 아래의 모습으로 데이터가 출력되도록 하자
print("-"*37)
print("번호\t이름\t나이\t전공\t주소")
print("-"*37)
print("1\tsam\t20\tweb\tseoul")
print("2\trobin\t25\tai\tbusan")
print("3\tpark\t30\tdata\tincheon")
print()

print("-"*37)
print(f"{"번호"}\t{"이름"}\t{"나이"}\t{"전공"}\t{"주소"}")
print("-"*37)
print(f"{1}\t{'sam'}\t{20}\t{'web'}\t{'seoul'}")
print(f"{2}\t{'robin'}\t{25}\t{'ai'}\t{'busan'}")
print(f"{3}\t{'park'}\t{30}\t{'data'}\t{'incheon'}")
print()



#문제 10. 아래의 긴 글을 여러줄 문자열로 출력하시오
print('''
파이썬은
      
웹 애플리케이션, 데이터 과학, 인공지능 등

다양한 분야에 사용되는 배우기 쉽고 효율적인

프로그래밍 언어입니다
      ''')






