# python desktop GUI 용 프로그램 만들기
# 표준모듈인 tkinter 사용 [ TK(툴킷) interface 의 약자]

from tkinter import * # tkinter 모듈 안에 있는 모든 클래스, 함수, 변수, 상수들을 import

# GUI 화면을 구성하는 구성요소들을 tkinter 에서는 [위젯]이라고 부름
# 위젯 종류
#1. 컨테이너 용 위젯[다른 위젯들을 담기 위한 위젯] : Tk,Frame,...
#2. 단순 위젯 : label, Button, Entry....

#GUI 프로그램의 제작 프로세스 : 최상위 위젯을 만들고, 그 안에 원하는 위젯들을 배치관리자를 통해 배치. 

#1] 최상위 윈도우 창 객체 생성. 

window = Tk()

#화면 구성은 최상위 윈도우 위젯의 mainloop() 요청 전에 추가 해야함. 
#3] 윈도우 창의 제목 설정
window.title('this is python GUI')

#4] 윈도우 창 크기 설정
window.geometry('400x500-200+30') # 너비x높이+x축+y축 ( +왼쪽부터 , + 위쪽부터)

#5] 창 크기 조절을 막을 수 있음.
window.resizable(False,True)
window.resizable(height=False,width=0)

#window 창에는 print()로 출력안됨. 글씨를 보여주는 위젯(구성요소)을 만들어서 그 안에 글씨를 쓰고 window에 배치
#6] Label

label = Label(window,text='Hello. Python GUI') # 이 라벨위젯이 붙을 컨테이너 위젯을 지정, 보여줄 글씨를 지정
#라벨을 적절한 위치에 배치해주는 기능 pack()

label.pack()

#글씨를 하나더 보여주려면.. 또 다른 Label 위젯 필요. 글씨(fg), 글씨배경(bg) 색상도 바꾸기. 

label2=Label(window,text='nice to meet you', bg='yellow',fg='blue')
label2.pack()

#사이즈를 지정해보기
label3=Label(window,text="안녕하세요",bg='black',fg='white',width=10,height='3') #너비 10글자
label3.pack()

#폰트 지정해보기
label4=Label(window, text='have a good day. 반가워요',font='times 20 bold italic') # 글꼴,크기, 볼드여부, 이텔릭
label4.pack()

#7] 버튼 추가하기
def aaa():
    print('clicked!!') # 내 콘솔창에 프린트 될뿐


btn = Button(window,text='눌러주셈',padx=10,pady=10,command=aaa)  
# 패딩x,y 는 여백. command = 버튼 클릭시 실행될 함수 이름만[함수가 버튼 보다 먼저 정의 되어있어야함.]
# 다른방법도 있음. 클래스로 만들면 됌.
btn.pack()

#8] 버튼 클릭할때 라벨이 보여주는 글씨 변경

label5 = Label(window,text="hello world")
label5.pack()

num=0
def bbb():
    global num
    num+=1
    label5.config(text='clicked button!! : ' + str(num))
    

btn2= Button(window,text='change text', command=bbb)
btn2.pack()     


#9] Entry 사용자로부터 한줄 텍스트를 입력받는 위젯
entry=Entry(window)
entry.pack()

# 버튼 클릭할때, entry 에 써 있는 글씨를 label에 보여주기

def ccc():
    value = entry.get()
    label6.config(text=value)


btn3= Button(window,text="입력완료", command=ccc)
btn3.pack()

label6 = Label(window, text="")
label6.pack()

#10] 여러줄 입력이 가능한 위젯
text=Text(window,width=30,height=3) # 30칸, 3줄
text.pack()




#11] 버튼 클릭할 때 경고(알림)창 보이기
from tkinter import messagebox # 하위 모듈을 임폴트

def ddd():
    value = text.get('1.0',END) # 1.0 첫번째 줄(1)의 첫번째 칸(0)에서부터 END(끝)까지 값을 읽어와라.
    messagebox.showinfo('메세지 값',value) # 알림창의 제목, 메세지
btn4= Button(window,text="메세지 읽기",command=ddd)
btn4.pack()



#2] 최상위 윈도우가 화면에 보여지며.. 사용자의 마우스 이동 , 클릭, 버튼클릭 같은 이벤트 처리를
# 지속적으로 수행하도록 요청하면 화면에 윈도우가 보임.
window.mainloop()





