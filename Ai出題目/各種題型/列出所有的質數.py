# n = int(input("請輸入一個正整數："))
# if n <= 0:
#     print("輸入錯誤，請輸入正整數。")
# else:
#     primes = []
#     for i in range(2, n+1):
#         is_prime = True
#         for j in range(2, int(i**0.5)+1):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(str(i))
#     print(primes)




# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:  # 整除，i 是 n 的因數，所以 n 不是質數。
#             return False
#     return True     # 都沒有人能整除，所以 n 是質數。

# n = int(input("輸入一個數字: "))  # 得到輸入值 n。

# for i in range(2, n + 1):   # 產生 2 到 n 的數字。
#     i_is_prime = is_prime(i)    # 判斷 i 是否為質數。
#     if i_is_prime:              # 如果是，印出來。
#         print(i, end = " ") #同一行列印




        

    

