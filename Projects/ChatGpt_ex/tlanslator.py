import tkinter as tk
from tkinter import scrolledtext
from deep_translator import GoogleTranslator

def translate_text():
    src_text = input_text.get("1.0", tk.END).strip()
    if not src_text:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "번역할 내용을 입력하세요.")
        return
    try:
        translated = GoogleTranslator(source='ko', target='en').translate(src_text)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)
    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"번역 중 오류 발생: {e}")

# GUI 창 생성
window = tk.Tk()
window.title("파이썬 GUI 번역기")
window.geometry("500x400")

# 입력 텍스트
tk.Label(window, text="번역할 문장 입력:").pack()
input_text = scrolledtext.ScrolledText(window, height=8)
input_text.pack(pady=5)

# 번역 버튼
btn_translate = tk.Button(window, text="번역하기", command=translate_text)
btn_translate.pack(pady=5)

# 출력 텍스트
tk.Label(window, text="번역 결과:").pack()
output_text = scrolledtext.ScrolledText(window, height=8)
output_text.pack(pady=5)

# GUI 실행
window.mainloop()