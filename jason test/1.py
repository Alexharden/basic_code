import random

def system_answer():   
    answer = random.sample(range(10),4)
    answer = ''.join(map(str, answer))
    return answer

def is_valid(user_answer):
    if len(user_answer) > 4:
        return False
    if len(set(user_answer)) < 4:
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
def play_game():
    while True:
        answer = system_answer()
        user_answer = input("輸入一個不重複的四位數字: " )
        if not is_valid(user_answer):
            print("請輸入一個不重複的四位數字")
            continue
        result = check_answer(answer, user_answer)
        print(f"你的猜測結果是：{result}")
        if result == "4A0B":
            print(f"恭喜你猜中了答案！")
            break
        else:
            print(f"繼續猜阿")   
        
while True:
    play_game()
    again = input('是否再玩一次？（輸入y再玩一次，其他結束遊戲）')
    if again.lower() == 'y':
        continue
    else:
        print('遊戲結束，謝謝遊玩！')
        break
        
