# ---------------------------------------------
# 필요한 라이브러리
# ---------------------------------------------
import pandas as pd
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import os

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

import pyttsx3
from PIL import Image, ImageTk

# 한글 폰트 설정
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

EXCEL_FILE = 'Projects/medical_data/aaa.xlsx'
SHEET_NAME = 'TreatmentPlan'
FONT_MAIN = ('Malgun Gothic', 12)
FONT_BOLD = ('Malgun Gothic', 12, 'bold')
FONT_HEADER = ('Malgun Gothic', 16, 'bold')


# =============================================
# 엑셀 읽기/쓰기
# =============================================
def load_patient_data(file_path):
    try:
        df = pd.read_excel(file_path, sheet_name=SHEET_NAME)
        df.set_index('Patient_ID', inplace=True)
        return df
    except FileNotFoundError:
        messagebox.showerror("오류", f"엑셀 파일 '{file_path}'을 찾을 수 없습니다.")
        return None
    except Exception as e:
        messagebox.showerror("오류", f"엑셀 로드 오류: {e}")
        return None

def save_patient_data(df, file_path):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with pd.ExcelWriter(file_path, engine="openpyxl",
                            mode="a", if_sheet_exists='replace') as writer:
            df.to_excel(writer, sheet_name=SHEET_NAME)
        messagebox.showinfo("저장 완료", "환자 정보가 성공적으로 업데이트되었습니다.")
    except Exception as e:
        messagebox.showerror("오류", f"파일 저장 중 오류 발생: {e}")


# =============================================
# GUI 클래스
# =============================================
class PatientGuideApp:

    def __init__(self, master):
        self.master = master
        master.title("🏥 대가연 통증 클리닉 진료 안내 시스템")
        master.geometry("1000x900")  

        self.create_menu()

        self.df = load_patient_data(EXCEL_FILE)
        if self.df is None:
            master.quit()
            return

        self.current_patient_id = tk.StringVar()
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', 150)
        self.tts_engine.setProperty('volume', 1.0)

        self.patient_photo = None

        self.setup_ui()

        # 엔터키 검색 연결
        self.master.bind("<Return>", lambda event: self.search_patient())

    # --------------------------
    # 메뉴바
    # --------------------------
    def create_menu(self):
        menubar = tk.Menu(self.master)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="열기", command=self.menu_placeholder)
        file_menu.add_command(label="저장", command=self.menu_placeholder)
        file_menu.add_separator()
        file_menu.add_command(label="종료", command=self.master.quit)
        menubar.add_cascade(label="파일", menu=file_menu)

        prog_menu = tk.Menu(menubar, tearoff=0)
        prog_menu.add_command(label="프로그램 정보", command=self.menu_placeholder)
        menubar.add_cascade(label="프로그램", menu=prog_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="도움말", command=self.menu_placeholder)
        menubar.add_cascade(label="도움말", menu=help_menu)

        self.master.config(menu=menubar)

    def menu_placeholder(self):
        messagebox.showinfo("안내", "이 기능은 아직 구현되지 않았습니다.")

    # --------------------------
    # UI 구성
    # --------------------------
    def setup_ui(self):
        main_frame = ttk.Frame(self.master)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # 좌: 정보+그래프 / 우: 환자 리스트
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side="left", fill="both", expand=True)

        right_frame = ttk.Frame(main_frame, width=300)
        right_frame.pack(side="right", fill="y")

        # =======================
        # 검색 영역
        # =======================
        frame_search = ttk.Frame(left_frame, padding="15 10 15 10")
        frame_search.pack(fill='x')
        ttk.Label(frame_search, text="환자 ID 검색", font=FONT_HEADER).pack(pady=5)
        ttk.Label(frame_search, text="환자 ID:", font=FONT_MAIN).pack(side='left', padx=5)
        self.id_entry = ttk.Entry(frame_search, font=FONT_MAIN, width=15)
        self.id_entry.pack(side='left', padx=10)
        ttk.Button(frame_search, text="검색", command=self.search_patient).pack(side='left', padx=10)

        ttk.Separator(left_frame).pack(fill='x', pady=5)

        # =======================
        # 환자 정보 + 사진 영역
        # =======================
        info_photo_frame = ttk.Frame(left_frame)
        info_photo_frame.pack(fill='both', expand=True)

        # 좌: 텍스트 정보
        self.info_frame = ttk.Frame(info_photo_frame)
        self.info_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # 우: 사진
        self.photo_frame = ttk.Frame(info_photo_frame, width=300)
        self.photo_frame.pack(side="right", fill="y", padx=5, pady=5)
        ttk.Label(self.photo_frame, text="환자 사진", font=("Malgun Gothic", 14, "bold")).pack(pady=5)
        self.photo_label = ttk.Label(self.photo_frame)
        self.photo_label.pack(pady=10)
        ttk.Button(self.photo_frame, text="🖼️ 사진 업로드", command=self.upload_patient_photo).pack(pady=5)

        # =======================
        # 정보 레이블
        # =======================
        self.info_labels = {}
        info_keys = [
            ("환자명", "Name"),
            ("전화번호", "Phone_Number"),
            ("진단명", "Diagnosis"),
            ("총 회차", "Total_Sessions"),
            ("현재 회차", "Current_Session"),
            ("금일 치료", "Treatment_Type_Cur"),
            ("금일 주의사항", "Today_Instructions"),
            ("다음 권장일", "Next_Visit_Date"),
            ("다음 치료", "Next_Treatment")
        ]
        for label_text, key in info_keys:
            row = ttk.Frame(self.info_frame)
            row.pack(fill='x', pady=5)
            ttk.Label(row, text=f"• {label_text}:", font=FONT_BOLD, width=15, anchor='w').pack(side='left')
            lbl = ttk.Label(row, text="---", font=FONT_MAIN, wraplength=400, justify='left', anchor='w')
            lbl.pack(side='left', fill='x', expand=True)
            self.info_labels[key] = lbl

        # -------------------------
        # TTS / 전화 / 문자
        # -------------------------
        button_frame = ttk.Frame(self.info_frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="📞 전화 걸기", command=self.call_phone_placeholder).pack(side='left', padx=5)
        ttk.Button(button_frame, text="📩 문자 보내기", command=self.send_sms_placeholder).pack(side='left', padx=5)
        ttk.Button(button_frame, text="🔊 정보 읽어주기", command=self.read_patient_info_tts).pack(side='left', padx=5)

        ttk.Separator(left_frame).pack(fill='x', pady=5)

        # =======================
        # 그래프 영역
        # =======================
        self.frame_graph = ttk.Frame(left_frame, padding="10")
        self.frame_graph.pack(fill='both', expand=True)

        # 회차 업데이트 버튼
        self.update_button = ttk.Button(left_frame, text="⭐ 진료 완료 및 회차 업데이트",
                                        command=self.update_session, state=tk.DISABLED, padding="10 10")
        self.update_button.pack(pady=10)

        # =======================
        # 오른쪽 환자 목록
        # =======================
        ttk.Label(right_frame, text="📋 환자 목록", font=FONT_HEADER).pack(pady=10)
        canvas = tk.Canvas(right_frame)
        scrollbar = ttk.Scrollbar(right_frame, orient="vertical", command=canvas.yview)
        self.patient_list_frame = ttk.Frame(canvas)
        self.patient_list_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.patient_list_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.build_patient_list_buttons()

    # =======================
    # 환자 목록 버튼
    # =======================
    def build_patient_list_buttons(self):
        for widget in self.patient_list_frame.winfo_children():
            widget.destroy()
        for pid, row in self.df.iterrows():
            btn = ttk.Button(self.patient_list_frame, text=f"{row['Name']} ({pid})", width=30,
                             command=lambda p=pid: self.load_patient_by_button(p))
            btn.pack(pady=2)

    def load_patient_by_button(self, patient_id):
        self.id_entry.delete(0, tk.END)
        self.id_entry.insert(0, patient_id)
        self.search_patient()

    # =======================
    # 환자 검색
    # =======================
    def search_patient(self):
        patient_id = self.id_entry.get().strip().upper()
        self.current_patient_id.set(patient_id)
        if patient_id not in self.df.index:
            messagebox.showerror("검색 실패", f"ID '{patient_id}' 환자 정보를 찾을 수 없습니다.")
            self.clear_info()
            return
        info = self.df.loc[patient_id]
        next_visit = self.calculate_next_visit(info)
        self.update_info_labels(info, next_visit)
        self.draw_prediction_graph(info)
        if info['Current_Session'] < info['Total_Sessions']:
            self.update_button.config(state=tk.NORMAL)
        else:
            self.update_button.config(state=tk.DISABLED)
            messagebox.showinfo("안내", "모든 계획된 치료가 완료되었습니다.")

    # =======================
    # 레이블 갱신
    # =======================
    def update_info_labels(self, info, next_date_str):
        for key in self.info_labels:
            if key in info:
                if key == "Total_Sessions" or key == "Current_Session":
                    self.info_labels[key].config(text=f"{info[key]}회차")
                else:
                    self.info_labels[key].config(text=info[key])
        self.info_labels["Next_Visit_Date"].config(text=next_date_str)

    # =======================
    # 사진 업로드
    # =======================
    def upload_patient_photo(self):
        file_path = filedialog.askopenfilename(title="환자 사진 선택",
                                               filetypes=[("이미지 파일", "*.png;*.jpg;*.jpeg;*.bmp")])
        if not file_path:
            return
        img = Image.open(file_path)
        img.thumbnail((300, 300))
        self.patient_photo = ImageTk.PhotoImage(img)
        self.photo_label.config(image=self.patient_photo)

    # =======================
    # 전화/문자 자리표시
    # =======================
    def call_phone_placeholder(self):
        messagebox.showinfo("안내", "전화 걸기 기능은 향후 구현 예정입니다.")
    def send_sms_placeholder(self):
        messagebox.showinfo("안내", "문자 보내기 기능은 향후 구현 예정입니다.")

    # =======================
    # TTS
    # =======================
    def read_patient_info_tts(self):
        patient_id = self.current_patient_id.get()
        if not patient_id:
            messagebox.showwarning("경고", "환자를 먼저 검색하세요.")
            return
        info = self.df.loc[patient_id]
        text = f"{info['Name']} 님의 진단명은 {info['Diagnosis']} 입니다. "
        text += f"총 치료 회차는 {info['Total_Sessions']}회차이며, 현재 {info['Current_Session']}회차입니다. "
        text += f"금일 치료는 {info['Treatment_Type_Cur']}이며, 주의사항은 {info['Today_Instructions']} 입니다. "
        text += f"다음 권장일은 {self.info_labels['Next_Visit_Date'].cget('text')} 입니다. "
        text += f"다음 치료는 {info['Next_Treatment']} 입니다."
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    # =======================
    # 다음 방문일 계산
    # =======================
    def calculate_next_visit(self, info):
        try:
            days = int(info['Next_Visit_Days'])
            next_day = datetime.now() + timedelta(days=days)
            return next_day.strftime(f"%Y년 %m월 %d일 ({days}일 후)")
        except:
            return "[오류] 날짜 정보 잘못됨"

    # =======================
    # 초기화
    # =======================
    def clear_info(self):
        for label in self.info_labels.values():
            label.config(text="---")
        self.update_button.config(state=tk.DISABLED)
        if hasattr(self, "canvas"):
            self.canvas.get_tk_widget().destroy()
        if self.photo_label:
            self.photo_label.config(image="")

    # =======================
    # 그래프
    # =======================
    def draw_prediction_graph(self, info):
        if hasattr(self, "canvas"):
            self.canvas.get_tk_widget().destroy()
        total = int(info['Total_Sessions'])
        current = int(info['Current_Session'])
        x = np.arange(1, total + 1)
        y = np.exp(-0.25 * (x - 1))
        current_y = y[current - 1]
        fig, ax = plt.subplots(figsize=(5, 3), dpi=100)
        ax.plot(x, y, marker='o', label='예상 통증 감소')
        ax.scatter([current], [current_y], color='red', s=80, label='현재 회차')
        ax.set_title(f"{info['Name']} 님 치료 개선 예상 그래프")
        ax.set_xlabel("치료 회차")
        ax.set_ylabel("예상 통증 지수")
        ax.grid(True)
        ax.legend()
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame_graph)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(pady=10)

    # =======================
    # 회차 업데이트
    # =======================
    def update_session(self):
        patient_id = self.current_patient_id.get()
        if not patient_id:
            messagebox.showwarning("경고", "환자를 먼저 검색하세요.")
            return
        name = self.df.loc[patient_id, 'Name']
        if not messagebox.askyesno("확인", f"{name} 님의 진료 회차를 업데이트할까요?"):
            return
        self.df.loc[patient_id, 'Current_Session'] += 1
        save_patient_data(self.df, EXCEL_FILE)
        self.search_patient()


# =============================================
# 메인
# =============================================
if __name__ == "__main__":
    root = tk.Tk()
    app = PatientGuideApp(root)
    root.mainloop()
