# #定義函式
# def multiply(n1,n2):
#     print(n1+n2) #不會執行
#     return n1 + n2 #預設None 不寫retutn也會執行None
#     #呼叫函式
# #multiply(3,4)
# Value = multiply(3,4)
# print(Value)

def  calcukate(max):
    sum = 0
    for i in range(1,max+1):
        sum =sum+i
    print(sum)
calcukate(5)
calcukate(10)