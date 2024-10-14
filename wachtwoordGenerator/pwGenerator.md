# Password Generator (Deel 1)

### gevorderd

Een sterk wachtwoord is heel belangrijk, maar als je een online generator gebruikt bestaat het risico dat de website jouw watchwoord ergens opslaat. Daarom zullen we onze eigen generator maken.

## Stap 1

Voor een willekeurig watchwoord zullen we de `random` bibliotheek nodig.

```python
import random
```

We kunnen hiermee willekeurige getallen genereren, maar geen willekeurige karakters. Daarom moeten we zelf de toegestane karakters instellen.

```python
TOEGESTANE_KARAKTERS = "abc..." # vul zelf verder aan
```

## Stap 2

Het wachtwoord genereren we in de functie `genereer_wachtwoord()`. Zo kunnen we deze functie oproepen waneer we willen, een beetje zoals een eigen blok maken in scratch.

```python
def genereer_wachtwoord():
    return 0
```

Tussen de haakjes zullen we een parameter stoppen, zodat we de lengte kunnen meegeven. bv. `genereer_wachtwoord(7)` -> "Xxu?5Id".

```python
def genereer_wachtwoord(lengte):
    return 0
```

Nu geeft de functie 0 terug, in de volgende stap zullen we zorgen dat er een wachtwoord terug geeft.

## Stap 3

We beginnen met een leeg watchtwoord, later zullen we karakters toevoegen.

```python
def genereer_wachtwoord(lengte):
    wachtwoord = ""

    return wachtwoord
```

Nu we een leeg watchtwoord hebben moeten we een aantal karaters toevoegen, namelijk het aantal dat werdt meegegeven. Dit getal kunnen we opvragen met de naam van de paramter (`lengte`).

! text na een # is commentaar en doet niets.

```python
def genereer_wachtwoord(lengte):
    wachtwoord = ""
    for i in range(lengte):
        # voeg karakter toe

    return wachtwoord
```

## Stap 4

Nu moeten we een karakter random selecteren en toevoegen. We kunnen aan een karakter in `TOEGESTANE_KARAKTERS` met een index bv `TOEGESTANE_KARAKTERS[15]` -> geeft het 16de karater van `TOEGESTANE_KARAKTERS`. (python begint bij 0 te tellen)

We kunnen een random getal als index gebruiken met `random.randint()`, we moeten meegeven tussen welke getallen een random getal gekozen moet worden.

```python
random.randint(0, <lengte van TOEGESTANE_KARAKTERS> - 1) # -1 omdat dit de hoogst mogelijke index is
```

We kunnen de lengte van `TOEGESTANE_KARAKTERS` opvragen met `len(TOEGESTANE_KARAKTERS)`

```python
def genereer_wachtwoord(lengte):
    wachtwoord = ""
    for i in range(lengte):
        random_index = random.randint(0, len(TOEGESTANE_KARAKTERS) -1)

    return wachtwoord
```

Nu moeten met de random index een karakter van `TOEGESTANE_KARAKTERS` opvragen. en het karakter aan het wachtwoord toevoegen

```python
def genereer_wachtwoord(lengte):
    wachtwoord = ""
    for i in range(lengte):
        random_index = random.randint(0, len(TOEGESTANE_KARAKTERS) -1)
        # kies random karakter
        random_char = ALLOWED_CHARS[random_index]
        wachtwoord += random_char
    return wachtwoord
```

Onze generator is nu af, nu moeten we hem enkel nog gebruiken.

## Stap 5

We vragen eerst aan de gebruiker hoeveel karakters het wachtwoord moet hebben. Hiervoor gebruiken we `input()`. We maken er ook direct een getal van.

```python
lengte_wachtwoord = int(input("Wachtwoord lengte: "))
```

Nu stoppen we een wachtwoord van die lengte in een vareable. Daarna tonen we het met een `print`-statement

```python
lengte_wachtwoord = int(input("Wachtwoord lengte: "))
random_wachtwoord = genereer_wachtwoord(lengte_wachtwoord)
print("Gegenereerd watchwoord:", random_wachtwoord)
```

In deel 2 berekenen we hoe lang het duurt om het wachtwoord te kraken.

## Oefeningen voor gevorderden

1. Hoe voeg ik extra karaters toe zoals `%` en `^` toe?

2. (moeilijk) Meeste websites willen dat je minstens één van elke soort (hoofdletter, kleine letter, getal, speciaal teken) gebruikt. Kun je ervoor zorgen dat dit telkens in het wachtwoord zit.

## Volledige code

```python
import random

ALLOWED_CHARS = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789*+-/!?.,;:&="

def generate_password(lenght):
    password = ""
    for i in range(lenght):
        random_index = random.randint(0, len(ALLOWED_CHARS) -1)
        random_char = ALLOWED_CHARS[random_index]
        password += random_char

    return password

input_lenght = int(input("Password lenght: "))
random_password = generate_password(input_lenght)
print("Randomly generated password:", random_password)
```
