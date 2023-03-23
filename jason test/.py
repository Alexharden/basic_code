import random

def system_answer():   
    answer = random.sample(range(10),4)
    answer = ''.join(map(str, answer))

def is_valid(user_answer):
    if len(user_answer) != 4:
        return  False
    if len(set(user_answer)) != 4:
        return False
    return True
def check_answer(answer, user_answer):
    a = 0
    b = 0
    for i in range(4):
        if user_answer[i] == answer[i]:
            a += 1
        elif user_answer[i] in answer:
            b += 1
    return(f"{a}A {b}B")
while True:
    answer = system_answer()
    user_answer = input("輸入一個不重複的四位數字: " )
    if not is_valid(user_answer) or not user_answer.isdigit():
        print("你他媽在輸入什麼洨")
        continue
    result = check_answer(answer, user_answer)
    print(f"你的猜測結果是：{result}")
    if result == "4A0B":
            print(f"恭喜你猜中了答案！")
    else:
        print(f"繼續猜阿")       
    
    play_again = input("你想再玩一次嗎？輸入 y 重新開始，輸入其他任何鍵結束遊戲。")
    if play_again.lower() != "y":
        break
print("謝謝遊玩，再見！")

