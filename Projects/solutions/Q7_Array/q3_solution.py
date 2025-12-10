# 문제 3.
# 아래와 같이 학생들의 성적을 받아서 score_list 라는 이름의 리스트에 저장하고, 평균을 구하는 프로그램을 작성해보자. 평균은 소수점 2자리까지만 표시
# 단, 입력값이 0~100 사이가 아니면 다시입력하도록 하시오. 


# 실행결과 예시)

#  학생의 수를 입력하시오 : 2

#  학생 1의 성적을 입력하세요 : 20
#  학생 2의 성적을 입력하세요 : 110
#  잘못된 성적입니다. 다시 입력하시오.
#  학생 2의 성적을 입력하세요 : 30
 
#  —--------------------
#  학생 1의 성적 : 20
#  학생 2의 성적 : 30
#  —--------------------
#  성적 평균은 25.0 입니다.


score_list=[]

num= int(input('학생의 수를 입력하시오 : '))

n=0
while n<num:
    score= int(input(f"학생 {n+1}의 성적 : "))
    if(score<0 or score>100): 
        print('잘못된 성적입니다. 다시 입력하시오.')
        continue

    score_list.append(score)       
    n+=1

print()
print('-'*30)

for idx, score in enumerate(score_list):
    print(f'학생 {idx+1}의 성적 : {score}')

print('-'*30)

total= sum(score_list)
print('성적 평균은 {:.2f} 입니다.'.format(total/num))
