# tuple ()-- 리스트와 비슷한데, 요소의 값 변경/요소추가/요소삭제 모두 불가능 


bbb=(10,20,30)
print(bbb)
print(type(bbb))

#요소값 사용하는 방법은 같음 - 인덱스 번호
print(bbb[0])  #여기서의 []는 리스트를 말하는게 아니라, 해당 종류 배열의 위치번호. 즉 튜플 포함.
print(bbb[1])
print(bbb[2])


#값변경.. 요소추가 삭제 모두 불가능.
#bbb[0]= 100 error
#bbb.append(20) error
#bbb.remove() error

for value in bbb:
    print(value+1)
print()

# 특이하게 튜플 생성 방법. 권장은 아닌데, 은근 보임.
bbb=10,20,30 # 파이썬이 알아서 튜플로 만들어버림.
print(bbb)


#반대로 튜플의 요소값들을 여러개의 변수로 분리해서 대입하는 것이 가능.꽤 씀.
bbb=(10,20,30)
print(bbb[0])
print(bbb[1])
print(bbb[1])

a,b,c=bbb
print(a)
print(b)
print(c)




