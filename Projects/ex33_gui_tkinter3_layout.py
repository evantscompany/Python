# 배치관리자 .. pack,grid,place

from tkinter import *

window=Tk()
window.title('gui layout')
window.geometry('400x300+100+50')
window.resizable(False,False)

# 위젯 배치방법 3가지 

#1) pack
btn1=Button(window,text="button#1")
btn1.pack(side='left',anchor='n')

btn2=Button(window,text="button#1")
btn2.pack(side='right',fill='y')

btn3=Button(window,text="button#3")
btn3.pack(side = 'top',anchor='e')

btn4=Button(window,text='button#4')
btn4.pack(side='bottom',fill='x')

#2) place : 절대위치 .. 원하는 좌표에 배치 (겹칠수도 있음)
btn5 = Button(window,text="button#5")
btn5.place(x=50,y=50)

btn6 = Button(window,text="button#6")
btn6.place(x=70,y=70)

btn7 = Button(window,text="button#7")
btn7.place(x=0,y=250)



#3) grid : 격자(행렬) 배치 --- 계산기 같은 GUI 만들때 용이
# 화면의 일부 영역을 구분하는 용도로 사용하는 컨테이너용 위젯

frame = Frame(window, width=300, height=150,bg='aqua')
frame.place(x=0,y=100)


#프레임 안에 버튼들을 격자로 배치해보기

b1 = Button(frame,text='1')
b1.grid(row=0,column=0)

b2 = Button(frame,text='2')
b2.grid(row=0,column=1)

b3 = Button(frame,text='3')
b3.grid(row=0,column=2)

b4 = Button(frame,text='4')
b4.grid(row=1,column=0)

b5 = Button(frame,text='5')
b5.grid(row=1,column=1)

b6 = Button(frame,text='6')
b6.grid(row=1,column=2)

b7 = Button(frame,text='7')
b7.grid(row=2,column=0)

b8 = Button(frame,text='8')
b8.grid(row=2,column=1)

b9 = Button(frame,text='9')
b9.grid(row=2,column=2)




window.mainloop()



