# Hoger lager

### Gemakkelijk

Hoger lager is een spelletje waarbij de speler een getal moet raden, de enige hulp die hij krijgt is dat het getal hoger of lager is. Let's code it!

## Stap 1

Eerst en vooral hebben we een random getal nodig. In python noemen we een getal zonder komma een _integer_. Met `random.randint(x, y)` kunnen we een random getal genereren tussen x en y.

```python
import random

print("Lets play a game")
print("Guess my number or I will HACK YOUR COMPUTER")

number = random.randint(1,20)
```

De waarde van het random getal wordt gestoken in `number`. Dit is een vareabele dat we gebruiken om later aan ons getal te kunnen. Probeer eens uit te vogelen wat de waarde is met `print(number)`

## Stap 2

We geven de speler 5 kansen om het juiste getal te raden. Als je al in scratch hebt gewerkt ken je zeker de "herhaal x keer"-blok. Dit bestaat ook in python, maar het noemt een for-lus. Hier staat een voorbeeld van een for-lus.

```python
for i in range(10):
    print("Hello")
```

We willen ons programma 5 keer herhalen, en als de speler het juist heeft moet het direct stoppen. Moet het scratch zijn zou dit ingewikkeld worden. Maar in python is het eenvoudig.

```py
# Voorgaande code...

for i in range(5):
    guess = int(input("Guess number: "))

```

Zo vragen we 5 keer aan de gebruiker voor een getal, dit getal stoppen we telkens in `guess`. Hoe checken we nu of het juist is? Met een `if`-statement natuurlijk!

```py
# Voorgaande code...

for i in range(5):
    guess = int(input("Guess number: "))

    if guess == number:
        print("Correct!")
        break
```

Om twee waarden de vergelijken, gebruiken we `==`, één gelijkheidsteken is enkel om een waarde in een vareabele te stoppen. Na onze check gebruiken we `break` om uit de lus te gaan.

## Stap 3

Nu hebben we een spelletje waarbij de gebruiker een getal moet raden. Maar dit is niet hoger lager... We hebben nog wat ifs en elses nodig. Als we een tweede if statement willen toevoegen, gebruiken we `elif`. `else` gebruiken we pas als laatst, als er geen andere mogelijkheid meer overschiet.

```py
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

Uiteindelijk kunnen we ook aan de for-lus een `else` toevoegen. De code die onder deze `else` komt activeert enkel als de for-lus sucessvol eindigd. Anders gezegd, als deze niet onderbroken wordt door een `break`.

```py
for i in range(5):
    # code ...
else:
    print("You lose, hacking computer...")
```

## Voledige code

```py
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
