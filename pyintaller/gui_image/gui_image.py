#pyinstaller 를 사용할때 모듈을 이용하여 실행파일을 만들면 기존에 사용하던 상대경로가 틀어짐
#파이썬만의 특정 폴더 영역으로 리소스(이미지,동영상 등등 파일들)위치한 후 동작함. 
#그래서 코드에서.. 이 경로를 기반으로 리소스의 경로를 지정해야 함. 

import sys
import os

#상대경로를 파라미터로 받아서 리소스용 경로를 만들어주는 기능함수를 미리 정의

def resource_path(path):
    try:
        base_path=sys._MEIPASS
    except:
        base_path=os.path.abspath('./') # ./ 현재 폴더를 말하는 기호
 
    #2개의 경로를 합성해주는 기능
    return os.path.join(base_path,path)



from tkinter import *



window=Tk()

img=PhotoImage(file=resource_path('gui_image/resources/image/bazzi.png'))
label=Label(window,image=img)
label.pack()

window.mainloop()