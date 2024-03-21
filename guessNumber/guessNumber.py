import random

print("Let's play a game")
print("Guess my number (1-20)")
print("You have 3 chances")

number = random.randint(1,20)

for i in range(3):

    guess = int(input("Guess: "))

    if guess == number:
        print("Fine you win.")
        break
    elif guess > number:
        print("Try lower...")
    else:
        print("Try higher")
else:
    print("You lose, hacking computer...")