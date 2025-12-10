import PyPDF2 as pdf

with open ("files/파이썬 실행파일 만들기.pdf","rb") as f:
    reader = pdf.PdfReader(f)
    text=""
    for page in reader.pages : 
        text+= page.extract_text()

print(text)