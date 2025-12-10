import pandas as pd
from tkinter import *
from tkinter import filedialog,messagebox

df=None
sheet_names=[]
current_sheet=None



window = Tk()
window.title('Excel Viewer Plus')
window.geometry("800x600")

frame_entry = Frame(window)
frame_entry.pack(fill='x',padx=10,pady=10)

# 파일 경로 entry
entry = Entry(frame_entry, width=60)
entry.pack(pady=10,padx=10,side='left',fill='x')

def choose_file():
    file_path = filedialog.askopenfilename(title="엑셀 파일 선택", filetypes=[("Excel Files","*.xlsx *.xls")])
    if file_path:
        entry.delete(0,END)
        entry.insert(0,file_path)

btn_choose = Button(frame_entry,text='파일선택',command=choose_file)
btn_choose.pack(pady=10,padx=10,side="left")

def read_file():
    global df
    file_path = entry.get()
    if not file_path:
        messagebox.showerror('오류','파일을 선택하세요')
        return

    try:    
        df= pd.read_excel(file_path,sheet_name=None)
        messagebox.showinfo("성공",f"{len(df)}개 시트가 로드되었습니다.")
    except Exception as e:
        messagebox.showerror("읽기 오류",str(e))

btn_read = Button(frame_entry, text='파일 읽기',command=read_file)
btn_read.pack(side='left',padx=5)



window.mainloop()


