# list_a = [1,2,3]
# list_b = [4,5,6]

# print('#리스트')
# print("list_a= ", list_a)
# print("list_b= ", list_b)
# print()

# print("#리스트 기본 연산자")
# print("list_a+list_b = ", list_a+list_b)
# print("list_a * 3=", list_a*3)
# print()

# print("#길이 구하기")
# print("len(list_a) = ", len(list_a))


# list_a=[1,2,3]

# print ('#리스트 뒤에 요소 추가하기')
# list_a.append(4)
# list_a.append(5)
# print(list_a)
# print()

# print('# 리스트 중간에 요소 추가하기')
# list_a.insert(0,10)
# print(list_a)

# list_a=[0,1,2,3,4,5]
# print("#리스트의 요소 하나 제거하기")

# del list_a[1]
# print("del list_a[1]: ", list_a)

# list_a.pop(2)
# print("pop(2): ", list_a)


# list_of_list = [ [1,2,3],[4,5,6,7,],[8,9]]

# for items in list_of_list:
#     for item in items:
#         print(items)

# numbers = [273,103,5,32,65,9,72,800,99]

# for number in numbers:
#     if number>=100:
#         print("- 100이상의 수 : ", number)

# for number in numbers:
#     if number%2==0:
#         print(f"{number}은 짝 수 입니다")
#     else:
#         print((f"{number}은 홀 수 입니다"))

# for number in numbers:
    
#     print(f"{number}은 {len(str(number))}의 자리 수 입니다")

numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for number in numbers:
    output[(number+2)%3].append(number)
    print(output)

print(output)