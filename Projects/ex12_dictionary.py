




























ccc={'name':'robin', 'age':25,'address':'busan'}
if 'name' in ccc:  #name 이라는 식별자가 존재하는가?
    print('name :', ccc['name'])

#만약 존재하지 않는 식별자를 사용하면.. 에러
#print( ccc['tel']) # error

#에러가 걱정이라면. in 연산자로 검사해야하지만 이것도 번거로움
# 그래서 특정 식별자의 값을 []로 접근하지 않고.. 값을 얻어주는 
value=ccc.get('address')
print(value)

value=ccc.get('tel') # 없는 key 를 사용하면 None 값을 줌.
print(value)
print()

#반복문 딕셔너리의 요소값을 접근해보기.
# range()는 불가능.. 인덱스 번호가 없고 name이기때문.

for a in ccc: #요소 값이 아니라 식별자 key가 뽑아짐.
    print(a)

#딕셔너리는 다른 리스트, 튜플과 다르게 요소값이 for 로 뽑아지지 않고, key가 뽑아짐.
#요소값을 알고 싶다면.. 뽑아진 key 를 이용하여 값을 취득
print()
for key in ccc:
    print(ccc[key])
    print()
    print(ccc[key])


#딕셔너리의 (key,value) 튜플 쌍을 가지고 있는 Item 이라는 녀석으로 for을 사용하기.

items=ccc.items()
print(items)
print(len(items))


print()
print()

for item in ccc.items():
    print(item)
    key,value = item
    print(key)
print()

for key,value in ccc.items():
    print(key,value)
print()

