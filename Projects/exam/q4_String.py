# message = input(" 아무 문장이나 입력하세요 >>")
# print("문자열의 길이는 : {}".format(len(message)))
# print("첫번째 문자는 : {}".format(message[0]))
# print("마지막 문자는 : {}".format(message[-1]))

# whitespace_string="      PYTHON      "
# print(whitespace_string.lower().strip(" "))


# sen= 'Python is a great language'
# print('great' in sen)

# num1=input("전화번호 첫번째 자리를 입력하세요(3자리)>>")
# num2=input("전화번호 두번째 자리를 입력하세요(3~4자리)>>")
# num3=input("전화번호 세번째 자리를 입력하세요(4자리)>>")

# print("입력된 전화번호는 [ {}-{}-{} ] 입니다".format(num1,num2,num3))

# mail=input("이메일 주소를 입력하세요 >>")
# mail_div=mail.split("@")
# print(mail)
# print("입력된 메일 주소명 : {}".format(mail_div[0]))
# print("메일 서버 이름 : {}".format(mail_div[1]))

message ='''
올해 신년 기자회견에서 저는 AI 연구와 AI 산업이 국가 경쟁력을 좌우할 것이라고 말씀드립니다.
정부는 공공 서비스에 ai를 적극 도입해 행정 효율성을 높일 계획입니다.
특히 의료AI 분야와 재난 대응 AI 시스템은 국민 안전을 지키는 데 중요한 역할을 할 것입니다.
교육 영역에서는 ai 기반 맞춤형 학습과 AI 튜터링 서비스를 확대하겠습니다.
중소기업의 생산성을 높이기 위해 AI 자동화와 AI 데이터 분석 지원 사업을 강화합니다.
산업 전반의 데이터·AI 생태계를 정비해 혁신 기반을 구축하겠습니다.
국방 분야에서도 ai 기술을 활용해 보다 정교한 위협 대응 체계를 마련하겠습니다.
또한 교통·에너지 관리에 AI 예측 모델을 적용해 효율성을 높이겠습니다.
정부는 AI 윤리 기준과 AI 안전 규범을 마련해 기술 발전이 책임 있게 이루어지도록 하겠습니다.
끝으로, ai 혁신이 모두에게 혜택이 될 수 있도록 포용적 성장을 이루겠습니다.
'''

print("해당 메세지의 총 글자수는 {}개 입니다".format(len(message)))
message_replace = message.replace(" ","").replace("\n","")
print("해당 메세지 중 줄바꿈,띄어쓰기를 제외한 글자수는 {}개 입니다".format(len(message_replace)))
print("해당 메세지에서 AI 라는 단어는 {}번 출현 합니다".format(message.upper().count('AI')))
