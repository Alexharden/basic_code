# a = int(input("輸入"))
# for i in range(a+1):
#     print("*" * i)
# for i in range(4,0,-1):
#     print(i)
# print()
# for i in range(0,4,1):
#     print(i)

# print()
# for i in reversed(range(0,4,1)):
#     print(i)   
    # print("*" * i)

# a = int(input("輸入 "))    
# for i in range(a+1):
#     print(' ' * (a-i) + '*' * (2*i-1))

# n = eval(input("輸入"))
# for i in range(n):
#     for a in range(n-i-1):
#         print(' ',end='')
#     for b in range(2*i+1):    
#         print('*',end='')
#     # print('\n',end='')  


# n = eval(input('請輸入三角形邊長:'))   #讓使用者輸入三角形邊長為n
# for i in range(n):                #撰寫雙層迴圈控制三角形長度，執行n次，每次分別輸出該行的空白與*號
#     for j in range(n-i,1,-1):       #三角形的前面須由空白填補，每行空白數量為n-1開始逐行遞減
#         print(' ',end='')
#     for k in range(0,i * 2 + 1,1):  #*則從0~2n+1
#         print('*',end='')
#     print()``

# for i in range(1,5,1):
#     print("*" * i)

# for i in range(4,0,-1):
#     print("*" * i)

a = int(input("輸入"))

# for i in range(1,a+1,1):
#     print("*" * i)

# for i in range(a,0,-1):
#     print("*" * i)

for i in range(1, a+1, 1):
    for j in range(1, 2*i, 1):
        print("*", end="")
    print()