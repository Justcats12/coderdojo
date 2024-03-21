import random

options = ["r", "p", "s"]

def choose():
    return options[random.randint(0,2)]

def prompt():
    res = input("rock (r), paper (p) or scissors (s): ")
    if res in options:
        return res
    else:
        print("Not an option!")
        return prompt()

# ask input
choice = prompt()
computer = choose()

while (choice == computer):
    print(f"{choice} vs {computer}! It's a draw, try again!")
    choice, computer = prompt(), choose()

# check winner
print(f"{choice} vs {computer}!")

winsAgainst = ["p", "s", "r"]

if choice == winsAgainst[options.index(computer)]:
    print("Player wins")
else:
    print("Computer wins")
