import random
answer =  random.randint(1, 100)
user_answer = 0
print(answer)
i = 1 
r = 100
while user_answer != answer:
    try:
        user_answer = float(input(f"猜數字遊戲，請在{i}到{r}之間輸入一個數字:　"))
    except:
        print("你在蝦雞掰輸入")
        continue
    if user_answer < i or user_answer > r:
        print("???????")
    elif user_answer < answer:
        print("你的數字不夠大喔 ")
        i = user_answer
    elif user_answer > answer:
        print("你的數字很大喔")
        r = user_answer
    else:
        print("恭喜你答對囉")
    
