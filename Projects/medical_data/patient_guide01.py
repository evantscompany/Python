# 핵심 코드 검증 목표 
# 1. 엑셀 파일을 오류없이 불러와 데이터프레임으로 만드는지 확인
# 2. ID 검색 : 입력한 Patient_ID로 정확한 환자 정보를 찾아내는지 확인
# 3. Next_Visit_Days 를 바탕으로 다음 방문 권장일이 올바르게 계산되는지 확인

import pandas as pd 
from datetime import datetime, timedelta
import os

#--설정변수
#--엑셀 파일 경로 설정 ( 동일 폴더 내에 있어야 함)
EXCEL_FILE = 'Projects/medical_data/aaa.xlsx'
SHEET_NAME = 'TreatmentPlan'

#--함수 정의 --

def load_patient_data(file_path): # 엑셀 파일을 읽어와 Patient_ID를 인덱스로 설정한 DataFrame 반환
    try : 
        #엑셀파일을 불러오면서 Patient_ID를 인덱스로 지정 
        df=pd.read_excel("Projects/medical_data/aaa.xlsx")
        df.set_index('Patient_ID',inplace=True)
       
        return df
    
    except FileNotFoundError:
        print(f"\n[치명적 오류] 엑셀파일 '{file_path}을 찾을 수 없습니다. 경로를 확인하세요")
        return None
    except Exception as e :
        #그 외 시스템 오류 발생 시 메시지 출력
        print(f"\n[시스템 오류] 엑셀 파일 로드 중 문제가 발생했습니다 : {e}")
        return None
    
def save_patient_data(df, file_path):
    try:
        df.to_excel(file_path, sheet_name=SHEET_NAME, index=True)
        print("\n[저장완료] 환자의 진료 정보가 엑셀 파일에 성공적으로 업데이트 되었습니다.")
    except Exception as e :
        print(f"\n[치명적오류] 파일 저장 중 문제가 발생했습니다. 파일이 열려있는지 확인해 주세요")

def run_patient_program(df):

    print("\n --- 대가연 마취통증의학과 진료 안내 시스템 ---")
    patient_id=input("환자 ID (예: P-250001)를 입력하세요 : ").strip().upper()

    if patient_id not in df.index:
        print(f"\n [검색실패] ID '{patient_id}'에 해당하는 환자 정보를 찾을 수 없습니다.")
        return
    
    patient_info=df.loc[patient_id]

    print("\n========================================")
    print(f"환자명: {patient_info['Name']} (ID: {patient_id})")
    print(f"진단명: {patient_info['Diagnosis']}")
    print("----------------------------------------")

    current_session = patient_info['Current_Session']
    total_sessions = patient_info['Total_Sessions']

    print(f" 현재 회차: {current_session}회차 / 총 {total_sessions}회차")
    print(f" 금일 치료: {patient_info['Treatment_Type_Cur']}")
    print(f" 금일 주의사항: {patient_info['Today_Instructions']}")

    try:
        days_to_next = int(patient_info['Next_Visit_Days'])
        next_visit_date = datetime.now() + timedelta(days=days_to_next)

        print("\n=== 다음 방문 일정 안내 ===")
        # 날짜 형식을 'YYYY년 MM월 DD일'로 지정하여 출력
        print(f"다음 방문 권장일: {next_visit_date.strftime('%Y년 %m월 %d일')} (약 {days_to_next}일 후)")
        print(f"다음 치료 내용: {patient_info['Next_Treatment']}")
    
    except ValueError:
        # Next_Visit_Days 컬럼에 숫자가 아닌 다른 값이 들어있을 경우 예외 처리
        print("\n[안내] 다음 방문일 정보(Next_Visit_Days)가 명확하지 않아 날짜 계산이 어렵습니다.")
    
    print("========================================")

    if current_session < total_sessions:
        # 사용자에게 진료 완료 여부 확인
        update_choice = input(f"\n⭐ {patient_info['Name']} 님의 금일 진료가 완료되었습니까? (Y/N): ").strip().upper()
        
        if update_choice == 'Y':
            # .loc[]를 이용해 해당 환자의 Current_Session 값을 1 증가시킴 (데이터프레임 메모리 내에서만 변경)
            df.loc[patient_id, 'Current_Session'] += 1
            
            # 변경된 내용을 엑셀 파일에 저장 요청 (영구 저장)
            save_patient_data(df, EXCEL_FILE)
            
        elif update_choice == 'N':
            print("업데이트 없이 프로그램을 종료합니다.")
        else:
            print("잘못된 입력입니다. 업데이트 없이 종료합니다.")
    else:
        # 총 회차와 현재 회차가 같으면 완료 메시지 출력
        print(f"\n[안내] {total_sessions}회차로 모든 계획된 치료가 완료되었습니다. 최종 경과 관찰을 진행해 주세요.")


# --- 프로그램 시작 지점 ---

# 이 코드가 메인 스크립트로 실행될 때만 아래 블록 실행
if __name__ == "__main__": 
    # 데이터 로드 함수 호출
    treatment_df = load_patient_data(EXCEL_FILE)
    
    # 데이터 로드가 성공적(None이 아님)일 경우에만 메인 실행 함수 호출
    if treatment_df is not None:
        run_patient_program(treatment_df)



import pandas as pd
import tkinter as tk
from tkinter import messagebox,ttk
import os


