
# try:
     
#     number_input_a= int(input("정수입력 >>"))
#     print('원의 반지름 :' , number_input_a)
#     print('원의 둘레 :' , 2*3.14*number_input_a)
#     print('원의 넓이 :' , 3.14*number_input_a*number_input_a)

    
# except:
#     print('정수를 입력하지 않았습니다')


# else:
#     print('예외가 발생하지 않았습니다. ')
    
# finally:
#     print("일단 프로그램이 어떻게든 끝났습니다.")



# list_input_a = ["52","273","32",'스파이','103']

# list_number=[]
# for item in list_input_a:
#     try :
#         float(item)
#         list_number.append(item)
#     except Exception as e:
#         print(e)

# print("{}내부에 있는 숫자는".format(list_input_a))
# print("{}입니다".format(list_number))


# def write_text_file(filename, text):
#     try : 
#         file= open(filename,'w')
#         return
#         file.write(text)

#     except:
#         print('오류가 발생했습니다')
#     finally:
#         file.close()

# write_text_file('text.txt',"안녕하세요!")



numbers = [52,273,32,103,90,10,275]

print("#(1) 요소 내부에 있는 값 찾기")
print(" - {}는 {}위치에 있습니다.".format(52, numbers.index(52)))
print()

print("#(2) 요소 내부에 없는 값 찾기")
number = 10000

try:
    print(" - {}는 {}위치에 있습니다.".format(number, numbers.index(number)))
except:
    print('- 리스트 내부에 없는 값입니다')

print()

print("--------정상적으로 종료되었습니다------------")
