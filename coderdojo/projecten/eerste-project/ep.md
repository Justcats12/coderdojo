# Eerste project
**Nodige Kennis:** Geen<br>
**Wat leer je:** Invoer & uitvoer, if statements, for loops
## Deel 1: Juiste naam
Voor het eerste project gaan we een programa maken dat enkel jou toelaat. Hier onder zie je voorbeeld uitvoer.
```
-- juiste naam --
Wat is jouw naam? Alice
Hallo Alice
-- foute naam --
Wat is jouw naam? Carol
Jij mag niet binnen
```

Om te beginnen vragen we de gebruiker om hun naam. We stoppen dit in een vareabele

```python
naam = input("Wat is jouw naam? ")
```

als je nu `print(naam)` gebruikt verschijnt de ingegeven naam in de console. Dit betekend dat het antwoord op de vraag in het vareabele "naam" zit.

```
Wat is jouw naam? Alice
Alice
```
We gaan nu checken of de waarde die in `naam` zit jouw naam is of niet. dit doen we met een "if-statement"

```python
if naam == "Carol": #een naam die niet jouw naam is
    print("Jij mag niet binnen")
```
Deze code checkt enkel voor één naam jammer genoeg, we moeten checken of de naam niet jouw naam is.

```python
if naam != "Alice": #jouw naam
    print("Jij mag niet binnen")

```
Nu moeten we nog beslissen wat er gebeurt als jouw naam wel juist is. Schrijf onder de if statement een compleet nieuwe lijn en hier moet niets staan belalve `else:`
```python
if naam != "...":
    print("...")
else: #<-- else komt hier
    #spring in met de tab toets om in de else te schrijven
```
onder de else schrijf je nu wat er moet gebeuren als de naam wel juist is, in dit voorbeeld gaan we gewoon "Hallo \<naam\>" laten verschijnen maar je kan alles doen wat je wilt (en kunt).

Voor het voorbeeld van hallo naam gebruiken we een *formatted string*, of anders gezegd, een zin die python nog moet invullen. Deze ziet er als vogld uit: `f"Letterlijke tekst {variable}"`
In ons voorbeeld
```python
else:
    print(f"Hallo {naam}")
```
Dat was deel 1! Als je nu nog een wachtwoord wilt toevoegen aan jouw programma om het veiliger te maken, ga dan naar deel 2!
```python
naam = input("Wat is jouw naam? ")
if naam != "Alice":
    print("Jij mag niet binnen")
else:
    print(f"Hallo {naam}!")
```

## Deel 2: Wachtwoord alstublieft
Om te beginnen moeten we een wachtwoord opstellen. Het voorbeeld gebruikt 1234 maar jij bedenkt mischien een betere code. Stop de code in een vareabele bovenaan de code
```python
code = 1234
```
De rest van het programa schrijven we onder de `else:`. Vraag alvast de gebruiker voor het wachtwoord. Stop de poging in een vareable.
```python
else:
    poging = input("Geef wachtwoord: ")
    #...
```
We kunnen nu op dezelfde manier nagaan of het wachtwoord juist was, gebruik hiervoor een `if` statement.
```python
else:
    poging = input("Geef wachtwoord: ")
    if poging == code:
        #...
```
Als je nu het programa laat werken zal het crashen... <br>
dit komt omdat de waarde die in `code` zit een getal is en de waarde die in `poging` zit een woord is. Je kent misschien het gezegde "geen appels met peren vergelijken". Wel, in python mag je geen getallen met woorden vergelijken!
Daarom moeten we eerst aan python zeggen om van `code` een woord te maken. Dit doen we met de functie `str()`.
```python
#...
    if poging == str(code):
        #...

```
Ten laatste kunnen we er voor zorgen dat de gebruiker 3 pogingen heeft om de code te raden. Hiervoor gebruiken we een `for` lus.
```python
else:

    for i in range(3): # for lus

        poging = input("Geef wachtwoord: ")
        if poging == code:
            #...
```
We zijn er bijna! Enkel nog zeggen aan python dat hij moet stoppen met herhalen als het wachtwoord juist is geraden. Hiervoor gebruiken we het woordje `break`.
```python
else:
    for i in range(3):
        poging = input("Geef wachtwoord: ")
        if poging == code:
            print("...")

            break
```
Check na of alles werkt, goed geprogrameerd!

```python
naam = input("Wat is jouw naam? ")
code = 1234


if naam != "Alice":
    print("Jij mag niet binnen")
else:
    for i in range(3):
        poging = input("Geef wachtwoord: ")
        if poging == str(code):
            print(f"Hallo {naam}")
            break
```
