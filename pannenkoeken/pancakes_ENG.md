# Baking pancakes

### Easy

In this unit you'll learn how to write a program that calculates how many pancakes you can make based on the amount of ingredients you have.

## Step 1

First we'll input the amount of eggs. In python there's a straightforward way to do this. With `input("<question>")` you can ask the user any question.

```python
input("How many eggs do you have? ")
```

But now we're not using the given info... We'll put it in a variable

```python
eggs = input("How many eggs do you have? ")
```

Now we can print this variable. If you put an f before your quotation marks (") python will fill in everything between the { }.

```python
eggs = input("How many eggs do you have? ")
print(f"You have {eggs} eggs.")
```

You'll see the value you gave in will replace `{eggs}` in the output.

But... there's a fault in our code. What happens when you try the following code?

```python
eggs = input("How many eggs do you have? ")
print(f"If you ate 2 eggs you'd still have {eggs -2}.")
```

You should get an error...

```
TypeError: unsupported operand type(s) for -: 'str' and 'int'
```

This is because python can't do math with an input, we can solve this issue by writing `int` in front of the input statement. That way python can do all kinds of calculations.

```python
eggs = int(input("How many eggs do you have? "))
print(f"If you ate 2 eggs you'd still have {eggs -2}.")
```

We'll always put the thing we want to turn into an int between brackets

Try to run the program and see what happens.

## Step 2

You'll need 3 ingredients for pancakes: eggs, milk and flour. So we'll have to ask three questions.

```python
eggs = int(input("Amount of eggs: "))
milk = int(input("ml milk: "))
flour = int(input("grammes of flour: "))
```

Check if everything works by printing every value.

```python
print(f"Eggs: {eggs}, milk: {milk}, flour: {flour}.")
```

For every ingredient we'll calculate how many pancakes we can make with that amount, then we'll take the lowest amount since you'll have enough of everything else for the lowest amount.

Below you'll find the calculations for every ingredient. Multipilication in python is done with `*` and devision with `/`. But we'll use `//` to divide without comma, were not gonna make 0.33333 pancakes!

```python
eggsForPancakes = eggs*4
milkForPancakes = milk//30
flourForPancakes = flour//12.5
```

We need to pick the lowest of these values. With what would we do this?

1. `max(1, 2, 3)` Picks the maximum, so 3
2. `print(1, 2, 3)` Prints "1 2 3"
3. `min(x, y, z)` Picks the minimum so 1
4. `sum(x, y, z)` Calculates the sum, so 6

If you hadn't guesses, the answer is `min()`. We'll take the minimum of the 3 values. We'll put this value in a variable.

```python
eggs = int(input("Amount of eggs: "))
milk = int(input("ml milk: "))
flour = int(input("grammes of flour: "))

eggsForPancakes = eggs*4
milkForPancakes = milk//30
flourForPancakes = flour//12.5

pancakeAmount = min(eggsForPancakes, milkForPancakes, flourForPancakes)
```

If you print this variable you'll see how many pancakes you can make!

## Step 3

If you don't have enough flour of milk it could be that you have to make 0 pancakes, and that's not possible. We'll do a check to see if this is the case.

```python
if pancakeAmount < 1:
    print("Not enough for pancakes!")
```

If there is enough we'll just print the amount.

```python
if pancakeAmount < 1:
    print("Not enough for pancakes!")
else:
    print(f"You can make {pancakeAmount} pancake(s)")
```

## Extras for professional coders

1. The word "pancake(s)" could be better, can you code it so 1 pancake makes it "pancake" and more than 1 makes it "pancakes"?

2. For every pancake you need 5 grams of butter. Can you add butter to the code?

3. (ADVANCED) Can you print how much of the ingredients remain at the end?

4. (ADVANCED) Rewrite the code in 4 or less lines.

5. (CHALLENGING) Oneline the code.

## Examplecode

```python
eggs = int(input("Amount of eggs: "))
milk = int(input("ml milk: "))
flour = int(input("grammes of flour: "))

eggsForPancakes = eggs*4
milkForPancakes = milk//30
flourForPancakes = flour//12.5

pancakeAmount = min(eggsForPancakes, milkForPancakes, flourForPancakes)

if pancakeAmount < 1:
    print("Not enough for pancakes!")
else:
    print(f"You can make {pancakeAmount} pancake(s)")


```

### Solution oneline

```python
pancakeAmount = min(int(input("Amount of eggs: "))*4, int(input("ml milk: "))//30, int(input("grammes of flour: "))//12.5); print({True: "Not enough for pancakes!", False: f"You can make {pancakeAmount} pancake(s)"}[pancakeAmount < 1])
```
