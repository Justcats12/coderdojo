# Quiz

### Easy

In this project we'll make a quiz, of which you can choose the questions! The player gets 3 lives, which means he can give 3 wrong answers.

## Step 1

We'll start with setting up the questions and answers. For this we'll use a _dictionary_ like shown here.

```python
quiz = {
    "In what language is this program?": "python",
    "What's the file extention for python files?": ".py",
}
```

You can of course make your own questions.

## Step 2

Now we'll go over every question and ask the player for the answer. For this we'll use a `for`-loop. After we'll ask the player the answer and store it in the vareable `answer`.

```python
# quiz = ...

for question in quiz:
    print(question)
    answer = input("Answer: ")
```

Now we can compare `answer` to the correct answer, which we'll find in `quiz[question]`.

```python
#for
    print(question)
    answer = input("Answer: ")

    correct = (answer == quiz[question])
```

`(answer == quiz[question])` is `True` or `False`. This boolean will be stored in `correct`.

## Step 3

As long as the answer is incorrect we'll keep repeating the question. For this we need a second kind of loop, a `while`-loop. We'll also show a message when the user isn't right.

```pythonthon
#for:
    correct = False
    while not correct:
        print(question)
        answer = input("Answer: ")

        correct = (answer == quiz[question])

        if not corrcect:
            print("Wrong.")
```

## Step 4

Now we'll make sure the player has 3 lives, and can give 3 wrong answers. If the player has no remaining lives, they'll be thrown out of the program. We'll start by setting a new vareable called `lives`and making its value 3.

```python
# quiz = {...}

lives = 3

# for ... :
```

Now we'll modify the while-loop so the user can't keep answering after losing all their lives.

```python
#for ... :
    correct = False
    while not correct and lives > 0:
        # If the player has more than 0 lives they may continue
        # code...


        # einde code
    if lives == 0:
        break #The player gets thrown out.
else:
    print("you win") # if you never get thrown out, you win!
```

Finaly we have to make sure the player loses a life afer getting an answer wrong.

```python
# for
    # while
        if not correct:
            lives -= 1
            print("Wrong, try again")
```

## Volledige code

```python
quiz = {
    "In welke taal is dit geschreven": "python",
    "Welke extensie gebruiken python bestanden?": ".py",
    "Waar of fout? Python is sneller in uitvoer dan Java.": "fout",
}

lives = 3

for question in quiz:

    correct = False

    while not correct and lives > 0:
        print(question)
        answer = input("Answer: ")

        correct = answer == quiz[question]

        if not correct:
            lives -=1
            print("Wrong, try again")
    if lives == 0:
        break
else:
    print("Good job you won!")
```
