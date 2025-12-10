# # 기타 제어문 break , continue : 반복문을 제어하는 추가제어문법

# for n in range(1,11):
#     if n==5:
#         break
#     print('n:',n)
#     print()

for n in range(1,11):
    if n==5:
        continue
    print('n:',n)
print()

# 무한 루프 - 반복을 하되.. 특정 조건이 되면 반복을 종료

num = 0
while(True):
    print('aa') 
    num+=1
    if num==10:
        break


print('aa')

#응용하면.. 특정 입력값이 들어올때까지 입력을 계속 받아라..

while(True):
    word=input('>>')
    if word=='exit' :
        break
    print(word)

# while, for 중 어느것을 사용해서 반복 논리를 만들것인가?
# 1. while : 반복횟수가 명확하지 않을때 .. 특정 조건이 될때 까지 반복할때 사용
# 2. for : 몇 번 반복할지 예측이 명확할때.