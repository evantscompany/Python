# oop ( obeject oriendted programming ) - 객체 지향 프로그래밍
# 객체지향을 위한 중요한 용어 : class(클래스), object(객체)

#왜 class 와 object 라는 것이 등장했는지에 대한 필요성..알아보기

#예) 학생의 성적을 분석하고 관리하는 서비스 개발 

# 학생의 [이름, 국어,영어,수학,평균] 데이터 저장.

# 값을 저장해야하니 변수 필요

name='sam'
kor = 80
eng = 70
math = 90
aver=80.0

# 학생1의 값들을 출력

print(name,kor,eng,math,aver)
print()

# 두번째 학생이 있다면?? 

#name = 'robin 으로 하면 첫번째 변수 'sam'이 사라짐.
name2 = 'robin' 
kor2=50
eng2=40
math2=60
aver2= (kor2+eng2+math2)/3
 
print(name2,kor2,eng2,math2,aver2)
print()

#이런 학생들이 만약 10명이면.. 100명이면?
#변수명을 만드는 것도 어려워짐. 개별 변수가 너무 많아짐
#다른 학생의 데이터를 사용하는 실수도 있을수 있음

#변수 하나에 학생 한명의 데이터들[이름,국어,영어,수학,평균]을 묶어서 가지고 있으면 관리가 더 용이.
#여러개의 데이터를 묶어서 저장해주는 타입 [리스트],(튜플),{딕셔너리}을 이용해보기

# 먼저 리스트로 묶어보기. 
aaa=['sam',70,80,90,80.0]
bbb=['robin',40,50,60,50.0]

print(aaa)
print(bbb)

#학생의 성적 분석을 위해. 두 명의 학생 성적 중 '국어'성적만 뽑아서 출력
print('학생1의 국어성적 : ', aaa[1])
print('학생2의 국어성적 : ', bbb[1])
print()

#데이터 추출이 가능은 하지만.. '수학' 찾으려면, 인덱스 번호라서 정확히 뭔지 식별이 불편함.
#bbb['수학'] 이런식으로, 요소값의 의미를 알수 있는 식별자를 이용하면 가독성이 좋아짐.


#key:value 쌍으로 데이터를 저장하는 dictionary 사용
ccc = {'name':'sam','kor':70,'eng':80,'math':90}
ccc['aver'] = (ccc['kor']+ccc['eng']+ccc['math'])/3
print(ccc)
print('학생의 수학성적 : ',ccc['math'] ) #수학성적 뽑을때 식별자를 이용하기에 가독성이 좋음.
print()

# 또 다른 학생의 데이터를 저장

ddd = {} # 식별자를 계속 쓰는게 짜증... 
print()

# 딕셔너리를 이용하면 식별은 좋지만 .. 학생데이터를 만들때 마다 같은 이름의 식별자를 
# 지속적으로 작성해야함 - > 이거 짜증.

# 그래서 새로운 타입의 변수를 만들수만 있다면 ... 
# [이름, 국어, 영어, 수학, 평균]을 한번에 저장할 수 있는 변수가 있다면.. 
# 더 편하게 사용이 가능하지 않을까? 
# 즉, 큰 상자같은 것이 있었으면... 좋겠지만, 파이썬은 위 다섯개의 데이터를 저장하는 타입을 만들어주지 않음.

#그래서, 개발자가 이런 큰 박스의 모양을 설계하여 사용할 수 있도록 제공되는 문법

# 똑같은 모양의 변수들을 dict 처럼 묶어서 필요할 때마다 만들어주는 문법 
# 이를 class(묶음 설계도) 와 object(설계도로 만든 제품. 객체) 라고 함. 

# class     : 연관있는 데이터(변수)와 기능(함수)을 묶어놓은 설계도
# object    : class 설계도를 기반으로 실제 메모리에 만들어진 제품

# 학생의 [이름,국어,영어,수학,평균] 변수를 하나의 그룹(class)으로 묶는다고 설계해보기.
# 파이썬 시스템에게 이렇게 묶을거라고 알려주는 설계도
# class 이름 명명하는 규칙 : 변수 식별자 규칙과 유사함. 
# 표기법은 스네이크표기법 말고, 단어의 첫글자를 대문자로 사용하는 파스칼표기법을 권장


class Student:
    #변수 5개를 사용하겠다고.. 미리 설계할 것임. 단 변수도 초기화가 필요하듯이 class 묶음도 초기화 과정 필요
    #이 class로 제품(객체,object)을 만들때 자동으로 처음 실행되는 영역(함수)이 존재함 (생성자 함수 라고 부름)
    def __init__(self):
        print ('Student 설계도 (class)로 객체가 생성되었습니다. ')
        #이 제품이 가지고 있을 값들을 저장할 변수들을 선언. 이 생성자 함수 안에서만 사용하는 지역변수가 됨
        #변수명을 그냥 쓰면 안되고.. 이 클래스 본인 것이라고 말하면서 선언해야 함. 
        #클래스 영역 안에서 본인것이라고 인식하는 키워드가 존재함. 그게 함수의 파라미터로 전달된 self
        #이 클래스의 소속임을 표현하는 self 로 만들어진 변수를 맴버변수라고 부름(self.oo)

        self.name='sam'
        self.kor = 0
        self.eng = 0
        self.math = 0
        self.aver = 0.0

    #멤버변수의 값들을 알아서 출력해주는 기능함수를 정의 -- 멤버함수(다른 용어로 메소드)
    def show(self): #파이썬의 클래스 영역 안에서 멤버변수를 지칭하려면 반드시 self와 함께
        #무조건 함수의 파라미터에 self 가 있어야 함. 
        print('이름 : ',self.name)
        print('국어 : ',self.kor)
        print('영어 : ',self.eng)
        print('수학 : ',self.math)
        print('평균 : ',self.aver)
        print()

    #멤버변수에 값을 대입해주는 기능함수 - 대입할 값을 함수의 파라미터로 받아서 멤버변수에 대입
    def set_members(self,name,kor,eng,math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.aver = (kor+eng+math) /3


    


#class 는 설계도임. 아직 제품이 아니기에.. 클래스를 설계했다고 해서 그 안에 있는 코드가 실행되지 않음
# (마치 함수 정의해 놓은 것과 비슷)

#Student 라는 이름을 가진 클래스(설계도)를 기반으로 제품(객체)을 만들어보기
# 객체 생성 문법(함수 호출문과 유사함): 클래스명()

Student() # 객체가 생성되면 __init__()함수의 영역이 실행됨. 이때 이 제품안에 5개의 변수가 만들어짐.

#같은 설계도를 또 다른 제품(객체)를 생성할 수 있음, 이때 이 제품안에 5개의 변수가 만들어짐.
Student()

# 객체(5개의 변수를 한번에 가지고 있는 녀석)를 만들었으면 이제 사용해야하는데..
# 이 객체를 제어하는 변수가 없으면 사용 불가. 
# print('이름:', ????)

# 마치 리스트를 만들고 변수에 대입을 안한 것 과 같은 상황

#객체를 사용하려면 변수에 대입
stu1=Student()#stu1 이라는 변수를 이용하여 Student 설계도로 만든 객체를 제어할 수 있음. 
print(stu1) # stu1 이라는 참조변수가 참조하고 있는 실제 Student객체의 위치 (메모리 주소)를 출력함.
#stu1이 참조하는 Student 객체 안에 있는 변수들을 사용하기. [이때 사용하는 것이 . 연산자]


print('이름 : ', stu1.name)
print('국어 : ', stu1.kor)
print('영어 : ', stu1.eng)
print('수학 : ', stu1.math)

#객체 안에 있는 작은 변수(맴버변수)들에 값들을 대입할때 리스트처럼 한번에 넣는 것은 불가능. 하나씩 대입해야함.
stu1.kor=70
stu1.eng=80
stu1.math=90
stu1.aver=(stu1.kor+stu1.eng+stu1.math)/3

print('이름 : ', stu1.name)
print('국어 : ', stu1.kor)
print('영어 : ', stu1.eng)
print('수학 : ', stu1.math)
print('평균 : ', stu1.aver)
print()

# 두번째의 학생의 데이터 저장이 필요하면 변수 5개를 만들어야 하지만
#Student 라는 큰 덩어리를 설계해 놓았으니, 
#Student 덩어리 객체를 하나 만들면 안에 멤버로 5개의 변수가 한번에 만들어짐. 

stu2=Student()

stu2.kor=40
stu2.eng=50
stu2.math=60
stu2.aver=(stu2.kor+stu2.eng+stu2.math)/3

print('이름 : ', stu2.name)
print('국어 : ', stu2.kor)
print('영어 : ', stu2.eng)
print('수학 : ', stu2.math)
print('평균 : ', stu2.aver)
print()

#이런식이면, 새로운 학생을 만들고 출력할때마다.. 저 맴버값 출력코드를 매번 작성하는 것이 매우 번거로움.
# 그래서.. 이 객체에 본인의 멤버변수값들을 출력해주는 기능이 있다면? 
# stu2.출력해줘()
# stu1.출력해줘()

# 그래서 파이썬의 클래스 영역안에 변수 외에 함수도 미리 만들어놓을 수 있음.

# 세번째 학생

stu3=Student()
stu3.name='hong'
stu3.kor=10
stu3.eng=20
stu3.math=30
stu3.aver=(stu3.kor+stu3.eng+stu3.math)/3

stu3.show()
stu2.show()
stu1.show()

#4번째 학생도 손쉽게 멤버값들을 출력할 수 있음...근데??
stu4=Student()
#객체를 만들고 그 멤버변수에 값을 대입할 때 멤버변수 하나에 한줄씩 대입하는 것 짜증
#전달할 값을 한번에 넣어주는 기능이 있다면.. 편하지 않을까요?
# stu4.입력해줘   # 평균까지 알아수 계산하여 대입해주면 짱!
#Student 클래스를 설계할 때 입력기능도 같이 설계... 

stu4.set_members('kim',50,60,70)

stu4.show()
stu3.show()
stu2.show()
stu1.show()

#5번째 학생도 쉽게 저장 및 출력가능 

stu5=Student()
stu5.set_members('lee',10,20,30)
stu5.show()

stu6=Student()
stu6.set_members('park',100,90,80)
stu6.show()

# 가만보니 객체를 생성하고 난 후 언제나 값을 대입하는 기능을 호출함.
# 이 특별한 함수를'생성자 함수 constructor 함수' 라고 부름. 파이썬은 이 용도의 함수명을 미리 정해놓았음
# __init__
# 이 생성자 함수의 파라미터에 값을 전달하여.. 생성하면서 값 대입이 가능해짐.
print()
print('-'*50)
print()


# ----------------------------------------------------------------

#새로운 클래스를 설계하여.. 생성자 함수에 값 전달하는 실습 진행..
#[이름,나이,주소] 정보를 그룹으로 묶어서 가질 수 있는 객체를 만들기 위한 클래스 설계 

class Member:
    
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def show(self):
        print("이름 : ", self.name)
        print("나이 : ", self.age)
        print("주소 : ", self.address)
        print()

m1=Member("김씨",20,'인천')
m2=Member("박씨",25,'서울')
m3=Member("홍씨",41,'경기')

m1.show()
m2.show()
m3.show()

# 각 객체들의 나이만 출력하려면.. 
print('나이 : ',m1.age)
print('나이 : ',m2.age)
print('나이 : ',m3.age)



member_lsit = [m1,m2,m3,Member('hong',40,'new york')]
for member in member_lsit:
    member.show()

print()

#-----------------------------------------------------------------------------

#여러 학생의 [이름,파이썬,웹,AI] 성적 데이터를 저장하기 편하도록 4개 데이터를 한번에 저장하는
# 객체를 설계하여 사용

class Stu :
    def __init__(self,name,py,web,ai):
        self.name=name
        self.py=py
        self.web=web
        self.ai=ai
    #멤버변수의 값을 출력해주는 기능함수 설계하기 - 멤버함수의 첫번째 파라미터는 언제나 self 등록
    def show(self):
        print(self.name,self.py,self.web,self.ai)
        print()
    #총첨을 계산하여 리턴해주는 기능 함수 설계하기
    def get_total(self):
        return self.py+self.ai+self.web

# class 는 단지 설계도임. 아직 객체가 되지 않았기에 사용이 불가능함.
# class 설계대로 멤버 (변수4개,함수1개) 를 가지는 객체를 생성하여 사용

s1=Stu('sam',80,70,50)
s1.show()

s2=Stu('robin',60,40,20)
s2.show()

# 만약 학생별 성적의 총점을 저장하고 싶다면?
# 직접 계산하기에는 좀 짜증. 학생이 많아서. 
# Stu 객체 안에 총점을 계산하여 주는 기능함수가 있으면 편할듯//

total_1 = s1.get_total()
print('1번 학생의 점수 총점 : ', total_1)

total_2 = s2.get_total()
print('2번 학생의 점수 총점 : ', total_2)

# module_a 에 person 클래스를 설계하고 사용해보기. 


        

# 객체 안에 변수와 함수가 같이 존재함. 
# 파이썬은 객체밖에도 변수와 함수를 만들어 사용할 수 있음. 

# 그래서 용어를 분리하여 부름.
# 객체 밖에서 값을 저장하는 것을 '변수 variable', 기능 코드가 있는 영역을 '함수function'
# 객체 안에서 값을 저장하는 것을 '속성 property', 기능 코드가 있는 영역을 '메소드, method'
#                              (멤버 변수)                            (멤버 함수)

a= 10 # 변수
def aaa(): # 함수
    pass

# p1.name # 객체의 속성값
# p1.display # 객체의 메소드














