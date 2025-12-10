# 2. 반복문 : while,for 

#1) while
# a=0
# while(a<5):
#     print('aaa')
#     #조건에 사용한 변수(제어변수)의 값을 변경해보기
#     a=a+1

# print(a)

# print()

# 특정 조건에 도달할때까지 반복수행해야 할때.. 많이 사용함.
# ex) 게임할때.. level 1이 있는데 10이 넘어야 사냥을 갈 수 있다고 할때. 
# 레벨을 높이기 위해 훈련을 해야함.. 한번 훈련할 때마다 1씩 레벨이 업되는.

# print("END")

# count = 0

# while True :
#     print(f"현재 박복 횟수 : {count+1}")
#     count +=1

#     if count ==5:
#         break
# print("반복문 종료")


# dan = int(input(" 구구단 단수 입력 >>"))

# count = 0
# while count<10:
#     print(f'{dan}x{count+1}={dan*(count+1)}')
#     count+=1

# print("구구단 완료")    

#while 문을 이용한 반복의 횟수는 하나의 코드만으로 결정되지 않음.
# 1) 제어변수 초기값, 2) 제어조건, 3) 제어변수 연산.. 을 모두 고려하여 결정하게 됨.

# "Hello" 라는 글씨를 화면에 5번 출력하는 프로그램을 만들어 보세요 .

# count=0
# while count<5:
#     print("hello")
#     count+=1
# print("End ")    

# 만약 판단이 안서면.. 초기값 0, 조건은 <횟수. 연산은 +=1

#예) 사용자로부터 정수를 5번 입력받으면서 짝/홀 인지 출력해주는 프로그램


# a=0
# while(a<5):
#     num=int(input("숫자 입력 : "))
#     if num%2==0:
#         print("짝수")
#     else:
#         print("홀수")
#     a+=1


# total = 0

# a=0
# while(a<5):
#     num=int(input('숫자 입력'))
#     total+=num
#     a+=1
# print(total)

#누적합의 구하는 방법을 문자열에 적용하면.. 문자열을 결합하여 새로운 긴 문자열을 만드는 방법으로 활용가능

# ss=""
# ss=ss+"aaa" #"aaa"
# ss=ss+"bbb" #"aaa,bbb"
# ss=ss+"ccc" #"aaa,bbb,ccc"
# print(ss)

#반복에 사용했던 제어변수를 출력할 수도 있음.

dan = 4
n=1
while n<10:
    print(dan,n)
    n+=1

# 조건식에 사용하는 값을 변수가 가진 값으로 지정하는 것도 가능.
num=6
num=int(input())
a=0
while a<3:
    print('nice')
    a+=1
#사용자가 입력한 숫자만큼 반복횟수 정하는것도 가능

# ()는 while 문에서도 생략 가능






























