# 문제 10.
# 어느 교육원의 Python Programming 성적을 저장하는 프로그램을 만들어보다.
# 교육원의 Python Programming은 3개 반으로 운영되고 있다. 단, 각 반의 인원수는 서로 다를 수 있다.
# 프로그램 사용자가 3개반의 성적을 입력하기 전에 해당 반의 인원수를 입력할 수 있도록 하고 그 인원수 만큼 성적을 넣으면 다음 반의 인원수를 입력하는 방식으로 3개반의 모든 성적을 입력해보자. 
# 모든 성적 입력이 끝났으면 그 값들을 출력해보고 각 반의 평균도 같이 계산되도록 해보자.

# 실행 예)

#  [1반] 인원 수 입력 : 3
#  [1반 1번] : 80
#  [1반 2번] : 70
#  [1반 3번] : 60
 
#  [2반] 인원 수 입력 : 4
#  [2반 1번] : 90
#  [2반 2번] : 80
#  [2반 3번] : 80
#  [2반 4번] : 60

#  [3반] 인원 수 입력 : 5
#  [3반 1번] : 90
#  [3반 2번] : 80
#  [3반 3번] : 70
#  [3반 4번] : 40
#  [3반 5번] : 60

#  --- Python Programming 성적표 ----
#  [1반]  80  70  60   [평균 : 70.0]            
#  [2반]  90  80  80  60   [평균 : 77.5]
#  [3반]  90  80  70  40  60  [평균 : 68.0]
#  -----------------------
#  전체평균 :  71.67
#  최우수 반 : [2반]


python_class=[[],[],[]] #3개의 빈 리스트를 요소로 가지는 2차원 배열

for idx, c in enumerate(python_class):
    
    num= int(input('['+str(idx+1)+'반] 인원 수 입력 : '))    
    for n in range(1, num+1):
        score= int(input('['+str(idx+1)+'반 '+str(n)+'번] :'))
        c.append(score)
    print()

print()

print('----------------- Python Programming 성적표 --------------------')
for idx, c in enumerate(python_class):
    
    print(f'[{idx+1}반]', end='\t')
    
    for score in c:
        print(score, end='\t')
    
    print('[평균 : {:.1f}]'.format( sum(c)/len(c) ))
print('---------------------------------------------------------------')

averages= [ sum(c)/len(c) for c in python_class ]
total_average= sum(averages)/3
print('전체평균 : {:.1f}'.format(total_average))

best_average= max(averages)
best_class_index= averages.index(best_average)
print('최우수반: {}반'.format(best_class_index+1) )






