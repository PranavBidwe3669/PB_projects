secret_number = 10
guess_count = 1
guess_limit = 3
print("welcome to the guessing number game..")
print("you have got 3 chances to guess the correct number..")
user_input = int(input("guess the number from 1 to 10: "))
while guess_count < guess_limit:
    user_input = int(input("take a guess: "))
    guess_count += 1
    if user_input == secret_number:
        print("you won! ")
        break
else:
    print("you have lost the game! ")