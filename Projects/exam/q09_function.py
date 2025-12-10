with open("files/scores.csv",'r',encoding="utf-8")as file:
    source=file.read().strip().split("\n") 
    name_list = []
    kor_list = []
    eng_list = []
    math_list= []
    for line in source[1:]:
        (name,kor,eng,math)=line.split(",")
        name_list.append(name)
        kor_list.append(int(kor))
        eng_list.append(int(eng))
        math_list.append(int(math))
def calculate(subject_name,subject_list ):
    avg = sum(subject_list)/len(subject_list)
    subject_max = max(subject_list)
    subject_min = min(subject_list)
    print (f"{subject_name} --- [평균 : {avg}] , [최고점 : {subject_max}] , [최저점 : {subject_min}] ")
calculate('국어',kor_list)
calculate('영어',eng_list)
calculate('수학',math_list)

