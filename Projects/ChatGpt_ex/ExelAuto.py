import pandas as pd
import glob
import os


def merge_excel_files(folder_path, sort_column=None):
    #폴더 내 엑셀 파일 목록 찾기
    excel_files = glob.glob(os.path.join(folder_path,"*.xlsx"))

    if not excel_files:
        print('엑셀 파일이 없습니다.')
        return
    
    all_data=[]

    #파일 하나씩 읽어서 리스트에 저장

    for file in excel_files:
        print(f" 읽는 중 : {file}")
        df = pd.read_excel(file)

        #공백 제거
        df= df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        df= df.dropna(how="all") # 완전 빈 줄 제거

        all_data.append(df)

    # 하나의 Dataframe 으로 합치기

    merged_df = pd.concat(all_data, ignore_index=True)

    #정렬옵션
    if sort_column and sort_column in merged_df.columns:
        merged_df=merged_df.sort_values(by=sort_column)

    output_path=os.path.join(folder_path, "result.xlsx")
    merged_df.to_excel(output_path,index=False)

    print(f'완료! 저장위치 : {output_path}')    

