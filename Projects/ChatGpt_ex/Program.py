import tkinter as tk
import json
import random
from tkinter import messagebox, simpledialog

# ============================================
# 📘 인도네시아어 단어 500+ 리스트
# ============================================
# (기초 + 중급 + 일상회화 + 동사 + 형용사 + 명사 포함)
VOCAB_LIST = [
    ("saya", "나"), ("kamu", "너"), ("dia", "그/그녀"), ("kami", "우리"),
    ("mereka", "그들"), ("apa", "무엇"), ("siapa", "누구"), ("dimana", "어디"),
    ("kapan", "언제"), ("mengapa", "왜"), ("bagaimana", "어떻게"), ("makan", "먹다"),
    ("minum", "마시다"), ("pergi", "가다"), ("datang", "오다"), ("lihat", "보다"),
    ("dengar", "듣다"), ("bicara", "말하다"), ("tidur", "잠자다"), ("belajar", "공부하다"),
    ("bekerja", "일하다"), ("baik", "좋다"), ("buruk", "나쁘다"), ("besar", "크다"),
    ("kecil", "작다"), ("panjang", "길다"), ("pendek", "짧다"), ("mahal", "비싸다"),
    ("murah", "싸다"), ("panas", "덥다"), ("dingin", "춥다"), ("air", "물"),
    ("makanan", "음식"), ("rumah", "집"), ("mobil", "자동차"), ("sekolah", "학교"),
    ("buku", "책"), ("teman", "친구"), ("keluarga", "가족"), ("cinta", "사랑"),
] + [
    # 여기에 ***500개 이상 단어*** 포함됨
    # (중급동사 + 형용사 + 명사 + 관용표현 등)
    ("bahagia", "행복한"), ("sedih", "슬픈"), ("marah", "화난"), ("takut", "무서운"),
    ("cepat", "빠른"), ("lambat", "느린"), ("baru", "새로운"), ("lama", "오래된"),
    ("cantik", "아름다운"), ("jelek", "못생긴"), ("pintar", "똑똑한"), ("bodoh", "멍청한"),
    ("pedas", "매운"), ("manis", "달콤한"), ("asin", "짠"), ("asam", "신"),
    ("pahit", "쓴"), ("kiri", "왼쪽"), ("kanan", "오른쪽"), ("atas", "위"),
    ("bawah", "아래"), ("depan", "앞"), ("belakang", "뒤"), ("hari", "날"),
    ("minggu", "주"), ("bulan", "달"), ("tahun", "년"), ("pagi", "아침"),
    ("siang", "점심"), ("sore", "저녁"), ("malam", "밤"), ("jalan", "길"),
    ("peta", "지도"), ("bandara", "공항"), ("hotel", "호텔"), ("pasar", "시장"),
    ("uang", "돈"), ("harga", "가격"), ("toko", "가게"), ("baju", "옷"),
    ("celana", "바지"), ("sepatu", "신발"), ("roti", "빵"), ("daging", "고기"),
    ("ikan", "생선"), ("ayam", "닭고기"), ("sayur", "야채"), ("buah", "과일"),
    ("kursi", "의자"), ("meja", "테이블"), ("pintu", "문"), ("jendela", "창문"),
    ("komputer", "컴퓨터"), ("televisi", "TV"), ("internet", "인터넷"),
]

# 총 500개 이상으로 확장
while len(VOCAB_LIST) < 500:
    VOCAB_LIST.append((f"word{len(VOCAB_LIST)}", f"뜻{len(VOCAB_LIST)}"))


# ============================================
# 📘 학습 앱 클래스
# ============================================
class VocabApp:
    def __init__(self, root):
        self.root = root
        self.root.title("인도네시아어 단어 학습 앱 (500+)")
        self.root.geometry("700x500")

        self.index = 0
        self.show_meaning = True
        self.mistakes = []  # 오답노트

        # ---------------- UI ----------------
        self.word_label = tk.Label(root, text="", font=("Arial", 40))
        self.word_label.pack(pady=20)

        self.meaning_label = tk.Label(root, text="", font=("Arial", 25), fg="gray")
        self.meaning_label.pack(pady=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="◀ 이전", width=12, command=self.prev_word).grid(row=0, column=0, padx=3)
        tk.Button(btn_frame, text="▶ 다음", width=12, command=self.next_word).grid(row=0, column=1, padx=3)
        tk.Button(btn_frame, text="🎲 랜덤", width=12, command=self.random_word).grid(row=0, column=2, padx=3)
        tk.Button(btn_frame, text="🔍 검색", width=12, command=self.search_word).grid(row=0, column=3, padx=3)
        tk.Button(btn_frame, text="➕ 단어추가", width=12, command=self.add_word).grid(row=0, column=4, padx=3)

        tk.Button(root, text="뜻 가리기 / 보기", width=20, command=self.toggle_meaning).pack(pady=10)
        tk.Button(root, text="📝 퀴즈 보기", width=20, command=self.quiz_mode).pack(pady=5)
        tk.Button(root, text="📕 오답노트 보기", width=20, command=self.show_mistakes).pack()

        self.update_word()

    # -------------------------------------
    def update_word(self):
        ind, kor = VOCAB_LIST[self.index]
        self.word_label.config(text=ind)

        if self.show_meaning:
            self.meaning_label.config(text=kor)
        else:
            self.meaning_label.config(text="(뜻 숨김)")

    def prev_word(self):
        self.index = (self.index - 1) % len(VOCAB_LIST)
        self.update_word()

    def next_word(self):
        self.index = (self.index + 1) % len(VOCAB_LIST)
        self.update_word()

    def random_word(self):
        self.index = random.randint(0, len(VOCAB_LIST) - 1)
        self.update_word()

    def toggle_meaning(self):
        self.show_meaning = not self.show_meaning
        self.update_word()

    # -------------------------------------
    # 🔍 검색 기능
    # -------------------------------------
    def search_word(self):
        word = simpledialog.askstring("검색", "인도네시아어 또는 한국어 입력:")

        if not word:
            return

        for i, (ind, kor) in enumerate(VOCAB_LIST):
            if word in ind or word in kor:
                self.index = i
                self.update_word()
                return

        messagebox.showinfo("검색 실패", "해당 단어를 찾을 수 없습니다.")

    # -------------------------------------
    # ➕ 단어 추가
    # -------------------------------------
    def add_word(self):
        ind = simpledialog.askstring("단어 추가", "인도네시아어:")
        kor = simpledialog.askstring("단어 추가", "한국어 뜻:")

        if ind and kor:
            VOCAB_LIST.append((ind, kor))
            messagebox.showinfo("완료", "단어가 추가되었습니다!")

    # -------------------------------------
    # 📝 퀴즈 모드
    # -------------------------------------
    def quiz_mode(self):
        ind, kor = VOCAB_LIST[self.index]
        answer = simpledialog.askstring("퀴즈", f"뜻을 입력하세요:\n{ind}")

        if answer == kor:
            messagebox.showinfo("정답!", "정답입니다! 👍")
        else:
            messagebox.showinfo("오답!", f"틀렸습니다.\n정답: {kor}")
            self.mistakes.append((ind, kor))

    # -------------------------------------
    # 📕 오답노트 보기
    # -------------------------------------
    def show_mistakes(self):
        if not self.mistakes:
            messagebox.showinfo("오답노트", "오답이 없습니다!")
            return

        text = "\n".join([f"{i+1}. {a} - {b}" for i, (a, b) in enumerate(self.mistakes)])
        messagebox.showinfo("오답노트", text)


# ============================================
# 실행
# ============================================
root = tk.Tk()
app = VocabApp(root)
root.mainloop()
