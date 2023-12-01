# Quiz
**Nodige Kennis**: If statements, for loops<br>
**Wat leer je**: lists, while-loop
<br><br>
In dit project gaan we een quiz maken over jouw favoriete onderwerp! Bedenk al vast maar een aantal vragen!
## Deel 1 Vragen en antwoorden
We beginnen met onze vragen en antwoorden in twee aparte lijsten te zetten, zorg ervoor dat elke vraag op de zelfde plaats in de lijst staat als het antwoord.
```py
vragen = ["Vraag 1", "Vraag 2", "Vraag 3"]
antwoorden = ["Antwoord 1", "Antwoord 2", "Antwoord 3"]
```
Als je hierme klaar bent schrijf dan een `for`-lus die het antwoord van de gebruiker op elke vraag opslaat in een varabele. Gebruik `len(vragen)` om de for loop alle vragen te doen overlopen
```python
teller = 0
for i in range(len(vragen)):
    antwoord = input(vragen[teller])
    teller += 1
```
We hebben nu een teller geschreven om alle vragen af te gaan, maar deze hebben we niet nodig. omdat de for lus een ingebouwde teller heeft! Let wel op, dit werkt enkel omdat we `range([getal])` hebben gebruikt in de `for`-lus
```python
for i in range(len(vragen)):
    antwoord = input(vragen[i]) # teller wordt i
```
Nu moeten we nog checken of het antwoord juist is. Dit doen we natuurlijk met een `if`-statement
```python
#for ...
    antwoord = input(vragen[i]) # teller wordt i

    if antwoord == antwoorden[i]:
        print("Juist antwoord")
```
Voeg nu een `else`-statement met een `break` zodat het programa stopt bij een verkeerd antwoord.
```python
#for ...
    # ...
    if antwoord == antwoorden[i]:
        print("Juist antwoord")
    else:
        print("Je bent verloren!")
        break
```
Zo, de quiz is af! Als je nog levens wilt toevoegen aan jouw quiz, ga dan naar deel 2!
## Deel 2: Een serieuze quiz
Voeg eerst en vooral wat vragen toe, want we gaan ze nodig hebben! En maak een nieuw vareabele waarin je het aantal levens waarmee de speler begint meegeeft.
```python
vragen = ["..."]
antwoorden = ["..."]

levens = 3

#for ...
```
Nu nog ervoor zorgen dat de speler levens verliest, en niet direct uit het programma wordt gesmeten. Hiervoor voegen we een `elif`-statement toe aan onze code.
```python
#for ...
    # ...
    if antwoord == antwoorden[i]:
        print("Juist antwoord")
    elif levens > 0: # als de speler nog levens heefd => speler heeft meer dan 0 levens.
        print("Fout antwoord")
        levens -= 1 # verwijder ook een leven!
    else:
        print("Je bent verloren!")
        break
```
Het probleem waar we nu nog mee zitten is dat het spel wel een leven weg pakt, maar de speler mag nog steeds door naar de volgende vraag.
Hiervoor zullen we een while loop gebruiken. Maar eerst en vooral een niew vareable maken waar we in opslaan of het antwoord goed was.
```python
#for ...
    juist_antwoord = False
    antwoord = input(vragen[i])
    juist_antwoord = (antwoord == antwoorden[i])
```
nu kunnen we de waarde in `juist_antwoord` ook gebruiken in onze if statement. Anders hebben we dubbele code.

```py
#for ...
    juist_antwoord = False
    antwoord = input(vragen[i]) 
    juist_antwoord = (antwoord == antwoorden[i])
    if juist_antwoord:
        print("Juist antwoord")
    # ...
```
nu moeten we nog de hele boel herhalen tot er een juist antwoord wordt geraden. Dit doen we met een `while`-loop
```py
#for ...
    juist_antwoord = False
    while not juist_antwoord:
        antwoord = input(vragen[i]) 
        juist_antwoord = (antwoord == antwoorden[i])
        if juist_antwoord:
            print("Juist antwoord")
        # ...
```
Ziezo, je bent klaar!

```py
vragen = ["Wat is een haai? ", "Hoe noemt de haai van de Ikea? ", "Wat eet een haai? ", "Is een haai een dolfijn? "]
antwoorden = ["Een haai", "Blahaj", "vis", "nee"]
levens = 3

for i in range(len(vragen)):

    juist_antwoord = False

    while (not juist_antwoord) and (levens > 0) :

        antwoord = input(vragen[i])
        juist_antwoord = antwoord == antwoorden[i]

        if juist_antwoord:
            print("Goed antwoord")
        elif levens > 0:
            print("Fout antwoord, probeer opnieuw")
            levens -= 1
        else:
            print("Je bent verloren")
            break
```