with open("files/scores.csv",'r',encoding='utf-8') as f:
    rows=[l.split(',') for l in f.read().strip().split('\n')[1:]]
    subject = {"국어" : [],"영어" : [], "수학" : []}
    for name,kor,eng,math in rows:
        subject['국어'].append(int(kor))
        subject['영어'].append(int(eng))
        subject['수학'].append(int(math))
        print(subject)
    for s, lst in subject.items():
        print(f"{s} ---[평균 : {sum(lst)/len(lst)}], [최고점 : {max(lst)}], [최저점 : {min(lst)}]")
