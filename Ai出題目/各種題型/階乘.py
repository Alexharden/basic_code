num = int(input("輸入一個數字: "))
answer = 1
for i in range(1,num+1):
    answer = i * answer
print(answer)