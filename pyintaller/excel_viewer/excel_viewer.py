#tkinter file choice and Viewer 기능

# 기능 요구
# 1. 파일선택 버튼을 누르면 excel 파일을 선택할 수 있어야함. 
# 2. 선택한 파일경로는 Entry 요소에 보여야 함 (파이썬에서는 위젯)
# 3. '파일읽기' 버튼을 누르면 해당 경로의 엑셀파일을 pandas 로 읽어야 함. 
# 4. '그래프보기'버튼을 누르면 숫자데이터 선그래프로 보여야함.
# 5. '엑셀데이터보기' 버튼을 누르면 다시 표 형태의 데이터가 보여야 함. 


#7.1전역변수 선언 --- 이 .py 파일 어디서든 인식이 가능한 변수
df=None #엑셀파일을 판다스로 읽어서 표 형태로 데이터를 가지고 있는 객체 참조변수
figure_canvas = None


#-----------------------------------------------------------------
# 버튼 클릭시 실행된 코드가 작성된 영역(함수, function 기능) 정의

#6.파일선택버튼클릭시 동작할 기능코드(함수)
def clicked_file_chooser():
    #윈도우 탐색기처럼 사용자가 마우스로 파일을 선택할 수 있도록 하는 [파일선택기]를 띄우기.
    #[tkinter 모듈안에 하위모듈로 filedialog]를 이용
    file_path=filedialog.askopenfilename(title='엑셀 파일 선택',filetypes=[('엑셀파일','*.xlsx *xls'),('모든파일','*.*')])
    if file_path:
        #기존 Entry 에 이미 이전 경로명이 써 있을 수도 있기에 먼저 제거.
        entry.delete(0,END)
        #사용자가 선택한 새로운 파일경로를 첫번째 자리부터 작성하기
        entry.insert(0, file_path)

#7.파일 읽기 버튼 클릭시 동작할 기능코드(함수)
def clicked_file_reader():  
    #이 함수 안에서 df를 사용하면 이는 전역변수임을 명시 !!
    global df

    #선택한 파일의 경로를 entry 로 부터 얻어오기
    file_path= entry.get()
    #선택된 경로가 없는데 읽으라고 하면..?file_path경로에 실제 파일이 있는지 확인하기 위해 os 모듈 사용
    if not os.path.exists(file_path):
        messagebox.showerror('파일 읽기 오류','파일을 찾을 수가 없습니다')
        #에러가 났으니, 더이상 파일읽기 기능을 수행할 필요가 없으므로.. 이 함수의 동작을 멈춤
        return
    #파일이 존재하는 상태이므로, pandas를 이용하여 file_path의 엑셀파일을 읽어서 DataFrame으로 만들기

    df = pd.read_excel(file_path)
    
    #잘 읽어졌는지 콘솔창에 출력해보기
    
    figure_canvas=None # 그래프 그려지는 도화지 위젯

    #데이터가 확인 되었으니, GUI 위젯으로 데이터들 보여주기.. 이 작업이 좀 복잡할 것임.
    #그래서 이 위치에 작성하면 지저분해 질듯..
    #또한 [엑셀데이터 보기]버튼이 클릭되었을때도 이 df를 보여주는 작업을 해야함. 즉 같은 기능을 다시 수행
    #그래서 이 작업을 별도의 함수에서 수행
    




#8. show_data 함수를 정의 - 데이터프레임의 데이터를 treeview에 표형태로 보여주기
def show_data():
    
    #데이터프레임에 데이터가 있는지 확인
    global figure_canvas
    global df
    if df is None:
        return
    
    #그래프가 그려진 FigureCanvasTkAgg 가 파괴되지 않음.
    global figure_canvas
    if figure_canvas is not None:
        figure_canvas.get_tk_widget().destroy()
        figure_canvas=None    
    
    #treeview에 표를 만들기 위해 컬룸들을 설정
    #기존에 있던 표를 제거
    treeview.delete(*treeview.get_children()) 
    
    #delete()은 삭제할 자식들을 ,,,,로 여러개를 지정함. 리스트로 한방에 지정불가,
    # 근데 get_children 기능이 리스트로 줌
    # 그래서 언패킹 연산자 (*) 사용



    #treeview 에 표를 만들기 위해 컬룸들을 설정 -- 표만들기 --
    treeview['column'] = list(df.columns)
    treeview['show'] = 'headings' # 컬룸 제목이 표시되어야 함을 설정

    #표안에 제목줄 작성
    for col in df.columns:
        treeview.heading(col,text=col) # 첫번째 파라미터인 col 에게 보여질 글씨 지정. 
        treeview.column(col,width=120) # col 너비 지정

    #표 안에 데이터들 작성
    for idx,row in df.iterrows(): 
        treeview.insert('','end',values=list(row))
        #'' : 최상위 레벨(parent)
        #'end' :  기존 데이터가 추가된 다음 줄에 추가 
        #values : 컬룸별 데이터 값 지정


#9. show_graph 함수를 정의 - 데이터프레임의 데이터를 treeview에 그래프로 보여주기
def show_graph():
    global df
    if df is None:
        return
    
    #그래프가 treeview에 그려져야 하기에.. 기존에 추가되어 있던 컬룸들을 모두 제거. 

    treeview.delete(*treeview.get_children())

    #시각화를 위한 그래프용 모듈 추가 matplotlib
    #1) x축에 보여줄 데이터와 라벨들 준비 -- 일반적으로는 첫번째 column에 있는 경우가 많음. 

    xs=df.iloc[:,0]
    xs_label = df.columns[0]

    #y축에 그려질 데이터들이 준비 - 그래프이기에 숫자 데이터들만 그려짐. 
    #데이터프레임(df)에서 숫자타입의 데이터를 가진 컬룸들만 뽑아서 다시 데이터 프레임 만들기

    numeric_df=df.select_dtypes(include=['int64','float64'])
    print(numeric_df)

    #혹시 숫자데이터 컬룸이 없으면 그래프는 못보여줌

    if numeric_df.empty:
        messagebox.showwarning("경고", '그래프를 그릴 수 있는 숫자 컬룸이 없습니다. ')
        return
    
    #숫자데이터들을 선 그래프에 표시하기.

    figure=plt.figure(figsize=(10,6))
    
    for col in numeric_df.columns:
        if col == xs_label:
            continue

        #x축 값, y축 값들로 선 그래프 그리기
        plt.plot(xs, numeric_df[col], label=col, marker='o')

    plt.xlabel(xs_label)
    plt.ylabel('값들')
    plt.title('엑셀 데이터 그래프')
    plt.legend() #범례표시
    plt.grid(True) # 격자 눈금
    # plt.show()

    #그래프를 tkinter의 treeview 안에 넣기 위해 그래프 그리는 전용 위젯 필요 
    #FigureCanvasTkAgg
    global figure_canvas
    if figure_canvas is None:

        figure_canvas = FigureCanvasTkAgg(figure=figure,master=treeview)
        figure_canvas.get_tk_widget().pack()

    
    
 






#-----------------------------------------------------------------




#0. 필요한 라이브러리 추가. 

from tkinter import * #모든건, 변수, 클래스, 함수 까지만 가져옴. 하위 모듈은 따로 또 불러야댐
from tkinter import filedialog,messagebox,ttk
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



#그래프에 한글 깨지는 이유.. 한글 글꼴 아니어서. 

plt.rcParams['font.family'] = 'Malgun Gothic'




#1. 최상위 윈도우 위젯 만들기

window=Tk()
window.title("엑셀 파일 뷰어")
window.geometry('800x600-100+50')

#2.파일 선택 영역 Frame
frame_top=Frame(window)
frame_top.pack(fill='x',padx=10,pady=5)

#3.파일 경로를 직접 입력하거나 선택된 파일 경로가 보여지는 Entry 위젯

entry=Entry(frame_top, width=60)
entry.pack(side='left',padx=5,pady=5)

#4.파일선택버튼
btn_file_chooser = Button(frame_top,text='파일선택',command=clicked_file_chooser)
btn_file_chooser.pack(side='left',padx=5)

#5.파일읽기버튼
btn_file_reader = Button(frame_top,text="파일읽기",command=clicked_file_reader)
btn_file_reader.pack(side="left",padx=5)

#--------------------------------------------------------------------

#8.1 [엑셀데이터 보기] [그래프 보기] 버튼으로 데이터를 보여주기 위한 위젯들..

#위 파일선택영영과 시각적으로 구분하기 위해 구분선 위젯(separator) 사용.. 
# 이 위젯은 tkinter안에 ttk하위모듈에 있음.
separator=ttk.Separator(window,orient='horizontal') # 수평선
separator.pack(fill='x', pady=10)

#버튼 2개 배치

frame_buttons=Frame(window)
frame_buttons.pack(anchor='center')


btn_show_data=Button(frame_buttons,text="엑셀데이터 보기",command=show_data)
btn_show_data.pack(side='left',padx=10)
btn_show_graph=Button(frame_buttons,text="그래프 보기",command=show_graph)
btn_show_graph.pack(side='left',padx=10)

#8.2 표 형태의 데이터와 그래프를 번갈아 보여줄 수 있어야 하기에 ttk.treeview이용
#자식요소들을 제거했다가 추가했다가. 

treeview= ttk.Treeview(window)
treeview.pack(expand=True,fill='both',padx=10,pady=10)


window.mainloop()




