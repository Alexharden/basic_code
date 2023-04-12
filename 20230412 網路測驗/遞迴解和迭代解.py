# #https://ithelp.ithome.com.tw/articles/10242602
# #遞迴 + 優化執行
# import functools
# @functools.lru_cache(maxsize=None) # 用@開頭的稱為裝飾器，有興趣的讀者可再深入了解。
# def cs(n):
#     if n == 1 or n == 2:    #cs(1)=1 cs(2)=2 
#         return n
#     return cs(n-1) + cs(n-2)  #cs(3)=cs(3-1)+cs(3-2)=cs(2)+cs(1)=3  cs(4)= cs(3)+cs(2) =3+2 cs(5) =cs(4)+cs(3)=5+3

# for i in range(1, 10):
# 	print(cs(i))
        

#迭代 
def cs(n):
    if n == 1 or n == 2:  #cs(1)=1 cs(2)=2
        return n
    s1, s2 = 1, 2

    for i in range(n - 2): #cs(3)=執行rang(1) 
        # Python的賦值是會一起看開始前的值來計算
        # 所以不會因為s1的值變s2了, s2新的值就變成s2+s2
        s1, s2 = s2, s1 + s2
       
    return s2

a = int(input("請輸入數字: "))

for i in range(1,a+1):
    print(cs(i))



def cs(n):
    
    s1, s2 = 1, 2
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    else:
        print(1)
        print(2)
        for i in range(n-2):
        
            s1, s2 = s2, s1 + s2
            
            print(s2)  # 加上這行印出每一次執行的s2
        return s2

a = int(input("請輸入數字: "))
cs(a)
