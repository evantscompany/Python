with open("files/scores.csv",encoding="utf-8") as f:
    d={"국어":[], "영어":[], "수학":[]}
    for _,a,b,c in (l.split(',') for l in f.read().splitlines()[1:]):
        for k,v in zip(d,(a,b,c)): d[k].append(int(v))
    for k,v in d.items():
        print(k, sum(v)/len(v), max(v), min(v))

        