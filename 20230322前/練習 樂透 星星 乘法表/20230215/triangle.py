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
#正直角三角形 層數跟星星數相等
# for i in range(1,a+1,1):  i 起始是1 range 取頭不取尾 取到前一位 變數+1 才會使 輸入變數和層數相等
#     print("*" * i)
#正直角三角形 層數跟星星數相等
for i in range(a): #range(0,a,1) (0,5,1)  #層數
    print("*" * (i+1)) #第一次i =0 層數+1 

#倒直角三角形   輸入幾個 第一層就是幾顆 
# for i in range(a,0,-1):  range 取頭不取尾 所以起始值==變數 終止值取到 前一位 最後一層一定要印一顆 所以取0 前一位的值
#     print("*" * i)
# for i in range(a): #range(start:0, stop:a, step:1) 預設
#     print("*" *(a-i)) #range(0,5,1) 跑 0 1 2 3 4 五次 所以第一層是5顆 第二層i+1 跑 1234 4次 i=2 234 3次 i=3 34兩次 i=4 4 1次


#正直角三角形 第一層為一顆 後面層數規律增加顆數
# #第一層1顆、第二層3顆... 
# for i in range(1, a+1, 1): #層數
#     for j in range(1, 2*i, 1): #星星數量
#         print("*", end="") #印出星星不換行
#     print() #換行
# #i=1 1顆 i=2 4顆 i=3 7顆
# for i in range(1, a+1, 1): #層數
#     for j in range(1, 3*i-1, 1): #星星數量 數學3i-2 但 range 取頭不取尾 會+1  3i-1
#         print("*", end="") #印出星星不換行
#     print() #換行
# #i=1 1顆 i=2 5顆 i=3 9顆
# for i in range(1, a+1, 1): #層數
#     for j in range(1, 4*i-2, 1): #星星數量 數學4i-3 但 range 取頭不取尾 會+1  4i-2
#        print("*", end="") #印出星星不換行
#     print() #換行

