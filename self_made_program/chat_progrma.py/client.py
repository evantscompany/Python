import socket
import threading
from tkinter import *
from tkinter import simpledialog, messagebox

# -------------------------------
# 서버 IP 입력 받기
# -------------------------------
SERVER_IP = simpledialog.askstring("서버 IP", "서버 IP를 입력하세요:")
SERVER_PORT = 5000

# TCP 소켓 생성
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((SERVER_IP, SERVER_PORT))  # 서버에 연결
except:
    messagebox.showerror("연결 오류", "서버에 연결할 수 없습니다.")
    exit()

# -------------------------------
# GUI 생성
# -------------------------------
window = Tk()
window.title("LAN 채팅 프로그램")
window.geometry("500x500")

# 메시지 출력창 (읽기 전용)
chat_box = Text(window, state=DISABLED)
chat_box.pack(expand=True, fill=BOTH, padx=10, pady=10)

# 메시지 입력창 + 전송 버튼 프레임
entry_frame = Frame(window)
entry_frame.pack(fill=X, padx=10, pady=5)

entry = Entry(entry_frame)
entry.pack(side=LEFT, expand=True, fill=X, padx=(0,5))
entry.focus()  # 커서 활성화

# -------------------------------
# 메시지 출력 함수
# -------------------------------
def add_message(msg):
    chat_box.config(state=NORMAL)  # 읽기 전용 해제
    chat_box.insert(END, msg + "\n")  # 메시지 추가
    chat_box.config(state=DISABLED)  # 다시 읽기 전용
    chat_box.see(END)                 # 항상 마지막 메시지 보이기

# -------------------------------
# 메시지 전송 함수
# -------------------------------
def send_msg(event=None):  # 엔터 입력 시 호출 가능
    msg = entry.get()
    if msg:
        try:
            client.send(msg.encode("utf-8"))  # 서버로 메시지 전송
            add_message(f"[나] {msg}")        # 내 메시지 화면에 표시
            entry.delete(0, END)              # 입력창 초기화
        except:
            messagebox.showerror("전송 오류", "메시지를 보낼 수 없습니다.")

# 전송 버튼
btn_send = Button(entry_frame, text="전송", width=10, command=send_msg)
btn_send.pack(side=RIGHT)

# -------------------------------
# 서버로부터 메시지 수신 스레드
# -------------------------------
def receive_msg():
    while True:
        try:
            msg = client.recv(1024).decode("utf-8")
            if msg:
                add_message(f"[상대] {msg}")  # 수신 메시지 화면에 표시
        except:
            break

# 메시지 수신용 스레드 실행
threading.Thread(target=receive_msg, daemon=True).start()

# -------------------------------
# 엔터 키 입력으로 메시지 전송
# -------------------------------
entry.bind("<Return>", send_msg)

# GUI 이벤트 루프 실행
window.mainloop()