# list_a=[1,2,3,4,5]
# list_reversed= reversed(list_a)

# print("# reversed() 함수")
# print('reversed([1,2,3,4,5]): ', list_reversed)
# print('list(reversed([1,2,3,4,5])): ', list(list_reversed))
# print()

# print('#reversed() 함수와 반복문')
# print('for i in reversed ([1,2,3,4,5]):')
# for i in reversed(list_a):
#     print("-", i)

# temp = reversed([1,2,3,4,5,6])

# for i in temp:
#     print("첫 번째 반복문 : {}".format(i))

# temp = reversed([1,2,3,4,5,6])

# for c in temp:
#     print("두 번째 반복문 : {}".format(c))

# example_list= ["요소A","요소B","요소C"]

# print("단순 출력 ")
# print(example_list)
# print()

# print('enumerate() 함수 적용 출력')
# print(enumerate(example_list))
# print()

# print('lst()함수로 강제 변환 출력')
# print(list(enumerate(example_list)))
# print()

# print("반복문과 조합")
# for i,value in enumerate(example_list):
#     print("{}번째 요소는 {}입니다".format(i,value))


# example_dictionary={
#     "키A": "값A",
#     "키B": "값B",
#     "키C": "값C",
# }

# print('딕셔너리의 items()함수')
# print('items():', example_dictionary.items() )
# print()

# print('딕셔너리의 items()함수와 반복분 조합하기')

# for key,element in example_dictionary.items():
#     print("dictionary[{}] = {}".format(key,element))


# array=[]

# for i in range(0,20,2):
#     array.append(i*i)
#     print(array)

# print(array)

# array= [ i*i for i in range(0,20,2)]
# print(array)

# array=["사과","자두","초콜릿","바나나","체리"]
# output = [fruit for fruit in array if fruit!="초콜릿"]
# print(output)


# number = int(input("정수입력 >>"))

# if number%2==0:
#     print('''\
#           입력한 문자열은 {}입니다. 
#           {}는 짝수 입니다'''.format(number,number))



# output= [n for n in range (1,100) if str("{:b}".format(n)).count("0")==1]

# for i in output:
    
#     print("{} : {}".format(i, "{:b}".format(i)))   
#     print("합계  : ", sum(output))



#----------------------------------------------------
# 다음 리스트에서 몇가지 종류의 숫자가 사용되었는지 구하는 프로그램 (page 268)

# array=[1,2,3,4,1,2,3,1,4,1,2,3]
# array_set=list(set(array))
# print(array_set)

# print(f"{array}에서 \n사용된 숫자의 종류는 {len(array_set)}개 입니다. \n참고 : 1:{array.count(1)}, 2:{array.count(2)}, 3:{array.count(3)}, 4:{array.count(4)}")

# dna= input("DNA 4가지 요소를 입력하세요 >>")
# for n in range(len(dna)):
#     adenin = dna.count("a")
#     timin = dna.count("t")
#     guanin = dna.count("g")
#     cytosin = dna.count("c")

# print(f" a의 개수 : {adenin}","\n",f"t의 개수 : {timin}","\n",f"g의 개수 : {guanin}","\n",f"c의 개수 : {cytosin}")

#---------------------------------------------------------------------------------


# 배열 (list, tuple, dictionary) 과제


#예제 1번
# 빈 리스트( 요소가 없는 리스트)를 만들고 프로그램 사용자로부터 총 5개의 정수를 입력받아 리스트에 추가
# 그리고 입력이 끝나면 다음의 내용을 출력하도록 예제를 작성해보기
# - 입력된 정수 중에서 최대값
# - 입력된 정수 중에서 최소값
# - 입력된 정수의 총합

# a=0
# array = []
# while a<5 : 
#     num = int(input(f"{a+1}번째 정수를 입력하세요"))
#     if num >0 :
#         array.append(num)
#         a+=1
#     else:
#         print("0보다 큰 수를 입력하세요")
#         break

# print(f"입력된 정수의 값들은 {array} 입니다.")
# print(f"입력된 정수 중에서 최대값은 {max(array)}입니다. ")
# print(f"입력된 정수 중에서 최소값은 {min(array)}입니다. ")
# print(f"입력된 정수의 총 합은  {sum(array)}입니다. ")


#문제 2 
#사용자로부터 정수형 숫자 하나를 입력. 이 입력된 숫자 만큼 사용자로부터 문자열 입력 받아 리스트에 저장.
# 입력된 문자열들 잘 저장되어 있는지 확인 작업으로 출력.

# 1. 입력된 숫자만 큼 사용자한테 재입력 기회 부여.

# count=int(input("생성할 문자열 갯수 입력 >>"))
# elements = []

# for element in range (count):
#     elements.append(input("단어를 입력하세요>>"))
# print(elements)    


#문제 3 
# 아래와 같이 학생들의 성적을 받아서 score_list 라는 이름의 리스트에 저장하고, 평균을 구하는 프로그램
#(평균은 소수점 2자리까지만 표시)
# 단, 입력값이 0~100 사이가 아니면 다시 입력


#이용자에게 직접 입력할 횟수를 제공하고, 그만큼 입력하게 만들되, 0~100사이의 범위가 아닌경우 재입력을 유도

# count=int(input("학생 수를 입력하세요. "))
# student_total=[]

# for student in range(count):
#     a=0
#     while a<count:
#         number = int(input(f"{a+1}번째 학생의 성적을 입력하세요"))
#         if number>=0 and number<=100:
#             student_total.append(number)
#             a+=1

#         else:
#             print("잘못된 성적입니다. 다시 입력하세요.")
#     print(student_total)
#     print(f"성적 평균은 {sum(student_total)/count}")
#     break


#문제 4 

#첫번째 리스트 list1 =  [10,20,30,40,50] 
#두번째 리스트 list2 =  [1, 2, 3, 4, 5]
#세번째 리스트 list3 =  [list 1+lsit 2를 더한값]

# list1 =  [10,20,30,40,50]
# list2 =  [1, 2, 3, 4, 5]

# list2.reverse()

# result = [list1[element]+list2[element] for element in range (0,5 )]
# print(result)

#예제5. 
# scores = [85,90,78,92,68]
# 1. scores 의 평균 점수를 구하기
# 2. 가장 높은 점수와 가장 낮은 점수 출력
# 3. 점수를 오름차순으로 정렬한 새 리스트
# 4. 80점 이상인 점수만 모은 리스트 만들기
# 5. 리스트 내의 점수를 전부 5점씩 올리는 코드 작성

# scores = [85,90,78,92,68]
# scores_re=sorted(list(scores))

# score_80up= [element for element in scores if element>=80]
# scroe_plus5 = [element +5 for element in scores ]


# print(scores_re)
# print("scores 의 평균 점수 : ",sum(scores)/len(scores))
# print(f"가장 높은 점수 : {max(scores)}, 가장 낮은 점수 : {min(scores)}")
# print(f"오름차순으로 정렬한 리스트는 { list(reversed(scores_re))}")
# print(f"80점 이상인 점수만 모은 리스트는 {score_80up} 입니다")
# print(f"리스트 내의 점수를 전부 5점씩 올리면 {scroe_plus5}과 같습니다.")



# 문제 6  2차원 좌표값은 퓨틀 (x,y) 형태의 데이터를 사용함.

# point1 = (2,3) #x1=2,y1=3
# point2 = (5,7) #x2=5,y2=7
# distance = (((point2[0]-point1[0])**2)+(point2[1]-point1[1])**2)**1/2

# #((x2-x1)²+(y2-y1)²)½




# print( f"point1 의 x 좌표는 {point1[0]}입니다")
# print( f"point2 의 y 좌표는 {point2[1]}입니다")
# print(f" 두 좌표간의 거리는 {distance} 입니다.")

# 문제 7. 아래 딕셔너리를 사용하여 전화번호부 관리.
#1) 박민수 : 010-1111-2222를 추가하시오
#2) 김철수의 번호를 010-9999-0000으로 수정
#3) 이영희의 정보를 삭제
#4) 모든 이름을 출력하시오.
#5) 모든 전화번호를 출력하시오.
#6) 사용자로부터 이름을 입력받아, 전화번호부에서 해당 번호를 찾아 출력하시오.  


# phone_book = {"홍길동":"010-1234-5678","김철수":"010-9876-5432","이영희":"010-5555-6666" }
# phone_book.update({"박민수" : "010-1111-2222"})
# phone_book["김철수"]="010-9999-0000"

# del phone_book["이영희"]
# print(list(phone_book.keys()))
# print(list(phone_book.values()))



# while True :
#     searching = input("찾고자 하는 사람의 이름을 입력하세요>>")

#     if searching in phone_book:
#         print(f"{searching}의 전화번호는 {phone_book[searching]} 입니다")
        

#     else:
#         print("제대로 된 이름을 입력하세요.")


# 문제 8
# 입력 값들의 분포를 시각적으로 볼 수 있는 히스토그램 프로그램
# 1~100이하의 정수 10개를 일겅야 하고, 1~10,11~20 등의 범위에 드는 값들의 횟수를 다음과 같이 출력

#1-10 :
# 그러니까.. 예를 들어 내가 입력한 정수가 1~10 사이에 포함되는 값이면 "*" 의 값이 하나씩 추가되도록
# 프로그램을 짜라는 이야기?
# 그럼 사용자 입장에서 바라볼수 있는 시각적인 디자인에, 리스트에 append 사용하여 하나씩 상승하도록
# 프로그램을 짜면 될듯. 

#1. 범위에 맞는 숫자 범위 지정?
# 딕셔너리를 만들어서 범위 지정 후, 그 범위 내에 삽입 예정.

# contents= { 
# "1-10"  : "" , #0
# "11-20" : "" , #1
# "21-30" : "" , #2
# "31-40" : "" , #3
# "41-50" : "" , #4
# "51-60" : "" , #5
# "61-70" : "" , #6
# "71-80" : "" , #7
# "81:90" : "" , #8
# "91:100" : ""  #9
# }

# for element in range(0,10):
#     while True :
#         num = int(input(" 1~100사이의 정수를 입력하세요 >>"))
#         if 0<=num<=100:
#             break
#         else: print("범위 밖 숫자입니다, 다시 입력하세요")
    
#     index = (num-1)//10 #0~9가 나온다. 만약 90 입력시 index = 9
#     keys=list(contents.keys()) #식별자들의 신규 리스트
#     key = keys[index] # key 는 keys의 인덱스 번호 변수. 왜냐하면 위의 index 에서 0~9로 만들었으니.
#     # 위에서 90을 입력했을때 keys[9]이므로, key는 keys의 9번 리스트에 값 들어감.

#     contents[key]+="*"

# for k,v in contents.items():
#     print((f"{k} : {v}"))


# 문제 9 리스트를 이용한 간단한 극장 예약 시스템. 

seat = [0 for n in range(10)] # 좌석별 예약상태를 모두 0으로 설정한 리스트

while True:
    menu = input(' 좌석을 예약하시겠습니까( 1(Y) 또는  0(N) )')
    if(menu=='0' or menu.upper()=='N'):
        print('예약을 종료합니다')
        break

    print()
    print('현재의 예약 상태는 다음과 같습니다. ')
    print('-'*95)
    print('좌석 번호 : ' , end='\t')
    for n in range(1,11):
        print(n,end='\t')    
    print()
    print('-'*95)
    print('예약 상태 : ', end='\t')
    for n in seat:
        print(n, end='\t')
    print()

    while True:
        print()
        seat_num= int(input('몇번째 좌석을 예약하시겠습니까?'))
        if seat[seat_num-1] ==1 :
            print('죄송합니다. 이미 예약된 좌석입니다. 다른 좌석을 선택해 주세요.')
        else:
            break

    seat[seat_num-1]
    print(f"{seat_num}번 좌석 예약 되었습니다.")
    print()
        




