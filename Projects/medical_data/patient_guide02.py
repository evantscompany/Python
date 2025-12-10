import pandas as pd
from datetime import datetime, timedelta
import tkinter as tk # GUI 라이브러리 임포트
from tkinter import messagebox, ttk # 메시지 박스와 ttk(테마 위젯) 임포트
import os

# --- 설정 변수 ---
# 엑셀 파일 경로 설정 (스크립트가 실행되는 곳을 기준으로 경로 설정)
EXCEL_FILE = 'Projects/medical_data/aaa.xlsx' 
SHEET_NAME = 'TreatmentPlan'
FONT_MAIN = ('Malgun Gothic', 12)
FONT_BOLD = ('Malgun Gothic', 12, 'bold')
FONT_HEADER = ('Malgun Gothic', 16, 'bold')


# --- 데이터 로드/저장 함수 (기존 로직 유지) ---

def load_patient_data(file_path):
    """엑셀 파일을 읽어와 Patient_ID를 인덱스로 설정한 DataFrame 반환"""
    try:
        # 엑셀 파일 로드 및 인덱스 설정
        df = pd.read_excel(file_path)
        df.set_index('Patient_ID', inplace=True)
        return df
    except FileNotFoundError:
        messagebox.showerror("오류", f"엑셀 파일 '{file_path}'을(를) 찾을 수 없습니다. 경로를 확인해 주세요.")
        return None
    except Exception as e:
        messagebox.showerror("오류", f"엑셀 파일 로드 중 문제가 발생했습니다: {e}")
        return None

def save_patient_data(df, file_path):
    """업데이트된 DataFrame을 엑셀 파일에 저장"""
    try:
        # 변경된 DataFrame을 엑셀 파일에 덮어쓰기 저장
        df.to_excel(file_path, sheet_name=SHEET_NAME, index=True) 
        messagebox.showinfo("저장 완료", "✅ 환자의 진료 정보가 성공적으로 업데이트되었습니다.")
    except Exception as e:
        messagebox.showerror("오류", f"파일 저장 중 문제가 발생했습니다. 엑셀 파일이 열려있는지 확인해 주세요. 오류: {e}")


# --- GUI 메인 로직 클래스 ---

class PatientGuideApp:
    def __init__(self, master):
        self.master = master
        master.title("🏥 대가연 통증 클리닉 진료 안내 시스템")
        master.geometry("600x650") # 윈도우 크기 설정
        
        # 엑셀 데이터 로드 시도
        self.df = load_patient_data(EXCEL_FILE)
        if self.df is None:
            master.quit() # 데이터 로드 실패 시 프로그램 종료
            return

        # 현재 검색된 환자 정보를 저장할 변수
        self.current_patient_id = tk.StringVar()
        
        # --- UI 구성 ---
        self.setup_ui()

    def setup_ui(self):
        """GUI 위젯(Widgets) 레이아웃 설정"""
        
        # 1. 상단 검색 영역 (Frame 1)
        frame_search = ttk.Frame(self.master, padding="15 10 15 10")
        frame_search.pack(fill='x')
        
        ttk.Label(frame_search, text="환자 ID 검색", font=FONT_HEADER).pack(pady=5)
        
        # ID 입력 필드
        ttk.Label(frame_search, text="환자 ID:", font=FONT_MAIN).pack(side='left', padx=5)
        self.id_entry = ttk.Entry(frame_search, font=FONT_MAIN, width=15)
        self.id_entry.pack(side='left', padx=10)
        
        # 검색 버튼
        ttk.Button(frame_search, text="검색", command=self.search_patient).pack(side='left', padx=10)

        ttk.Separator(self.master).pack(fill='x', pady=5)
        
        # 2. 정보 출력 영역 (Frame 2)
        frame_info = ttk.Frame(self.master, padding="15")
        frame_info.pack(fill='both', expand=True)

        ttk.Label(frame_info, text="✅ 환자 정보 및 치료 계획", font=FONT_HEADER).pack(pady=10)
        
        # 정보를 담을 레이블들을 딕셔너리로 저장
        self.info_labels = {}
        info_keys = [
            ("환자명", "Name"), ("진단명", "Diagnosis"), ("총 회차", "Total_Sessions"), 
            ("현재 회차", "Current_Session"), ("금일 치료", "Treatment_Type_Cur"), 
            ("금일 주의사항", "Today_Instructions"), ("다음 권장일", "Next_Visit_Date"), 
            ("다음 치료", "Next_Treatment")
        ]
        
        for label_text, key in info_keys:
            frame_row = ttk.Frame(frame_info)
            frame_row.pack(fill='x', pady=5)
            
            # 제목 레이블 (굵게)
            ttk.Label(frame_row, text=f"• {label_text}:", font=FONT_BOLD, width=15, anchor='w').pack(side='left', padx=5)
            
            # 내용을 출력할 레이블
            info_label = ttk.Label(frame_row, text="---", font=FONT_MAIN, anchor='w')
            info_label.pack(side='left', fill='x', expand=True)
            self.info_labels[key] = info_label

        ttk.Separator(self.master).pack(fill='x', pady=5)

        # 3. 업데이트 버튼 영역 (Frame 3)
        self.update_button = ttk.Button(self.master, 
                                        text="⭐ 진료 완료 및 회차 업데이트", 
                                        command=self.update_session,
                                        state=tk.DISABLED, # 처음에는 비활성화
                                        padding="10 10")
        self.update_button.pack(pady=20)


    def search_patient(self):
        """검색 버튼 클릭 시 호출되는 함수"""
        patient_id = self.id_entry.get().strip().upper()
        self.current_patient_id.set(patient_id) # 현재 ID 저장
        
        # 데이터프레임 인덱스에 ID가 있는지 확인
        if patient_id not in self.df.index:
            messagebox.showerror("검색 실패", f"ID '{patient_id}'에 해당하는 환자 정보를 찾을 수 없습니다.")
            self.clear_info()
            return
        
        patient_info = self.df.loc[patient_id]
        
        # 다음 방문일 계산
        next_visit_date_str = self.calculate_next_visit(patient_info)
        
        # GUI 레이블에 정보 업데이트
        self.update_info_labels(patient_info, next_visit_date_str)
        
        # 업데이트 버튼 활성화/비활성화
        if patient_info['Current_Session'] < patient_info['Total_Sessions']:
            self.update_button.config(state=tk.NORMAL) # 활성화
        else:
            self.update_button.config(state=tk.DISABLED) # 비활성화
            messagebox.showinfo("안내", "계획된 모든 치료가 완료되었습니다.")
        

    def update_info_labels(self, info, next_date_str):
        """환자 정보를 GUI 레이블에 표시"""
        self.info_labels['Name'].config(text=info['Name'])
        self.info_labels['Diagnosis'].config(text=info['Diagnosis'])
        self.info_labels['Total_Sessions'].config(text=f"{info['Total_Sessions']}회차")
        self.info_labels['Current_Session'].config(text=f"{info['Current_Session']}회차")
        self.info_labels['Treatment_Type_Cur'].config(text=info['Treatment_Type_Cur'])
        self.info_labels['Today_Instructions'].config(text=info['Today_Instructions'])
        self.info_labels['Next_Visit_Date'].config(text=next_date_str)
        self.info_labels['Next_Treatment'].config(text=info['Next_Treatment'])

    def calculate_next_visit(self, info):
        """다음 방문 권장일을 계산"""
        try:
            days = int(info['Next_Visit_Days'])
            next_date = datetime.now() + timedelta(days=days)
            return f"{next_date.strftime('%Y년 %m월 %d일')} ({days}일 후)"
        except ValueError:
            return "[오류] 다음 방문일 정보가 숫자가 아닙니다."

    def clear_info(self):
        """정보 출력 레이블 초기화"""
        for label in self.info_labels.values():
            label.config(text="---")
        self.update_button.config(state=tk.DISABLED)


    def update_session(self):
        """진료 완료 후 Current_Session을 1 증가시키고 저장"""
        patient_id = self.current_patient_id.get()
        
        if not patient_id:
            messagebox.showwarning("경고", "먼저 환자를 검색해 주세요.")
            return

        # 사용자에게 최종 확인
        confirm = messagebox.askyesno("확인", f"{self.df.loc[patient_id, 'Name']} 님의 진료 회차를 업데이트 하시겠습니까?")
        
        if confirm:
            # Current_Session 값 1 증가
            self.df.loc[patient_id, 'Current_Session'] += 1
            
            # 데이터 저장
            save_patient_data(self.df, EXCEL_FILE)
            
            # 화면 정보 즉시 업데이트
            self.search_patient() 
            

# --- 메인 실행 ---

if __name__ == "__main__":
    root = tk.Tk()
    app = PatientGuideApp(root)
    root.mainloop()