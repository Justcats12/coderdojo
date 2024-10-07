# Quiz

### Makkelijk

In dit project maken we een quiz, waarvan de de vragen zelf mag kiezen! De speler krijgt 3 levens, wat betekent dat hij 3 foute antwoorden mag geven.

## Stap 1

We beginnen met de vragen en antwoorden op te stellen. We doen dit in een _dictionairy_ op de volgende manier.

```python
quiz = {
    "In welke taal is dit geschreven": "python",
    "Welke extensie gebruiken python bestanden?": ".py",
}
```

De vragen mag je natuurlijk zelf kiezen.

## Stap 2

Nu gaan elke vraag overlopen en de speler om een antwoord vragen. Hiervoor gebruiken we een `for`-lus. Daarna vragen we de speler voor het antwoord. We houden het antwoord bij in het vareabele `answer`.

```python
# quiz = ...

for question in quiz:
    print(question)
    answer = input("Answer: ")
```

Nu kunnen we `answer` vergelijken met het juiste antwoord, wat we vinden in `quiz[question]`.

```python
#for
    print(question)
    answer = input("Answer: ")

    correct = (answer == quiz[question])
```

`(answer == quiz[question])` is `True` of `False`. De waarde van deze vergelijking stoppen we in `correct`.

## Stap 3

Zolang het antwoord fout is blijven we het herhalen. Hiervoor gebruiken we een andere soort lus, de `while`-lus. We zullen ook een gepast bericht tonen aan de gebruiker als hij het fout heeft.

```pythonthon
#for:
    correct = False
    while not correct:
        print(question)
        answer = input("Answer: ")

        correct = (answer == quiz[question])

        if not correct:
            print("Wrong.")
```

## Stap 4

Nu zullen we zorgen dat de speler 3 levens heeft, en dus 3 foute antwoorden kan geven. Als de speler geen levens meer heeft, wordt hij uit het programma gestuurd. We beginnen alvas met in het begin een nieuw vareabele te maken `levens` en het op 3 te zetten.

```python
# quiz = {...}

lives = 3

# for ... :
```

We zullen nu de while lus aanpassen zodat de speler niet verder kan antwoorden als hij geen levens meer heeft.

```python
#for ... :
    correct = False
    while not correct and lives > 0:
        # als de speler meer dan 0 levens heeft mag hij doordoen
        # code...


        # einde code
    if lives == 0:
        break #de speler wordt uit de for-lus gesmeten.
else:
    print("you win") # als je er noot wordt uitgesmeten, win je!
```

Als laatste moeten we er nog voor zorgen dat de speler een leven verliest als hij verkeerd antwoord.

```python
# for
    # while
        if not correct:
            lives -=1
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
