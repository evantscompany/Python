# 모듈 
# 하나의 py 파일에 모든 코드와 기능을 작성하면 복잡함.  기능별로 관리하거나 재사용하기 어려움.
# 모듈은 여러상수값이나 기능함수들을 가지고 있는 파일의 집합체 (일종의 폴더)


# 파이썬 모듈의 종류 
#1. 표준 모듈 : 파이썬을 설치할때 같이 내장되어 설치된 모듈들. 그래서 별도의 설치없이 그냥 import만 하면 됨.
# (내장함수는 아님. import 없이는 사용 불가)
#2. 외부 모듈 : 사용하려면 별도의 다운로드 및 설치작업이 요구되는 모듈들.
# [이런 외부모듈을 설치해주는 프로그램  pip - package installer for python]
# pip[CLI]환경으로 모듈을 설치

# 먼저 표준 모듈 중 활용이 많은 모듈들

# 1. math 모듈 : 수학적인 연산기능(함수)들을 모아놓은 폴더 같은 모듈

import math #모듈 적용

print(math.sin(1))
print(math.cos(1))
print(math.log(100,10)) # x, 밑수 .. [뜻. 밑수를 몇승하면 x 값이 되는가?]
print(math.floor(3.3)) # 소수점 아래 내리기..
print(math.ceil(3.1)) # 소수점 아래 올리기.. 
#반올림은 math 모듈이 아니라, 표준함수에 존재함. 

print(round(3.7))
print(round(3.2))

#1.1 모듈 사용할때마다 모듈명. 쓰는거 은근 짜증..  모듈명이 길면 쓰기 불편해서 다른 이름으로 바꿔부르기
import math as m # math 대신 m으로 쓰겠다.
print(m.pow(4,2)) # pow() : 4의 2제곱

#1.2 줄여쓰는 모듈명 조차도 짜증...  그냥 모듈명 없이 필요한 함수만  뽑아서 import
from math import floor,ceil #*쓰면 다 가져옴. from math import *
# 뽑아온 함수를 마치 내장 함수인냥 그냥 사용가능.

print(floor(2.5))


# 함수 말고 값도 있음.
print(math.pi)
print()

#2. random 모듈 : 랜덤값 생성, 관련 기능 
import random

print(random.random()) # 0.0000~0.99999999....... 까지

#만약 0~9중 하나의 숫자를 생성하려면.. (정수만...)
number= random.random()*10
print(floor(number))
# 위 계산을 쉽게 해주는 기능함수 존재함.
print(random.randrange(10)) #0~9
print(random.randrange(5,16)) #5~15

#리스트의 요소 중 랜덤하게 값을 선택하는 기능
aaa=[1,2,3,4,5]
print(random.choice(aaa))
print(random.sample(aaa,3)) # 임의의 값 3개를 선택 - 리스트로 리턴

#[예] 로또 번호 추천.
lotto = list(range(1,46))
print(lotto)
nums=random.sample(lotto,6)
nums.sort()
print(nums)
print()

#3. os 모듈 : 운영체제와 관련된 기능 모듈
import os

print('현재 운영체제 : ', os.name) # nt = window, posix = mac or linux
print('현재 작업폴더 : ', os.getcwd()) # current working directory
print('현재 폴더 안에 있는 파일과 폴더 목록들 : ', os.listdir())

#폴더 만들기
# os.mkdir('image') # 만약 이미 존재하는 폴더라면, 만들수 없음.에러!!
# if not os.path.isdir('image'):
# os.mkdir('image')
# else: 
# os.mkdir('image2')

#폴더 삭제
# os.rmdir('image2')

#폴더 이름 변경

# # 파일이름변경 -- 새로운 파일을 만들고 이름을 변경해보기. 

# with open("nice.txt",'w',encoding='utf-8')as file:
#     file.write('hello python....')

# # os.rename('nice.txt','good.txt')
# if os.path.exists('good.txt'): # 변경하려는 파일명이 있는지 확인 
#     #원래는 변경 못하도록 해야하지만, 지금은 연습으로, 그 파일을 제거하고 이름을 변경.
#     os.remove('good.txt')
#     os.rename('nice.txt','good.txt')
    
# print()

# # 명령 프롬프트(터미널)에서 실행했던 명령어를 코드로 실행할 수도 있음.  system()

# os.system('dir')
# # os.system('python ex01_print.py')

# #change directory 명령은 일부 안됨.
# os.system('cd ..') # 안됨. change directory 전용함수를 이용해야함. 

# os.chdir('..')
# os.chdir('Projects')

