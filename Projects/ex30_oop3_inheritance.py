#상속 inheritance -- 이미 설계된 다른 class를 상속받아 새로운 멤버만 추가하는 문법

# 문법 학습 전에 대략적인..상속의 필요성[개념]을 보여주는 예)

#게임 개발 ... 로봇 케릭터 필요 (이동기능, 공격기능)

class Robot : 
    #이동기능
    def move(self):
        print('아장 아장....')
    #공격기능
    def attack(self):
        print('주먹 발사!!')

#Robot 객체 생성 
r= Robot()
r.move()
r.attack()
print()

r1 = Robot()
r1.attack()
r1.move()

#캐릭터 종류를 추가... [공중유닛] .. 날아다니는 로봇
#Fly robot 설계[이동,공격, + 나는 기능 까지 추가][robot 기능 + 나는기능]
# 원래 있던 Robot 클래스에 나는 기능을 추가하면, 모든 로봇이 날아버림.
print()

class FlyRobot:
    #이동기능
    #공격기능
    # + 나는 기능
    def move(self):
        print("아장 아장")
    def attack(self):
        print("주먹 발사!!")
    def fly(sefl):
        print("날아서 이동")

fr=FlyRobot()

fr.attack()
fr.fly()
fr.move()
print()

#또 새로운 캐릭터 추가..[해상유닛 -- 수영하는 로봇이 있었으면]
#새로운 유닛이니.. 새로운 설계도를 만들어야 함..

class SwimmingRobot(Robot): #Robot클래스의 기능들을 굳이 다시 작성하지 않고 그대로 가져오기 (상속 inheritance)
    #이미 [이동,공격] 기능을 보유한 상태임. 
    #새로운 기능만 추가하면 됨.
    def swimming(self):
        print("음~파")

sw=SwimmingRobot()
sw.attack()
sw.move() # 만든적이 없는 메소드.. Robot 클래스에 있던 메소드를 상속받아 내것인양 사용!!
sw.swimming()

#SwimmingRobot 의 경우 Robot 을 상속받았기에 기능 구현을 직접 안해도. 편하게 물려받아 내것인양 사용가능


# 상속 문법 조금 더 알아보기 
# First - Second (퍼스트를 상속받은 세컨드 클래스 만들어보기)

class First:
    #생성자를 만들어서 멤버변수 a 만들기 
    def __init__(self):
        self.a=10
        print('First 객체가 생성되었습니다.')
    
    #멤버변수를 출력 기능 메소드

    def show(self):
        print('a : ', self.a)


# First 클래스를 상속하는 Second 클래스 설계

class Second(First):
    #이미 First의 멤버들 [a,show()]을 이미 보유한 상태
    
    #second 클래스도 본인의 멤버변수를 만들기 위해 초기화 영역(생성자 함수) 추가하기 
    def __init__(self):
        super().__init__() # 명시적으로 상속해준 클래스의 생성자 함수를 호출해줘야만 함.
        self.b=20   #must[super()이 상속해준 클래스 객체를 의미함]
        print('Second 객체를 생성했습니다. ')

    #멤버값 출력기능 만들기 [기존에 있는 show() 기능이 맘에 들지 않아서 다시 만들기_override
    def show(self):
        super().show() # first의 쇼가 발동. super()<- 상속자의 기능을 불러올때
        print('a : ', self.a)
        print('b : ', self.b)    


#Second 객체 생성
s= Second() # 상속해준 First 객체도 같이 생성됨.
#상속해준 first 의 멤버를 사용. 

print(s.a) # 상속문법의 진정한 의미는.. 상속해준 First 객체의 멤버를 마치 내것인양 사용할 수 있도록해주는 문법
print(s.b) #Second 에서 새로만든 변수

#멤버값을 출력하는 기능을 사용해보기.

s.show() # 상속받은 멤버 출력기능을 내것인냥 호출해보기.. [새로 추가된 Second의 b 변수를 출력하지 않음.]
#S.show() 기능을 오버라이드 하여.. 개선된 기능 사용

print('-'*30)
print()

#상속과 오버라이드 메소드 사용에 대한 마지막 연습예제.

#예) 어떤 대학의 웹사이트의 회원데이터 저장 [회원 종류가 여러개.. ]

#일반회원 : 이름, 나이 
#학   생 : 이름, 나이, 전공
#교   수 : 이름, 나이, 연구과제
#근로학생 : 이름, 나이, 전공, 업무

#일반회원 데이터를 저장하기 위한 클래스 설계 

class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('Person 객체 생성')


    def show(self):
        print('이름 : ', self.name)
        print('나이 : ', self.age)

p = Person('sam', 20)
p.show()
print()


#학생회원 정보 저장을 위한 Student 클래스를 설계 및 생성.[Person 클래스를 상속받아서]

class Student(Person):
    def __init__(self, name, age , major):
        super().__init__(name, age)
        self.major=major
        print('Student 객체')

    def show(self):
        super().show()
        print("전공 : ",self.major)

    #전공 정보도 출력하는 기능으로 show()를 개선
s=Student('robin',30,'AI web')
s.show()
print()
#교수 회원 [일반회원 + 연구과제]

class professor(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject=subject
        print("Professor 객체")

    def show(self):
        super().show()
        
        print("연구과제 : ",self.subject)

p = professor('park',50,'catapi')
p.show()
print()
#근로 학생 [학생 + 업무]

class WorkStudent(Student):
    def __init__(self, name, age, major,work):
        super().__init__(name, age, major)
        self.work=work
        print("WorkStudent 객체 생성")
        

    def show(self):
        super().show()
        print("업무 : ", self.work)

w = WorkxStudent('kim',30,'Ai data','laundry')
w.show()