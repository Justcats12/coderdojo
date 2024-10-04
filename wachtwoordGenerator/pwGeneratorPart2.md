# Password Generator (Deel 2)

### moeilijk

Nu we een wachtwoord hebben kunnen we berekenen hoe lang het zal duren voor dit te genereren

## Stap 6

Een computer voert instructies uit, maar hoeveel instructies per seconde hangt af van computer tot computer. Je kan testen hoe snel jouw computer is als je een nieuw python bestand aanmaakt en de volgende code uitvoert.

```python
import time
n,c=time.time(),0
while n + 1 > time.time():
    c+=1
print(c)
```

Nu kan je het terug gaan naar het vorige bestand en dit in een constante steken. Als voorbeeld zal ik 8 miljoen pakken. Ook moeten we weten hoveel instructies nodig zijn om elk mogelijk karakter af te gaan. Dit is gewoon de lengte van `TOEGESTANE KARAKTERS`

```python
IPS = 8000000
INSTRUCTIES_VOOR_ALLE = len(TOEGESTANE_KARAKTERS)

```

## Stap 7

Nu zullen we een nieuwe functie maken om de tijd te berekenen om een wachtwoord te kraken. Maar eerst moeten we de logica erachter snappen.

### Brute force attack

![slot](image.png)

Stel dat we dit hangslot willen openbreken, dan zouden we alle codes proberen beginnende bij 0000. Dan zouden we het eerste cijfer op elk getal zetten en daarna zouden we pas het tweede cijfer naar omhoog draaien.

Een wachtwoord wordt op dezelfde manier gekraakt. We beginnen bij de eerste letter op elke positie en pas als we alle mogelijke karakters zijn afgegaan veranderen we het volgende karakter.

Bijvoorbeeld als we een wachtwoord van 8 karakters hebben zullen we beginnen bij `AAAAAAAA` -> `AAAAAAAB` -> `AAAAAAAC` -> `AAAAAAAD` -> ... -> `AAAAAABA` -> `AAAAAABB` -> ...

Zo kunnen we berekenen hoeveel mogelijke wachtwoorden er zijn. Als we berekenen hoeveel wachtwoorden zullen afgegaan worden alvorens ons wachtwoord geraden zal worden.

### De code

We beginnen met een simpele functie waarin we de instructies tellen. We gaan het wachtwoord als parameter meegeven.

```python
def bereken_tijd(wachtwoord)
    instructies = 0

    return instructies/IPS
```

Nu gaan we elk karakter in het wachtwoord afgaan en opvragen het hoeveelste karakter dit nu is. Dit kunnen we doen door de index op te vragen van het karakter in `TOEGESTANE_KARAKTERS`

```python
def bereken_tijd(wachtwoord)
    instructies = 0
    for c in wachtwoord:


        instructies += TOEGESTANE_KARAKTERS.index(c)

    return instructies/IPS
```

Er mist nog iets...

Als we meerdere karakters hebben zal het langer duren het voorste karakter juist te krijgen. Voor de plaats erna zou namelijk elk karakter al afgegaan zijn. Daarom moeten we `instructies` telkens maal `INSTRUCTIES_VOOR_ALLE` alvorens het huidige karakter erbij op te tellen. (`x *= 2` is kort voor `x = x*2`)

```python
def bereken_tijd(wachtwoord)
    instructies = 0
    for c in wachtwoord:
        instructies *= INSTRUCTIES_VOOR_ALLE

        instructies += TOEGESTANE_KARAKTERS.index(c)

    return instructies/IPS
```

Nu kunnen we het aantal seconden berekenen, probeer dit eens voor een wachtwoord

```python
seconds = bereken_tijd("bazinga123")
print(seconds)
```

225255890588.85614 seconden is wat veel om in perspectief te zetten... We moeten dit omrekenen naar een iets langere periode. Geen uren, geen dagen, geen maanden maar jaren.

```python
seconds = bereken_tijd("bazinga123")
minutes = seconds/60
hours = minutes/60
days = hours/24
months = days/30
years = days/365.25
print(f"{seconds} seconden")
print(f"{minutes} minuten")
print(f"{hours} uur")
print(f"{days} dagen")
print(f"{months} maanden")
print(f"{years} jaren")
```

Voor het wachtwoord "bazinga123" kom ik ongeveer 7138 jaar uit. In werkelijkheid ligt dit lager omdat dit wachtwoord enkel geen hoofdletters of speciale tekens bevat. Dit wachtwoord zou namelijk maar 9 jaar duren als de kraker dit weet.

Zo kun je een aantal experimenten doen. Kun je de volgende scenarios berekenen?

| Wachtwoord         | Toegestane karakters    |
| ------------------ | ----------------------- |
| 5656               | Alle nummers            |
| coderdojo          | a-z (geen hoofdletters) |
| Coderd0j0          | a-z A-Z 0-9             |
| Python!!!          | A-Z a-z ? ! . \* + =    |
| letmein            | e, i, l, m, n, t        |
| H@ck3rW4chtW00rd\* | a-z A-Z 0-9 @ \* ! &    |
