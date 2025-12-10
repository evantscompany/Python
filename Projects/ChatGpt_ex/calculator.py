from tkinter import *
from PIL import Image,ImageTk

window=Tk()
window.title="계산기"
window.geometry('500x500')
frame_01=Frame(window,padx=10,pady=10,bg="blue")
frame_01.pack(fill='x')


img=Image.open("Projects/images/ms/bazzi.png")
tk_img=ImageTk.PhotoImage(img)
tk_img=tk_img.resize()

label_main=Label(frame_01,text='표준',font=("",14))
label_main.pack(side='left')
label_screen=Label(frame_01,image=tk_img,width=30,height=30)
label_screen.pack(side='left')





window.mainloop()
