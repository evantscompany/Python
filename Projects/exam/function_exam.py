FILE_PATH = r"C:\Users\Admin\MBCA\Python\files\scores.csv"


def read_scores(filename):
    """CSV 파일을 읽어 점수 데이터를 반환하는 함수"""
    data = []

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    header = lines[0].strip().split(",")  # ["이름", "국어", "영어", "수학"]

    for line in lines[1:]:  # 첫 줄 제외
        parts = line.strip().split(",")
        name = parts[0]
        scores = list(map(int, parts[1:]))  # 점수 숫자로 변환
        data.append([name] + scores)

    return header, data


def calc_subject_stats(data):
    """과목별 통계 계산"""
    korean  = [row[1] for row in data]
    english = [row[2] for row in data]
    math    = [row[3] for row in data]

    stats = {
        "국어": (sum(korean)/len(korean), max(korean), min(korean)),
        "영어": (sum(english)/len(english), max(english), min(english)),
        "수학": (sum(math)/len(math), max(math), min(math)),
    }
    return stats


def print_stats(stats):
    """과목별 통계 출력"""
    print("[과목별 통계]")
    for subject, (avg, max_val, min_val) in stats.items():
        print(f"{subject} - 평균: {avg:.1f}, 최고점: {max_val}, 최저점: {min_val}")


def save_result_csv(data, filename="result.csv"):
    """학생별 총점, 평균을 result.csv 파일로 저장"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("이름,총점,평균\n")

        for row in data:
            name = row[0]
            total = sum(row[1:])
            avg = total / 3
            f.write(f"{name},{total},{avg:.2f}\n")


# ---------------------------- 실행 파트 ----------------------------

header, data = read_scores(FILE_PATH)
stats = calc_subject_stats(data)
print_stats(stats)

# 선택 과제: 결과 CSV 저장
save_result_csv(data)
print("\nresult.csv 파일 저장 완료!")
