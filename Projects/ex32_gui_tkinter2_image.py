from tkinter import *

# 이미지를 보여주는 위젯은 없음. 대신 label 위젯에 text='' 대신 image=''로 이미지를 보여줌

window=Tk()

#이미지 파일의 경로를 써야 해서... 
#이미지 파일을 읽어서 파이썬에서 사용할 수 있는 객체로 만들어주는 클래스를 이용
img= PhotoImage(file='Projects/images/ms/ms18.png').subsample(2)
label=Label(window,image=img)
label.pack()


#jpg 이미지를 보여주고 싶다면, 외부 라이브러리 추가 (pillow [ PIL 파이썬 이미지 라이브러리의 후속판])
#설치 pip install pillow

#pillow library 사용

from PIL import Image,ImageTk 
# image : 이미지 객체 , imagetk : tkinter에서 PIL image를 사용할수 있도록 해줌

#PIL 를 이용하여 이미지 파일을 불러오기 

pil_img= Image.open('Projects/images/paris.jpg')
#이미지 사이즈 변경 가능
pil_img=pil_img.resize((300,200),Image.LANCZOS) # 튜풀 타입으로(너비,높이),LANCZOS 사이즈 조절시 이미지 품질
#pil_image를 Label 위젯에서 인식하지 못함. 그래서 변환
img2=ImageTk.PhotoImage(pil_img)
#이미지를 보여주는 Label 객체 생성하면 이미지를 설정

label2=Label(window,image=img2)
label2.pack()

#버튼 클릭시에 이미지를 변경해보기.
#버튼 클릭할때 변경할 이미지도 미리 만들어놓기

pil_img=Image.open('Projects/images/newyork.jpg')
pil_img=pil_img.resize((300,200), Image.LANCZOS)
img3=ImageTk.PhotoImage(image=pil_img)

def aaa():
    img=label2.cget('image')
    if img==str(img2):
        label2.configure(image=img3)
    else:
        label2.configure(image=img2)



    

btn = Button(window,text="change image",command=aaa)
btn.pack()


window.mainloop()
