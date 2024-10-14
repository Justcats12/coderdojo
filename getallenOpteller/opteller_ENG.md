# Number adder

### Easy

Python is very usefull in math because it's very fast at it. This program takes a number and adds every digit in it. e.g. 4637195 -> 4 + 6 + 3 + 7 + 1 + 9 + 5 = 35 -> 3 + 5 = 8

## Step 1

First set the number we want to add together, we'll call it `number`.

```python
number = 123456789987654321
```

We'll now make a new function where we can give a parameter. This works like a custom block in scratch.

```python
def addDigits(integer):
    return 0
```

This function returns 0 for now, if you execute the following code you'll see 0 in the terminal.

```python
print(addDigits(number))
```

## Step 2

We'll now work inside of the function, indent everthing that is in the function with 1 tab (↹)

**VOORBEELD**

```python
def addDigits(integer):
    # in the function


    # also within the function

# outside of the function
```

IMPORTANT everything that's behind a `#` does nothing, it's just a comment.

First we have to make sure we can read the number digit by digit. We can do this with the built in function `str(<integer>)`. We'll put this tring in a variable.

```python
def addDigits(integer):
    string = str(integer)

    return 0
```

We can now use a for-loop to go over every digit. To test if this actually works we'll print all of them first.

To write inside of the for loop we'll have to indent with an extra tab.

```python
def addDigits(integer):
    string = str(integer)

    for digit in string:
        print(digit)

    return 0
```

Now try the following bit of code at the end of the program.

```python
addDigits(integer)
```

If everything went smoothly every digit in `number` should appear in the console.

You can remove this bit of code when you're done testing.

## Step 3

We don't have to print the digits but add them together. Remove the print statement, we'll replace it.

The sum of all digits starts at 0, so well make a variable `sumDigits` and set it to 0.

```python
def addDigits(integer):
    string = str(integer)
    sumDigits = 0
    for digit in string:
        # ...

    return 0
```

After we'll have to turn every digit back into an int, because we can't add a string to `sumDigits`. If you want to know why read the following text.

### Difference between a string and integer

A string is a combination of characters, while an integer is a whole number. In short:

- 1 + 1 = 2
- "1" + "1" = "11"
- "1" + 1 = error

With this in mind we'll have to use `int(<string>)` to turn digit into an integer.

```python
def addDigits(integer):
    string = str(integer)
    sumDigits = 0
    for digit in string:
        sumDigits = sumDigits + int(digit)

    return 0
```

You can make the code we just added even shorter. Here's an example

**VOORBEELD**

```python
x = 2
y = 2

x = x + 5

y += 5

print(x) # 7
print(y) # 7

```

Finally we have to edit the last line of the function. We don't return `0` but `sumDigits`

```python
def addDigits(integer):
    string = str(integer)
    sumDigits = 0
    for digit in string:
        sumDigits = sumDigits + int(digit)

    return sumDigits  # <--
```

Now we can test this by printing the result

```python
print(addDigits(number))
```

Normally there should appear 45 in de terminal.

## Step 4

We now want to keep adding this 45 as 4 + 5. This step should get repeated for every number until only 1 digit remains.

We'll do a check to see if the number is 9 or less, if it's not the function calls itself.

```python
def addDigits(integer):
    string = str(integer)
    sumDigits = 0
    for digit in string:
        sumDigits = sumDigits + int(digit)
    if sumDigits <= 9:
        return sumDigits
    else:
        return addDigits(sumDigits)
```

Finally we'll put the result in a variable and print it neatly.

```python
result = addDigits(number)
print("The result is", result)
```

We call this a recursive function, this is easy in python but not so much in scratch.

Calculate the result for the following digits

- `999888777` (9)
- `1010101010` (5)
- `15975345685215987412563` (3)
- `1234567891011121314151617181920` (3)

## Exercises for pros

1. Instead of putting `number` in the code, try asking for input every time you run the code.

2. What do you see if you enter any multiple of 9?

3. What if you want a result of at least 2 digits?

4. (EXTRA) can you make it work for numbers with a comma or negative numbers?

## Entire code

```python
number = 999999

def sumNumbers(number):
  string = str(number)
  sum = 0
  for n in string:
    sum += int(n)

  if sum <=9:
    return sum
  else:
    return sumNumbers(sum)


result = sumNumbers(number)

print("The result is", result)
```
