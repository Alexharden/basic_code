# sum = 0  #1+2+3... ...+10=
# for i in range(1,11):
#     sum += i
#     print(sum)
# print(sum)

# n = 0
# for x in [0,1,2,3]:
#     if x % 2 == 0:
#         continue
#     print(x)   #1 3
#     n += 1
# print("最後的 n: ", n) #2
 
# n = int(input("輸入一個正整數: "))
# for i in range(n): 
#     if i * i == n:
#         print("整數平方根" , i) 
#         break #強制終止 不會執行 else
# else:
#     print("沒有整數平方根")
n = 0
for i in [0,1,2,3,4,5,6,7,8]:
    if i % 2 ==0:
        n += 1
print(n)