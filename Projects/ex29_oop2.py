# 클래스 변수, 메소드 -- 객체를 생성하지 않아도 사용이 가능한 멤버 [클레스명.멤버명]
#신림고등학교 학생들의 명단을 관리 서비스.. 
# 학생마다 [이름, 학년]을 묶어서 저장하기 위해 그룹을 만들기
# 추가로.. 학생객체 안에 [학교명]정보를 저장하고 싶어..모두 같은 학교학생들이면 굳이 학교명을 학생들마다
# 변수로 가질 필요가 없다면?
# Student 클래스로 만들 객체들이 모두 하나의 변수값을 공유하고 싶을때, [클래스변수]를 만들어 사용할 수 있음


class Student:
    school_name = '신림고등학교'  #여기에 넣으면 클래스변수임.(영역이 student class 내부)
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

# 위 설계(멤버변수 2개)를 가진 객체를 생성

stu1 = Student('sam',1)
stu2 = Student('robin',2)

print(stu1.name,stu1.grade, "-" , Student.school_name)
print(stu2.name,stu2.grade, "-" , Student.school_name)

#클래스 변수는 모든 객체들이 공유하여 사용이 가능하기에, 마치 본인이 가진 변수인 것처럼 사용하는 것도 가능

print(stu1.name,stu1.grade, "-" , stu1.school_name)
print(stu2.name,stu2.grade, "-" , stu2.school_name)
# 위 객체명,변수명으로 클래스 변수를 사용하는 것은 권장하지 않음. (사용이 가능하긴 한데 판별이 어려울지도)
# 마치 객체마다 변수가 있는 것처럼 오해될 수 있어서.

#객체명을 사용하면 안되는 이유

stu2.school_name = '종로고등학교' # 객체명을 이용해 클래스명 변경이 된게 아니라, stu2객체에 새로운 school_name 변수를 추가한것
print(stu1.name,stu1.grade, "-" , stu1.school_name)# 클래스 변수가 출력
print(stu2.name,stu2.grade, "-" , stu2.school_name)
print(Student.school_name)
Student.school_name='종로고등학교'
print(stu1.name,stu1.grade, "-" , stu1.school_name)
print(stu2.name,stu2.grade, "-" , stu2.school_name)

#정리.. 클래스변수를 제어하려면, 무조건 클래스명. 으로 접근.
#ex) 
# Student.school_name = '송파 고등학교'

#클래스 변수가 있다면.. 클래스 메소드도 만들 수 있음.

class Hello:
    #일반 메소드
    def show(self):
        print('this is show method...')        
    

    #클래스 메소드 - 클래스메소드가 되려면.. 파이썬 인터프리터에게 '데코레이터 @ '를 이용하여 클레스 메소드라고
    #표기해야함.

    @classmethod #만드는 방법은 똑같지만, 표기만 해두는 거임.
    def output(self):
        print("output!!!!!!!")

#일반 멤버함수(메소드)는 객체를 생성하지 않으면 호출할 수 없음. 
#객체를 생성하지 않아도... 클래스명. 을 통해 메소드 호출이 가능. 
print()
Hello.output()

#대표적인 사용모습 .. 현재시간 .. now()함수.

# import datetime

# now = datetime.datetime.


