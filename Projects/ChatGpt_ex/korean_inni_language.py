import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import os
import datetime



# --- 1. 핵심 기능: 인도네시아어 발음 한글 표기 변환 함수 ---
def id_to_korean_phonetic(text):
    """
    인도네시아어 텍스트를 간소화된 한글 발음으로 변환하는 함수.
    (실제 외래어 표기법은 훨씬 복잡하며, 이는 단순 예시 로직임)
    """
    text = text.lower()
    
    # 주요 발음 규칙 치환 (매우 간소화된 규칙)
    conversion_map = {
        'c': 'ㅊ', 'sy': '시', 'kh': '크', 'ng': '응',
        'e': '으', 'o': '오', 'u': '우', 'a': '아', 'i': '이',
        'r': '르', 'l': '을', 'k': '크', 'p': '프',
        # 문장 끝 발음 단순화 (예: 'selamat' -> '슬라맛')
        't': '트', 'd': '드', 'b': '브'
    }
    
    # 복합 자음/모음 먼저 처리
    for key, value in sorted(conversion_map.items(), key=lambda item: len(item[0]), reverse=True):
        text = text.replace(key, value)
    
    # 자음으로 끝나는 단어 처리 (한국어는 받침 사용)
    # 복잡하므로 여기서는 간단한 대체만 수행
    
    return text.strip()

# --- 2. GUI 로직 및 기능 함수 ---

class VoiceMemoApp:
    def __init__(self, master):
        self.master = master
        master.title("인도네시아어 음성 메모장")
        
        self.r = sr.Recognizer()
        self.memo_file = "voice_memo.txt"

        # UI 구성
        self.label = tk.Label(master, text="아래 버튼을 누르고 인도네시아어로 말하세요.")
        self.label.pack(pady=10)

        self.record_button = tk.Button(master, text="🎙️ 녹음 시작", command=self.start_recording)
        self.record_button.pack(pady=5)
        
        self.status_label = tk.Label(master, text="대기 중...", fg="blue")
        self.status_label.pack(pady=5)

        self.result_label = tk.Label(master, text="결과:", justify=tk.LEFT, wraplength=400)
        self.result_label.pack(pady=10, padx=10)
        
        self.save_button = tk.Button(master, text="💾 메모 저장", command=self.save_memo, state=tk.DISABLED)
        self.save_button.pack(pady=10)

    def start_recording(self):
        """음성 인식을 시작하고 결과를 처리합니다."""
        self.status_label.config(text="녹음 중... 말하세요!", fg="red")
        self.master.update()

        try:
            with sr.Microphone() as source:
                self.r.adjust_for_ambient_noise(source)
                audio = self.r.listen(source, timeout=5, phrase_time_limit=10)
            
            self.status_label.config(text="음성 인식 중...", fg="orange")
            self.master.update()
            
            # Google Speech Recognition 사용 (인도네시아어 'id-ID')
            indonesian_text = self.r.recognize_google(audio, language="id-ID")
            
            # 한글 발음 표기 변환
            korean_phonetic = id_to_korean_phonetic(indonesian_text)
            
            # 결과 업데이트
            result_text = f"인도네시아어: {indonesian_text}\n한글 표기: {korean_phonetic}"
            self.result_label.config(text=result_text)
            self.status_label.config(text="인식 완료. 저장 가능.", fg="green")
            self.save_button.config(state=tk.NORMAL)
            
            self.last_indonesian_text = indonesian_text
            self.last_korean_phonetic = korean_phonetic

        except sr.WaitTimeoutError:
            self.status_label.config(text="인식 시간 초과. 다시 시도하세요.", fg="red")
            self.save_button.config(state=tk.DISABLED)
        except sr.UnknownValueError:
            self.status_label.config(text="음성을 인식할 수 없습니다.", fg="red")
            self.save_button.config(state=tk.DISABLED)
        except sr.RequestError as e:
            self.status_label.config(text=f"API 요청 실패; 인터넷 연결 확인 ({e})", fg="red")
            self.save_button.config(state=tk.DISABLED)
        except Exception as e:
            self.status_label.config(text=f"오류 발생: {e}", fg="red")
            self.save_button.config(state=tk.DISABLED)


    def save_memo(self):
        """인식된 내용을 텍스트 파일에 저장합니다."""
        if hasattr(self, 'last_indonesian_text') and self.last_indonesian_text:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            memo_entry = (
                f"[{timestamp}]\n"
                f"원문 (ID): {self.last_indonesian_text}\n"
                f"한글 발음: {self.last_korean_phonetic}\n"
                "------------------------------------\n"
            )
            
            try:
                with open(self.memo_file, "a", encoding="utf-8") as f:
                    f.write(memo_entry)
                messagebox.showinfo("저장 완료", f"메모가 성공적으로 저장되었습니다.\n({self.memo_file})")
                self.save_button.config(state=tk.DISABLED)
            except Exception as e:
                messagebox.showerror("저장 오류", f"파일 저장 중 오류 발생: {e}")
        else:
            messagebox.showwarning("오류", "먼저 녹음을 완료해주세요.")


# --- 3. 메인 실행 ---

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceMemoApp(root)
    root.mainloop()