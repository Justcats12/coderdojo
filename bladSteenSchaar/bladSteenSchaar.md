# Blad-Steen-Schaar

### gevorderd

Je kent zeker het spelletje blad-steen-schaar. Maar je hebt hier twee spelers voor nodig in het echt. We kunnen gelukkig een programma maken zodat we het tegen de computer kunnen spelen. Let's code it!

## Stap 1

De computer zal een random optie kiezen, dus import alvast `random`. We zullen alle opties ook in een list steken, waaruit de computer zal kiezen. We zullen de woorden ook afkorten. (Rock = r, paper = p, scissors = s)

```python
import random

options = ["r", "p", "s"]
# random keuze van de computer
computer = options[random.randint(0,2)]
```

Als volgt zullen we aan de speler vragen voor een optie. We moeten er wel voor zorgen dat die niet iets verkeerds ingeeft.

```python
# import
# options = ...

def prompt():
    #vraag input
    res = input("Rock (r), paper (p) or scissors (s)")
    # check of input correct is
    if res in options:
        # return de keuze
        return res
    else:
        # als niet correct vraag opnieuw
        return prompt()


computer = options[random.randint(0,2)]
choice = prompt()
```

Deze functie vraagt om invoer, checkt of deze goed is voor de ingegeven letter terug te geven. Als deze niet goed is, doet de functie zichzelf opnieuw.

## Stap 2

we zullen eerst nakijken of er geen gelijk spel is, pas daarna kunnen we beslissen wie is gewonnen.

```python
# voorgaande code

while computer == choice:
    print(f"{choice} vs {computer}. It's a draw!")
    computer = options[random.randint(0,2)]
    choice = prompt()

```

# Stap 3

Nu zullen we checken wie is gewonnen. We maken eerst een nieuwe list die toont welke optie tegen welke wint. Dus als `options[0]` -> `"r"`, dan moet `winsAgainst[0]` -> `"p"`

```python
import random

options = ["r", "p", "s"]
winsAgainst = ["p", "s", "r"]
```

Ten laatste doen we de check wie er is gewonnen.

```python
# voorgaande code...

print(f"{choice} vs {computer}!")

winsAgainst = ["p", "s", "r"]

if choice == winsAgainst[options.index(computer)]:
    print("Player wins")
else:
    print("Computer wins")
```

## Volledige code

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
    print(f"{choice} vs {computer}! It's a tie, try again!")
    choice, computer = prompt(), choose()

# check winner
print(f"{choice} vs {computer}!")

winsAgainst = ["p", "s", "r"]

if choice == winsAgainst[options.index(computer)]:
    print("Player wins")
else:
    print("Computer wins")

```
