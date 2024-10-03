# Higher-lower

### Easy

Higher-lower is a game where the player has to guess a number, their only help is knowing if the number is higher or lower. Let's code it!

## Step 1

First of we need a random number. In python we call a number with no comma an _integer_. With `random.randint(x, y)` we can generate a random number between x and y

```python
import random

print("Lets play a game")
print("Guess my number or I will HACK YOUR COMPUTER")

number = random.randint(1,20)
```

The value of the random number will be stored in `number`. This is a vareable that we can use later to access our number. You can try figuring out the value with `print(number)`

## Step 2

We'll give the player 5 tries to guess the right number. If you've worked with scratch, you probably know the "repeat x times" block. This also exists in pythong, only we call it a for-loop. Below is an example.

```python
for i in range(10):
    print("Hello")
```

Now, we want to repeat our program 5 times. And when the player guesses correctly it has to stop the loop. If this were scratch it'd get complicated, but luckily it's not.

```python
# Previous code...

for i in range(5):
    guess = int(input("Guess number: "))

```

This is how we ask the player 5 times for a number, we'll put this number in `guess`. But how do we check if it's correct or not? With `if`-statements of course!

```python
# Previous code...

for i in range(5):
    guess = int(input("Guess number: "))

    if guess == number:
        print("Correct!")
        break
```

To compare two values we use `==`, one equal sign is only used to store a value in a varaible. After our check we use `break` to interupt the loop.

## Step 3

Now we have a game where the player has to guess a number. This isn't higher-lower... We need some more ifs and elses. If we wanna add a second statement to our `if`-statement, we use `elif`. We use `else` when no other possibilities remain.

```python
#for ...
    # ...
    if guess == number:
        print("Correct!")
        break
    elif guess > number:
        print("Try lower")
    else:
        print("Try higher")
```

We can also add an `else` to our for-loop. The code under this `else` will only activate if the for-lus ends succesfully. So if no `break` was used to interupt it.

```python
for i in range(5):
    # code ...
else:
    print("You lose, hacking computer...")
```

## Complete code

```python
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
```
