# 함수 (fuction 기능) : 특정 기능을 수행하는 코드를 모아놓은 코드 영역
#예) 로그인함수 (==로그인 기능 코드들), 회원가입 함수 ( == 회원가입 코드들 영역)

# [ 특정 기능을 작성한 코드 영역을 필요할 때 마다 언제든 호출(call)하여 그 코드 영역이 실행되도록...]

# 파이썬 함수의 종류
#1. 표준(내장)함수 : 이미 파이썬에서 만들어서 내장해 놓은 함수들 print(), input(), len() 등등
#2. 외부함수 : 기존 개발자 또는 업체들에서 만들어 라이브러리로 제공하는 함수. 내장되어 있지 않아서 그냥 사용 불가능.
# 대신 그 모듈( 함수들을 가진 폴더 )을 파일에 삽입(import)하여 불러 사용함.

#3. 개발자 정의 함수 ( 11월 25일 수업 내용임)

# 코드가 써 있는 영역을 구분하기 위해 보통 함수의 이름을 영어로 작성 ( 동사 verb)
# 함수 이름 ( 식별자 ) 옆에 소괄호()가 반드시 있어야 함. 이를 통해 변수와 구별함.
# age <--- 변수 
# login()  <- 함수

#1. 함수 정의 문법 def [ define ]


def show():
    print('show function..')
    #코드 영역에 여러줄 코드 당연히 가능
    print('good')



#함수를 정의했다고해서 코드가 실행되는 것은 아님. 함수를 사용하겠다고 호출해야 그 영역의 코드들이 실행됨.
# 함수 호출 - function call
print('함수 호출 연습')

show()
# 필요할 때 언제든 다시 함수를 호출할 수 있음. 그럼 그 코드 영역이 다시 실행됨.
show()
print()

# 함수 호출할 때마다 같은 글씨만 출력되는 기능은 효용성이 약해보임. 
# 내가 전달한 값을 출력해주는 기능이 필요한 경우도 있음.

#2. 함수를 만들때 파라미터(값)를 전달받는 함수 만들기
def show_name(name): # name 처럼 소괄호()안에 전달된 값을 받기 위한 변수를 '매개변수(parameter)' 라고 부름
    print('welcome', name)

#함수를 호출하면서 매개변수에 값 전달..

# show_name('sam')
# show_name('bethi')
# show_name(input("이름을 입력하세요>>"))
# print()

# 매개변수는 여러개 일 수도 있음.
def output(a,b):
    print('a: ',a)
    print('b: ',b)

output(1,2)    
output(100,200)
# 사용시 주의점 : 함수호출할 때 매개변수의 개수만큼 값을 줘야만 함.

#output(1000) #이렇게 하면 에러남. 파이썬은 안됨. 
#output(1000,2000,3000) # 이래도 에러남. 무조건 갯수에 맞춰서

print()

# 결국 파라미터 개수만큼 반드시 값을 전달해야만 함..
#근데.. 경우에 따라서는 값 전달하면 그 값을 보여주고, 아니면 기본값 보여줘.. 이럴땐?
# -> 기본값 지정
#3. 함수 파라미터의 default value 지정.
def display(a=1,b=2):
    print('a의 값 : ',a)
    print('b의 값 : ',b)

display(100,200)
display(100) #a=100, b는 기본값
display() # a,b 모두 기본값
# 근데.. 값 1개 줄건데.. b에게..
display(b=1000)
display()

def display2(a,b=2):
    print(a,b)

display2(10)
display2(10,20)   
# display2(b=50) #error 

show_name('hong')
output(10,20)
display()
print()

#기능을 만들다 보면.. 전달 값이 몇개인지 특정하기 어려움.
# 예) 전달받은 모든 값 출력... 모든 값 덧셈.. 

#해결방법1) 여러개의 값을 받기 위해 리스트 1개로 받기..
def cal_total(number_list):
    print('전달받은 값의 총합 :', sum(number_list))

cal_total([10,20,30])
cal_total([10,20,30,4,45,6,7,1,2,3,5])
cal_total([10,20,30,1,2,5,1,23])
# cal_total(10,20,30) []안썼기 땜시 error

#4. 매개변수의 길이가 가변적인 파라미터 variable length aragments [가변 파라미터]

def nice( *values ): #   *표시를 매개 변수만들때 맨앞에 표기
# 보기에는 변수 1개로 보이지만, 내부에서는 리스트로 만들어줌. 
    print('전달 받은 값의 개수 : ', len(values))

# nice()
# nice(10)
# nice(10,20,30)
# print(type(nice))
# print()

# # 표준 내장 함수 중에서 가변 파라미터를 사용하는 함수

# aaa=[10,20,30]
# m=max(aaa) # 파라미터에 리스트 1개를 전달

# print(m)
# m=max(40,50,60,70)
# print(m)

# max()

#--------------------------------------------------------

#함수를 정의할 때 유의할 점..  같은 이름의 함수를 또 정의하면??
def aaa():
    print('aaa function')
aaa()

def aaa():
    print('다시만튼 aaa function')

aaa()

def aaa(num):
    print('aaa num:', num )

aaa(10)
# aaa() # 값 안줘서 에러뜸. 파이썬은 그냥 다 덮어써버림. 

# 그래서 주의 ... 여러분은 모든 내장함수의 이름을 외우지 못함. 
# 하필 내장함수와 같은 이름의 함수를 만드는 경우가 있을수 있음.
# def max():
#     print("내가 만든 max()함수")

# 변수 이름도 식별자여서, 내장 함수명을 변수명으로 덮어지기도 함. 
# min= 100
# min(10,5,4,3,2) 내장함수명에 겹치지 않도록 할것.

print()

# 함수의 호출문이 .. 함수 정의보다 먼저 되면 안됨!!!!!!!! 정의 -> 함수 호출 

#------------------------------------------------------------------------

#5. 리턴을 해주는 함수.  -- 함수안에 print()로 출력만 하는게 아니라.. 연산결과를 함수를 호출하는 쪽으로
# 되돌려주는 문법 return
def aa():
    return 10   # 10이라는 값을 호출하는 쪽으로 돌려주는 기능함수

num = aa() # 함수의 실행결과인 return 값 10을 받으려면 = 대입 연산자로만 받을 수 있음.
print(num)


# hello 라는 문자열을 리턴해주는 기능
def bbb():
    return 'hello'
s=bbb()
print(s)


# 매번 같은 값만 리턴되면 효용가치가 떨어지는 기능임. 
# 2개의 정수를 전달하면 덧셈의 결과를 계산해서 리턴해주는 기능(함수)
def add(a,b):
    x=a+b
    return x

num = add(3,5)
print(num)

# return 을 할때, 값이 없이 사용하는 것도 가능함.

def ccc():
    print('ccc function')
    return # 이 글자를 만나면 되돌아가라고 하는 것이어서 이 함수의 코드 영역이 종료되는 것을 의미함
    print('zzzz') # return 다음에 나온영역이므로 의미 없음. 실행 안됨..


ccc()

def ddd(n):
    #음수면 출력금지
    if n<0:
        print("음수는 출력이 금지됩니다.")
        return  # 값 주는 것 없지만 끝내고 싶을때
    print(n)

ddd(10)
ddd(-10)
print()


#만약, 실수로 리턴 값이 없는 함수의 실행결과를 대입 받으면.. None
def eee():
    print("eee!!!!!")

x=eee()
print(x)
print()

#리턴값은 원래 1개만 가능함. 근데 파이썬은 여러개를 해도 에러 아님. 
def fff():
    print('ffff~~~~~~~~~~')
    return 10,20,30

a,b,c= fff()
print(a)
print(b)
print(c)

#일반 변수 대입도 한번에 여러개 대입이 되었었음.
n1,n2=100,200

a=100,300 # a 변수가 여러개의 값을 가진것이 아님. 튜플1개를 가짐. 

def ggg():
    print('gggggggggg')
    return 100,200,300

#a,b,c,d = ggg() error
a=ggg() # 리턴 값들 (100,200,300)을 자동으로 tuple로..
print(a)



n=('aa','bb')
print(n[0])
print(n[1]) 

a,b=n # 튜플이나 리스트의 요소를 분해하여 변수에 대입 가능
print(a)
print(b)

def hhh():
    return['sam','robin','hong']

name_list=hhh()
print(name_list)
print(len(name_list[0]))

#리턴된 리스트 1개를 분해하여 요소별로 변수에 바로 대입

name1, name2, name3 = hhh()

print((name1,name2,name3.upper()))
print()



#[별외.] 지역변수(local variable) 와 전역변수(global variable)에 대한 이해...

def mmm():
    age = 20 # 지역 변수 - 함수 안에서 처음 만들어진 변수 : 이 지역 안에서만 인식 가능
    print('나이 : ',age)

mmm()
# 함수의 지역변수는 밖에서 사용 불가능
#print('밖 : ', age) error

# 함수 밖에 만든 변수는 전역변수임...

name = 'park'
def nnn():
    # 함수안에서 변수값을 변경하려는 코드를 쓰면.. 새로운 지역변수 생성문법으로 인식.
    name = 'kim' # 새로운 지역변수를 만들었다고 생각함.
    print(' 함수 안 : ', name) # 밖에서 만들어진 변수를 사용할 수 있음.

nnn()
print(' 함수 밖 : ', name) # 여기서도 사용가능. 그래서 전역변수

#그래서 함수안에서 전역변수의 값을 변경하고 싶다면 .. 내가 사용하는 변수가 전역변수임을 명시적으로 알려줘야함.
# 
def ttt():
    global name # 이 함수 안에서 name 변수는 밖에 있는 전역변수를 사용할 것이라고 명시!
    name = 'lee' 
    print('함수 안 : ', name)

ttt()

print('함수 밖')
























