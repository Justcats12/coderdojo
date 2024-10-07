# Getallen Opteller

### Makkelijk

Python wordt heel vaak gebruikt om te rekenen, en hier is het ook heel goed in. Dit programma neemt een getal en telt alle cijfers hier in op, en het kan dit heel snel. Bv 4637195 -> 4 + 6 + 3 + 7 + 1 + 9 + 5 = 35 -> 3 + 5 = 8

## Stap 1

Stel eerst het getal in dat we willen optellen, dit zullen we `nummer` noemen

```python
nummer = 123456789987654321
```

Daarna zullen we een functie maken waarin we een getal als parameter kunnen meegeven.

```python
def optellengetallen(getal):
    return 0
```

Nu geeft deze functie 0 terug, als je de onderstaande code zal uitvoeren zul je 0 in de terminal zien.

```python
print(optellengetallen(nummer))
```

## Stap 2

We gaan nu binnen de functie werken, alles dat binnen de functie moet gebeuren moet met 1 tab toets (↹)

**VOORBEELD**

```python
def optellengetallen(getal):
    # binnen de functie


    # ook binnen de functie

# buiten de functie
```

BELANGRIJK dingen die achter een `#` staan doen niets, dit is gewoon comentaar.

Het eerste wat we moeten doen is ervoor zorgen dat we het getal cijfer per cijfer kunnen lezen. Dit kunnen we doen door er een string van te maken met `str(<getal>)`. Deze string slaan we op in een vareable.

```python
def optellengetallen(getal):
    string = str(getal)

    return 0
```

Nu kunnen we elke letter afgaan met een for-lus. Om te testen of dit werkt zullen we ze eerst allemaal eens printen.

Voor in de for-lus code te steken moeten we een extra tab ervoor schrijven.

```python
def optellengetallen(getal):
    string = str(getal)

    for cijfer in string:
        print(cijfer)

    return 0
```

Probeer nu eens de volgende code uit te voeren helemaal onderaan.

```python
optellengetallen(nummer)
```

Normaal zouden alle cijfer van `nummer` na elkaar moeten geprint worden in de console.

Je mag dit laatste stukje code weer wegdoen eens je getest hebt.

## Stap 3

We moeten de getallen niet printen maar optellen. Doe de print statement weg, we zullen deze vervangen.

De som van de getallen begint bij 0, dus we zullen een vareable `som` maken en het op 0 instellen.

```python
def optellengetallen(getal):
    string = str(getal)
    som = 0
    for cijfer in string:
        # ...

    return 0
```

Daarna zullen we het cijfer terug een int maken, omdat we bij `som` geen string kunnen optellen. Lees hieronder waarom.

### Verschil tussen string en int

Een string is een combinatie van karaters, een int is een geheel getal. In het kort uitgelegd:

- 1 + 1 = 2
- "1" + "1" = "11"
- "1" + 1 = error

Daarom moeten we met `int(<string>)` opnieuw een int maken van cijfer.

```python
def optellengetallen(getal):
    string = str(getal)
    som = 0
    for cijfer in string:
        som = som + int(cijfer)

    return 0
```

Je kan dit ook korter schijven, hieronder een voorbeeld

**VOORBEELD**

```python
x = 2
y = 2

x = x + 5

y += 5

print(x) # 7
print(y) # 7

```

als laatste moeten we de laatste lijn in de fucntie aanpassen. We returnen niet `0` maar `som`

```python
def optellengetallen(getal):
    string = str(getal)
    som = 0
    for cijfer in string:
        som = som + int(cijfer)

    return som # <--
```

Test dit nu uit met door de onderstaande code toe te voegen

```python
print(optellengetallen(getal))
```

Normaal zou er 45 in de terminal moeten komen.

## Stap 4

Nu willen we er ook voor zorgen dat deze 45 opgeteld wordt als 4 + 5. Deze stap zou voor elk getal moeten blijven herhaald worden tot er maar één cijfer overblijft.

We checken dus of het getal 9 of kleiner is en als dat niet zo is roept de functie zichzelf op

```python
def optellengetallen(getal):
    string = str(getal)
    som = 0
    for cijfer in string:
        som = som + int(cijfer)
    if som <= 9:
        return som
    else:
        return optellengetallen(som)
```

ten laaste zorgen we dat de uitvoer in een vareable opgeslagen wordt en geprint.

```python
resultaat = optellengetallen(nummer)
print("Het resultaat is", resultaat)
```

Dit noemt een recursieve functie, en dit is onmogelijk in scratch.

Bereken eens de uitkomst voor de volgende getallen

- `999888777` (9)
- `1010101010` (5)
- `15975345685215987412563` (3)
- `1234567891011121314151617181920` (3)

## Oefeningen voor gevorderden

1. Probeer er voor te zorgen dat je `nummer` niet in de code moet ingeven, maar dat het programma vraagt als je het programma start.

2. Wat merk je op als je da maaltafels van 9 invoert?

3. Wat als je een resultaat wilt van max. 2 getallen?

4. (EXTRA) Kun je ervoor zorgen dat het ook werkt voor negatieve getallen en kommagetallen?

## Voledige code

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
