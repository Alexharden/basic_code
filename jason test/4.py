import random
game = "y"

while game == "y":
    answer = random.sample(range(10),4)
    print(answer)
    
    max_guess = 3
    guess_count = 0

    while guess_count <= max_guess:
        guess = input("輸入你要的四位數")
        if len(guess) !=4:
            print("你輸入的數字不是四位數")
            continue
        if len(set(guess)) !=4:
            print("你輸入的數字有重複喔")
            continue
    if answer == guess:
        print("你猜中了")
    else:
        for i in range(4)
    a = 0 
    b = 0
    