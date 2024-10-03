# Rock-paper-scissors

### intermediate

You probably know the game of rock-paper-scissors. But sadly you need two players to play this game. Luckily we can make a program in pythong so you can play against your computer. Let's code it!

## Step 1

The computer will choose a random option, so certainly import `random`. We'll put all the options in a list, from which the computer shall choose. Note that for this program we're abreviating the words. (Rock = r, paper = p, scissors = s)

```python
import random

options = ["r", "p", "s"]
# random choice of the computer
computer = options[random.randint(0,2)]
```

Now we'll ask the player for their choice. Make sure they don't give in an invalid option.

```python
# import
# options = ...

def prompt():
    # ask input
    res = input("Rock (r), paper (p) or scissors (s)")
    # check if input is correct
    if res in options:
        # return the choice
        return res
    else:
        # if not correct ask again
        return prompt()


computer = options[random.randint(0,2)]
choice = prompt()
```

This function asks for input, checks if it's correct before returning the given letter. If it's incorrect, the function calls itself.

## Step 2

Now we'll check if there's no draw before checking if anyone won.

```python
# previous code

while computer == choice:
    print(f"{choice} vs {computer}. It's a draw!")
    computer = options[random.randint(0,2)]
    choice = prompt()

```

# Step 3

We'll check for the winner. First off we'll make a new list that shows us which option beats which. For example, if `options[0]` -> `"r"`, then `winsAgainst[0]` -> `"p"`

```python
import random

options = ["r", "p", "s"]
winsAgainst = ["p", "s", "r"]
```

Now we can easily check for who won.

```python
# Previous code...

print(f"{choice} vs {computer}!")

winsAgainst = ["p", "s", "r"]

if choice == winsAgainst[options.index(computer)]:
    print("Player wins")
else:
    print("Computer wins")
```

## Entire code

```python
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

```
