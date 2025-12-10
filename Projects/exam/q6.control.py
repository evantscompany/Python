# output = ""

# for i in range(1,15):
#     for j in range(14,i,-1):
#         output+=" "
#     for k in range(0,2*i-1):
#         output+="*"
#     output+="\n"


# print(output)        

# output = ""

# for i in range(1,10):
#     output +=("*"*i)
#     output +="\n"
# print(output)

# import time
# number = 0

# target_tick = time.time()+5
# while time.time()<target_tick:
#     number+=1

# print("5초 동안 {}번 반복했습니다".format(number))

i = 0

# while True:
#     print("{}번째 반복문 입니다.".format(i))
#     i=i+1

#     input_text=input(">종료하시겠습니까?(y/n)")
#     if input_text in ["y","Y"]:
#         print("반복을 종료합니다")
#         break


# limit = 10000
# i = 1

# sum_value=0

# while sum_value<limit:
#     sum_value +=i
#     print(i,sum_value)
#     i+=1

# print("{}를 더할 때 {}을 넘으며 그 때의 값은 {}입니다".format(i,limit,sum_value))

    
# max_value=0
# a= 0
# b= 0 

# for i in range (1,100):
#     j=100-i
#     print(i*j)
    



# print(j,i)

# plus_num=int(input("양의 정수를 하나 입력하세요"))

# for a in range(plus_num):
#     print("hello")


#---------------------------------------

# num = int(input("양의 정수를 입력하세요"))

# for a in range (3,(num*3+1),3):
#     print(a," ",end="")


#----------------------------------------

# total = 0

# while True:
#     num=int(input("정수를 입력하세요"))    
#     total += num
#     print(num)
#     if num == 0:
#         print(total)
#         break

#---------------------------------------------------
   
# dan= int(input("출력할 구구단 단수 입력 >>"))

# for a in range(9,0,-1):
#     print(f"{dan}x{a}={dan*a}")

#----------------------------------------------------

# count = int(input("평균을 구할 숫자 갯수를 입력>>"))
# total_av = 0

# for a in range (1,count+1):
#     av=int(input(f"{a} 번째 숫자입력 : "))
#     total_av+=av

# print("{}개 숫자를 입력하였으며 평균 값은 {:4f} 입니다.".format(count,float(total_av/count)))

#--------------------------------------------------------------

# value_sum= 0

# a=0
# while a<5:

#     num= int(input(f"{a}번째숫자 :  '1'이상의 값을 입력하세요>>"))
    
#     if num>0:
#         value_sum+=num
#         a+=1

    
#     else:
#         print("1이상의 값만 입력하세요>>")

# print(value_sum)

# output=""


# for a in range (0, 5):
#     for j in range(0, a):
#         output+="o"
#     output+="*"

#     output+="\n"
      
# print(output)

# for n in range(1,100):
#     if n%7==0 or n%9==0:
#         print(n,end= " ")

word = input("각 단어에 콤마를 추가하여 여러개 입력하시오").split(",")
total_word = ""

a=0
while a<len(word):
    if len(word[a])>=5:
        total_word+=word

print(total_word)        
        
    
   

    


   














