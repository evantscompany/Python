#GUI 로 성적 관리 프로그램 만들기 
# 기능요구 
#1. 사용자로부터 [이름, 국어, 영어, 수학 ] 점수를 입력받아야 함
#2. [입력완료] 버튼을 클릭하면 [총점, 평균]을 자동 계산하여 데이터들을 리스트 박스에 추가해야함.
#3. [입력취소]버튼을 통해 입력된 모든 글씨 일괄 삭제
#4. 리스트박스의 항목을 선택하여 삭제하는 기능 [버튼으로 실행]
#5. 리스트박스에 등록된 성적 데이터를 csv 파일로 저장하는 버튼



#[5]. 각 버튼들이 클릭되었을때 수행할 작업코드들을 별도의 함수들로 만들어서 버튼에 적용하기

#------------------------------------------------------------------------------

def clicked_complete():
    #각 entry 위젯에 써있는 글씨를 얻어오기
    name = entry_name.get()
    kor=entry_kor.get()
    eng=entry_eng.get()
    math=entry_math.get()
    #중간 확인
    print(name,kor,eng,math)
    pass
    #총점, 평균계산 [주의 : 모든 사용자 입력은 string 문자열..]
    total = int(kor)+int(eng)+int(math)
    average = total/3
    
    #리스트박스에 입력데이터들 + 총점 + 평균데이터를 추가.
    listbox_result.insert(END,f'{name},{kor},{eng},{math},{total},{average}') 
    # END : 마지막 위치에 새로 추가

    clicked_reset()
    

def clicked_reset():
    #Entry 요소에 써있는 글씨 모두 삭제
    entry_name.delete(0,END) # 0번 글씨부터 end 까지 지움
    entry_kor.delete(0,END)
    entry_eng.delete(0,END)
    entry_math.delete(0,END)
    


def clicked_delete():
    #리스트 박스에서 선택한 항목의 위치번호 알아야 삭제 가능
    index = listbox_result.curselection() # current selection : 현재 선택된 항목의 인덱스 번호를 튜플로 줌
    print(index)
    listbox_result.delete(index[0])#선택항목이 한개뿐이어서(튜플의 첫번째에 선택한 번호가 있으니 그거 지움)



import csv

def cliecked_save():
    #저정할 모든 데이터를 리스트박스에서 가져오기 
    all_items = listbox_result.get(0,END) # 0번줄 부터 끝까지.. 
    print(all_items)
    #튜플로 되어 있는 각 줄의 데이터를 csv 파일로 저장하기. csv 전용 표준모듈이 존재함.
    with open("files/grades.csv",'w',encoding='utf-8') as file:
        writer=csv.writer(file)
        
        for row in all_items:
            writer.writerow(row.split(',')) #한줄 문자열을, 단위로 분리하여 리스트[]로 만들어 csv파일에 저장







#------------------------------------------------------------------------------




#[0]. tkinter 모듈 추가
from tkinter import *

#[1] 화면부터 구성
window=Tk()
window.title('성적처리 프로그램')
window.resizable(False,True)
window.geometry('400x500-200+50')

#[2] [이름,국어,영어,수학] 성적을 입력하기 위젯만들기 
frame1=Frame(window,padx=10,pady=10) #여백
frame1.pack(fill='x')

label_name = Label(frame1,text='이름',font=('',14,)) #글꼴,글자크기,
label_name.grid(row=0,column=0,padx=10,pady=10)
entry_name = Entry(frame1,font=("",12),width=15) # 15칸 정도 사이즈
entry_name.grid(row=0,column=1,padx=10,pady=10)

label_kor = Label(frame1,text='국어',font=('',14,)) #글꼴,글자크기,
label_kor.grid(row=1,column=0,padx=10,pady=10)
entry_kor = Entry(frame1,font=("",12),width=15) # 15칸 정도 사이즈
entry_kor.grid(row=1,column=1,padx=10,pady=10)

label_eng = Label(frame1,text='영어',font=('',14,)) #글꼴,글자크기,
label_eng.grid(row=2,column=0,padx=10,pady=10)
entry_eng = Entry(frame1,font=("",12),width=15) # 15칸 정도 사이즈
entry_eng.grid(row=2,column=1,padx=10,pady=10)

label_math = Label(frame1,text='수학',font=('',14,)) #글꼴,글자크기,
label_math.grid(row=3,column=0,padx=10,pady=10)
entry_math = Entry(frame1,font=("",12),width=15) # 15칸 정도 사이즈
entry_math.grid(row=3,column=1,padx=10,pady=10)

frame2=Frame(window,padx=10,pady=10) #여백
frame2.pack(fill='x')
btn_complete = Button(frame2,text='입력완료', font=('Gungsuh',14),command=clicked_complete)
btn_complete.pack(side='left',padx=10,pady=10)
btn_reset = Button(frame2,text='입력취소',font=('Gungsuh',14),command=clicked_reset)
btn_reset.pack(side='right',padx=10,pady=10)

#[4]. 리스트박스, 항목삭제버튼, csv 파일 저장 버튼을 구성하는 영역

frame3=Frame(window,padx=10,pady=10) #여백
frame3.pack(fill='x')
listbox_result=Listbox(frame3,font=('',12),height=5)
listbox_result.pack(fill='x')

btn_del = Button(frame3,text='항목삭제', font=('Batang',14),command=clicked_delete)
btn_del.pack(side='left', pady=10)
btn_save = Button(frame3,text='csv 파일 저장', font=('Batang',14),command=cliecked_save)
btn_save.pack(side='right', pady=10)







window.mainloop()
