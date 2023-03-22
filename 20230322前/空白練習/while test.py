secret_word = "dog"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and guess_count < guess_limit: 
    if guess_count < guess_limit:
        guess = input("Enter guess(is 3 words): ")
        guess_count += 1

if guess == secret_word :
    print("you win")
else:
    print("you lose")