# # 파일 처리(입출력)를 위한 파이썬의 표준 내장함수 

# #1. 파일에 데이터를 저장하기.  - 파일명을 경로 없이 쓰면.. 이 .py 파일이 있는 곳과 같은 위치에 만들어짐.

# file=open('aaa.txt','w', encoding='UTF-8') # mode : 'w' write, 'a' append, 'r' read

# file.write('This is python progamming....한글도 될까?')

# # 파일 쓰기 작업이 종료되면 반드시 .. 스트림을 닫아야 함. 
# file.close()

# #2. 파일에서 텍스트 데이터 읽어오기 .....

# file=open('aaa.txt','r',encoding='UTF-8') # 파일명이 없으면, 못 읽어오기 때문에, 안 읽어짐.

# contents = file.read()
# print('파일에서 읽을 텍스트 : ', contents)

# file.close()
# print()

# #-----------------------------------------------------


# #3. 파일 이어쓰기. append mode

# file = open('bbb.txt', 'a',encoding='UTF8')

# file.write('apple')
# file.write('banana')
# file.write('orange')

# file.close()

# file = open('ccc.txt', 'a',encoding='UTF8')

# file.write('apple\n')
# file.write('banana\n')
# file.write('orange\n')

# file.close()


# #(응용) 사용자로부터 한줄 리뷰를 계속 입력받아.. 파일에 저장. 단 'quit' 을 입력하면 입력을 종료하는 프로그램.
# # file=open('ddd.txt','a',encoding='UTF-8')

# # while True:
# #     message = input("리뷰를 입력 : ")
# #     if message =='quit'or message =='그만':
# #         break
# #     file.write(message+"\n")

# # file.close()


# #4. 파일 경로에 폴더명 써보기...

# file=open('files/aaa.txt','w')             # [만약 files 라는 폴더가 없다면 에러!! 폴더는 자동으로 만들어주지 않음.]
# file.write('nice to meet you')
# file.close()
# #files 폴더를 직접 만들면 되지만, 실제 이 프로그램이 실행되는 환경은 개발자 pc가 아니라 사용자 pc 임.
# #그래서.. 파이썬에서 시스템의 폴더를 만들거나 삭제할 수 있음. 이를 위한 별도의 라이브러리. 모듈이 존재함. 
# # os 라는 이름.

# #경로를 지정할때, 상대 경로...(상위폴더를 지칭하는 경로)
# file = open('../aaa.txt','w')
# file.write('have a good day')
# file.close()

# #경로를 모두 현재 위치를 기준으로 한 경로만 해봤음. 이런 경로를 상대경로 라고 부름. 
# # 특정 경로를 풀네임으로 지정할 수도 있음. 절대경로 라고 부름.

# # file=open('C:\\aaa.txt','w') #Permission denied: 'C:\\aaa.txt'
# file=open('C:/Users/Admin/aaa.txt','w')
# file.write('aaaa')
# file.close()

# #----------------------------------------------------------------------

# #경로에 대한 학습은 .. 추후에 배울 모듈 수업에서 다시 소개..
# #-------------------------------------------------

# # 5. 문자열 중에 .. 여러줄 문자열 ''' ''' 이 것도 당연히 한번에  쓰기 가능함. 
# file= open('files/bbb.txt','w',encoding="UTF-8")
# data = '''\
# 안녕하세요.
# 여기서 줄바꿈을 해도 잘 되는지,
# 여러줄의 데이터를 써봅니다. 
# 줄바꿈이 될것인가?
# 역슬래쉬 n도 안쓰고 있는데.
# '''
# file.write(data)


# file.close()
# #----------------------------------------------------

# #6. 보통 프로그램에서 저장할 데이터들을 .. 리스트와 같은 형태로 다루어지는 경우가 많음.
# # 리스트 데이터들을 저장해보기.. - 쉽게 보기 위해 한줄에 리스트 요소 하나씩 저장되도록. 

# names=['강중구','김종경','유지희','최준영']
# print(names)


# #데이터를 원하는 형태로 전처리 
# new_names=map(lambda s:s+'\n', names)
# new_names=list(new_names)
# print(new_names)
# file=open('files/902호 학생들.txt','w',encoding='UTF-8')
# #file.write(names)#error
# file.writelines(names)
# file.close()
# print()

# #---------------------------------

# #7. 파일 다룰때 주의할 점. close()를 잊지 않아야 함..사람이라 실수의 여지가 있어서..
# # 이를 보완 하는 특별한 키워드 등장. with 키워드

# with open('ggg.txt','w') as file :
#     file.write('hello python..')

#close()를 안해도 자동으로 with 영역이 종료되면 file 객체에게 close()를 요청해줌.

#8. 아주 긴 파일을 읽어와서 출력해보기

with open('files/long story.txt','r',encoding='UTF-16')as file:
    contents=file.read() # 모든 글씨를 하나의 문자열로 읽어오기. 
    print(contents)

    print("-"*30)

#9. 대량의 데이터를 파일로부터 읽어서 분석하려면, 일단, 대부분의 경우 한줄 단위로 처리함. 
# 그러려면 split('\n) 을 통해 한 줄 단위로 분리하여 리스트로 만들어 처리..
# 이 작업이 번거로워서.. 다행히 file 객체가 이미 한줄 단위씩 읽어오는 기능함수가 존재함.
# 
#  
with open('files/short story.txt','r',encoding='utf-8')as file:
    line = file.readline() # 한줄 읽기
    print('첫번째 줄 문자열 : ', line)


#10. 
# 데이터 분석을 하려면 데이터셋 (data set) 파일들을 많이 읽어와야 하는데. 보통 이 파일들은
# 엑셀 형태가 많음. 
# 엑셀 파일을 읽어서 데이터를 분석하는 경우가 아주 많음..  이를 시도 했으나 엑셀이나 hwp 파일들은
# 데이터 외에 추가정보를 보유하고 있어서 그대로 읽어지지 않음.
# 파이썬의 표준 함수 중에는 엑셀 파일을 읽을 수 있는 기능함수가 없음. 
# 외부 라이브러리 중에는 존재함.. 보통 이를 사용함. pandas 라이브러리에 엑셀파일 쉽게 읽어오는 기능 존재

# 대부분의 분석할 데이터들은 표 형태(행row과 열column 구조) 를 가지고 만들어짐. 
# 이를 위해 등장한 데이터 표기형식 ( csv, xml, json)
with open('files/member.csv','r', encoding='utf-8')as file:
    #contents= file.read() # 통으로 한방에 읽어오면 분석할때 짜증.
    #보통의 표형태의 데이터 구조는 한줄에 한 아이템의 정보들이 존재함. 
    #그래서 한줄 단위로 읽어서 처리

    for line in file : # 자동으로 readline() 하면서 반복수행함. 
        print('한줄의 데이터 : ', line)
        
        #한줄 안에 있는 여러개의 데이터를 분리해서 취득하기 - csv 분석 - parse
        # data_list=line.split(',')
        # print(data_list)

        # print('이름 : ', data_list[0])
        # print('나이 : ', data_list[1])
        # print('주소 : ', data_list[2])
        

        # #인덱스 번호로 칸의 의미를 해석하기 불편-- 리스트의 요소를 분해하여 변수에 대입.
        # name,age,address = data_list
        # print('이름 : ', name)
        # print('나이 : ', age)
        # print('주소 : ', address)

        name, age, address = line.split(',')
        print('이름 : ', name)
        #나이를 1 증가시킨 값을 출력하고 싶다면.. 
        if age.isdigit(): # 문자열이 숫자로만 이뤄졌냐
            print('나이 : ', int(age)+1)
        print('주소 : ', address)


# [추가] mode 지정할 때 + 기호...

#1) w+ ( 읽기+ 쓰기 모두 가능 - 덮어쓰기.. 기존 데이터를 모두 지우고 작성)
with open('files/ggg.txt','w+',encoding='utf-8') as file:
    file.write('new data............')
    #파일 커서의 위치가 글씨의 마지막에 있어서 그냥 읽으면 이후 데이터가 없음.
    file.seek(0)
    contents= file.read()
    print(contents)


#2) a+
with open('ggg.txg','a+',encoding='utf-8')as file:
    file.write('새로운 데이터~~~~~~~~')
    file.seek(0)
    print(file.read())



#3) r+ 읽기+ 쓰기 ~ 덮어쓰기.. 단 w+와 다르게 전체를 지우고 쓰지 않음. 
with open('files/ggg.txt','r',encoding='utf-8') as file:
    file.write('덮어쓰기')
