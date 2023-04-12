import random
answer = random.randrange(101)
print(answer)
user_answer = 0
i = 1
r = 100
while user_answer != answer:
    try:
        user_answer = int(input(f"猜數字遊戲 輸入一個數字在{i} 到 {r}之間: "))
    except:
        print("請輸入正常數字喔")
        continue #回到迴圈開始
    if user_answer <i  or user_answer>r:
        print("?????")
    elif user_answer < answer:
        print("你猜的數字比答案小喔")
        i = user_answer
    elif user_answer > answer:
        print("你猜的數字比答案大喔")
        r = user_answer
    else:
        print("恭喜你猜中答案了")









