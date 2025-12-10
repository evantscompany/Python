from PIL import Image
import os
import random

# 저장할 폴더
os.makedirs("random_patient_photos", exist_ok=True)

for i in range(1, 21):
    # 300x300 픽셀 이미지
    img = Image.new('RGB', (300, 300), 
                    (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    img.save(f"random_patient_photos/patient_{i}.png")

print("랜덤 환자 사진 20개 생성 완료!")