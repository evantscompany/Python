# 문제 2.
# 사용자로부터 정수형 숫자 하나를 입력받자. 이 입력된 숫자 만큼 사용자로 부터 문자열을 입력받아 리스트에 저장하도록 해보자.
# 입력된 문자열들이 잘 저장되어 있는지 확인하기 위해 배열의 각 요소들을 for in 반복문으로 차례로 출력해보자.


num= int(input('몇 개의 문자열을 입력받으시겠습니까? '))

data=[]
for n in range(num):
    s= input('문자열 입력 : ')
    data.append(s)

print()

for s in data:
    print(s)
