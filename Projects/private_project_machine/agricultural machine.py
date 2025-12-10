import numpy
import pandas as pd 
import requests
from bs4 import BeautifulSoup

def load_kosis_data(url: str) -> pd.DataFrame:
    #kosis 통계 json을 요청하고, pandas Dataframe 으로 변환하는 함수

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    rows = None
    if 'StatisticSearch' in data :
        rows = data['StatisticSearch'].get('row')
    elif 'result' in data:
        rows=data['result']
    else:
        raise ValueError
    
    if rows is None:
        raise ValueError
    
    df=pd.json_normalize(rows)
    return df


if __name__=="__main__":
    url = "https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=ZWJiOTY0MGNmZWY0NTg0MTUxMzM0ZDBhODAwODdjYTY=&itmId=T00+T01+T02+T03+T04+T05+T06+T07+T08+T09+T10+T11+T12+T13+T14+T15+T16+T17+T18+&objL1=00+03+04+05+11+21+22+23+24+25+26+29+31+32+33+34+35+36+37+38+39+&objL2=000+B00+J00+K00+M00+S00+T00+V00+&objL3=&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=F&newEstPrdCnt=3&orgId=101&tblId=DT_1AG20119"
    df= load_kosis_data(url)
    print(df.info())
    print(df.head())
