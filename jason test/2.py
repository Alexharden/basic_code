import random

# 產生一個不重複的四位數字作為答案
def generate_number():
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(str(d) for d in digits[:4])

# 檢查使用者輸入的數字是否合法
def is_valid_input(user_input):
    if len(user_input) != 4:
        return False
    if not user_input.isdigit():
        return False
    if len(set(user_input)) != 4:
        return False
    return True

# 比較答案和使用者輸入的數字，返回結果（例如"2A1B"）
def compare_numbers(answer, user_input):
    a = 0
    b = 0
    for i in range(4):
        if answer[i] == user_input[i]:
            a += 1
        elif answer[i] in user_input:
            b += 1
    return "{}A{}B".format(a, b)

# 主要的遊戲邏輯
def play_game():
    answer = generate_number()
    max_guesses = 10
    num_guesses = 0

    while num_guesses < max_guesses:
        user_input = input("請輸入一個不重複的四位數字：")
        if not is_valid_input(user_input):
            print("輸入無效，請重新輸入。")
            continue

        num_guesses += 1
        result = compare_numbers(answer, user_input)
        print("猜測結果：{}".format(result))

        if result == "4A0B":
            print("恭喜你猜中了！")
            return True

    print("很遺憾，你沒有在限定次數內猜中。答案是{}。".format(answer))
    return False

# 開始遊戲
while True:
    play_game()
    play_again = input("想再玩一次嗎？輸入 Y 以繼續，其他任意鍵退出。")
    if play_again.lower() != "y":
        break
