# 參數的預設資料
# def power(base,exp=0):  次方
#     print(base ** exp)
# power(3,2)
# power(4)
# 使用參數名稱對應
# def divide(n1,n2): 除法
#     print(n1/n2)
# divide(2,4)
# divide(n2=2,n1=4)
#無限/不定 參數資料
def avg(*numbers): #平均
    sum = 0
    for n in numbers:
        sum =sum+n
    print(sum/len(numbers))
avg(1,2,3)
avg(2,4,6,8)
avg(1,3,5,6,7)

