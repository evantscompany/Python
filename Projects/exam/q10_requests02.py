import json

# 제공해 주신 JSON 데이터를 Python 딕셔너리로 저장합니다.
json_data = {
  "movieInfoResult": {
    "movieInfo": {
      "movieCd": "20252432",
      "movieNm": "주토피아 2",
      "movieNmEn": "Zootopia 2",
      "movieNmOg": "",
      "showTm": "108",
      "prdtYear": "2025",
      "openDt": "20251126",
      "prdtStatNm": "개봉",
      "typeNm": "장편",
      "nations": [
        {
          "nationNm": "미국"
        }
      ],
      "genres": [
        {
          "genreNm": "애니메이션"
        }
      ],
      "directors": [
        {
          "peopleNm": "재러드 부시",
          "peopleNmEn": "Jared Bush"
        },
        {
          "peopleNm": "바이론 하워드",
          "peopleNmEn": "Byron Howard"
        }
      ],
      "actors": [
        {
          "peopleNm": "지니퍼 굿윈",
          "peopleNmEn": "Ginnifer Goodwin",
          "cast": "",
          "castEn": ""
        },
        {
          "peopleNm": "제이슨 베이트먼",
          "peopleNmEn": "Jason Bateman",
          "cast": "",
          "castEn": ""
        },
        {
          "peopleNm": "키 호이 콴",
          "peopleNmEn": "Ke Huy-Quan",
          "cast": "",
          "castEn": ""
        }
      ],
      "showTypes": [
        {
          "showTypeGroupNm": "2D",
          "showTypeNm": "디지털"
        },
        {
          "showTypeGroupNm": "2D",
          "showTypeNm": "디지털 영문자막"
        }
      ],
      "companys": [
        {
          "companyCd": "20161801",
          "companyNm": "월트디즈니컴퍼니코리아 유한책임회사",
          "companyNmEn": "The Walt Disney Company Korea",
          "companyPartNm": "배급사"
        },
        {
          "companyCd": "20161801",
          "companyNm": "월트디즈니컴퍼니코리아 유한책임회사",
          "companyNmEn": "The Walt Disney Company Korea",
          "companyPartNm": "수입사"
        }
      ],
      "audits": [
        {
          "auditNo": "2025-MF03006",
          "watchGradeNm": "전체관람가"
        }
      ],
      "staffs": []
    },
    "source": "영화진흥위원회"
  }
}

# 1. 'movieInfo' 딕셔너리를 추출하여 접근을 단순화합니다.
movie_info = json_data['movieInfoResult']['movieInfo']

# 2. 팀별 데이터를 추출하고 리스트 형태로 정리합니다.

# 2-1. 🎬 감독 (directors)
directors = [d['peopleNm'] for d in movie_info.get('directors', [])]
# 영어 이름도 보고 싶다면:
# directors_en = [f"{d['peopleNm']} ({d['peopleNmEn']})" for d in movie_info.get('directors', [])]

# 2-2. 🎭 출연진 (actors)
# 출연진 이름만 추출합니다.
actors = [a['peopleNm'] for a in movie_info.get('actors', [])]

# 2-3. 🏢 제작/배급사 (companys)
# 회사명과 그 역할을 묶어서 추출합니다.
companies = [f"{c['companyNm']} ({c['companyPartNm']})" for c in movie_info.get('companys', [])]

# 3. 정리된 정보를 출력합니다.
print(f"==================================================")
print(f"🎬 영화 제목: {movie_info['movieNm']} ({movie_info['movieNmEn']})")
print(f"==================================================")

# 3-1. 감독 정보 출력
print("### 👥 감독 (Directors)")
if directors:
    print(f"총 {len(directors)}명: {', '.join(directors)}")
else:
    print("정보 없음")

print("-" * 50)

# 3-2. 출연진 정보 출력
print("### 🌟 출연진 (Actors)")
if actors:
    print(f"총 {len(actors)}명: {', '.join(actors)}")
else:
    print("정보 없음")

print("-" * 50)

# 3-3. 제작/배급사 정보 출력
print("### 🏢 배급/수입사 (Companies)")
if companies:
    # 중복 제거를 위해 set()을 사용하고 다시 리스트로 변환 후 출력
    unique_companies = list(set(companies))
    print(f"총 {len(unique_companies)}개:")
    for company in unique_companies:
        print(f"  - {company}")
else:
    print("정보 없음")

print("==================================================")