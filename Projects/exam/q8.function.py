# def print_3_times():
#     print("안녕하세요")
#     print("안녕하세요")
#     print("안녕하세요")

# print_3_times()    

# def print_n_times (value, n):
#     for i in range(n):
#         print(value)

# print_n_times("안녕하세요",5)



# def print_n_times(n,*values):
#     #n번 반복합니다.
#     for i in range(n):
#         # values 는 리스트처럼 활용합니다. 
#         for value in values:
#             print(value)
            

# print_n_times(3,"안녕하세요","즐거운","파이썬 프로그래밍")


# def print_n_times(value,n=2):
#     for i in range(n):
#         print(value)

# print_n_times("안녕하세요")


# def sum_all(start=0, end=100,step=1):
#     output=0
#     for i in range(start,end+1,step):
#         output+=i
#     return output

# def mul(*values):
#     output=1
#     for i in range (len(values)):
#         output*=values[i]
#         print(output,values[i])
#     return output

# print(mul(5,7,9,10))    

# def my_max(values):
#     max_num=0
#     for i in range(len(values)):
#         if values[i]>max_num:
#             max_num=values[i]
#     return max_num


# def my_min(values):
#     min_num=sum(values)
#     for i in range(len(values)):
#         if values[i]<min_num:
#             min_num=values[i]
#     return min_num


# total_count=[]
# while True:
#     count=input("숫자를 입력하고, 다 입력한 경우 0000 입력>>")
#     count=int(count)
#     if count!=0000:
#         total_count.append(count)
#     else:
#         break    
# print(f"입력하신 모든 값은{total_count}이며,")

# print(f"최대값은 {my_max(total_count)} 입니다")
# print(f"최소값은 {my_min(total_count)} 입니다")

# # my_max(num)


# # print(num)
# # my_max(num)


# # print(my_min(3000,-1,900))

def cel_to_fah():
    cel=0
    while True:
        cel=int(input("섭씨 온도를 입력하세요.>>"))
        fah=1.8*cel+32
        print(f"입력하신 섭씨 온도는{cel}이며, 화씨 온도는 {fah}입니다 ")
        break

cel_to_fah()
    
