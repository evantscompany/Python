with open('files/scores.csv', 'r', encoding='utf-8') as file:
    lines = file.read().split('\n')
    

#헤더 분리
header = lines[0].split(',') # 이름, 국어, 영어, 수학

data_line=lines[1:]

#2. 데이터 처리 : 과목별 점수 리스트 초기화
kor_scores = []
eng_scores = []
math_scores = []


#3 학생별 총점/평균 저장할 리스트 생성
student_results=[]

for line in data_line:
    if line.strip() == "":
        continue # 빈 줄 건너띄기
    parts = line.split(',')
    name = parts[0]
    kor,eng,math = parts[1],parts[2],parts[3]

    if not (kor.isdigit() and eng.isdigit()and math.isdigit()):
        continue

    kor=int(kor)
    eng=int(eng)
    math=int(math)

    kor_scores.append(kor)
    eng_scores.append(eng)
    math_scores.append(math)

    total=kor+eng+math
    avg=total/3
    student_results.append([name,total,round(avg,2)])

def print_stats(subject, scores):
    avg = sum(scores)/len(scores)
    maximum=max(scores)
    minimum=min(scores)
    print(f"{subject} - 평균 : {avg:.2f}, 최고점 : {maximum}, 최저점: {minimum}")

print("[과목별 통계]")
print_stats("국어", kor_scores)
print_stats("영어", eng_scores)
print_stats("수학", math_scores)

