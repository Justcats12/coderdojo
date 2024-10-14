# Pannenkoeken bakken

### Gemakkelijk

In deze les leer je een programma maken waar je kan berekenen hoeveel pannenkoeken je kan maken met de ingrediënten die je hebt.

## Stap 1

Het eerste wat we gaan doen is ingeven hoeveel eiren je hebt. In python is hier een hele handige manier voor. Met `input("<vraag>")` kun je aan de gebruiker een vraag stellen.

```python
input("Hoeveel eieren heb je? ")
```

Maar nu doen we er niets mee... We moeten het opslaan in een vareabele.

```python
eieren = input("Hoeveel eieren heb je? ")
```

Deze vareabele kunnen we nu printen. Als je een f voor de aanhalingtekens (") zet zal de code alles tussen { } zelf invullen.

```python
eieren = input("Hoeveel eieren heb je? ")
print(f"Je hebt {eieren} eieren")
```

De waarde die je invult zal op de plaats waar `{eieren}` staat ingevuld worden.

Er zit een fout in deze code, wat gebeurt er als je de volgende code uitprobeert?

```python
eieren = input("Hoeveel eieren heb je? ")
print(f"Als je 2 eieren opeet zul je {eieren -2} eieren hebben.")
```

Normaal krijg je een error...

```
TypeError: unsupported operand type(s) for -: 'str' and 'int'
```

Dit komt omdat er niet kan gerekent worden met een ingevulde waarde, dit kunnen we makkelijk oplossen door er `int` bij te schrijven. Daardoor kan python er wel mee rekenen.

```python
eieren = int (input("Hoeveel eieren heb je? "))
print(f"Als je 2 eieren opeet zul je {eieren -2} eieren hebben.")
```

Voor de zekerheid zetten we altijd hetgeen dat we een `int` willen maken tussen haakjes.

Probeer nu de code uit te voeren.

## Stap 2

Voor pannenkoeken heb je 3 ingredienten nodig: eieren, melk en bloem. We moeten dus voor elk ingredient een vraag stellen.

```python
eieren = int (input("Hoeveel eieren heb je? "))
melk = int (input("Hoeveel mililiter melk heb je? "))
bloem = int (input("Hoeveel gram bloem heb je? "))
```

Ga na of alles werkt door alles een keer te printen.

```python
print(f"Eieren: {eieren}, melk: {melk}, bloem: {bloem}.")
```

Nu gaan we per ingrediënt berekenen hoeveel pannenkoeken je kan maken, en het laagste aantal nemen, want als de rest meer dan dat is lukt het sowiso.

Hier onder staag de code voor het aantal pannenkoeken per ingrediënt. In python is `*` de maal en `/` gedeeld door. Met `//` bereken je de deling zonder rest, we gaan natuurlijk geen halve pannenkoeken maken!

```python
eierenVoorPannenkoeken = eieren*4
melkVoorPannenkoeken = melk//30
bloemVoorPannenkoeken = bloem//12.5
```

Hiervan moeten we de laagste pakken. Hoe zouden we dit doen?

1. `max(1, 2, 3)` neemt het maximum, dus 3
2. `print(1, 2, 3)` print "1 2 3"
3. `min(x, y, z)` neemt het minimum, dus 1
4. `sum(x, y, z)` telt alles op, dus 6

Als je het niet geraden had, het antwoord is `min()`. We pakken het minimum van de drie waarden. We stoppen deze waarde in een vareabele.

```python
eieren = int (input("Hoeveel eieren heb je? "))
melk = int (input("Hoeveel mililiter melk heb je? "))
bloem = int (input("Hoeveel gram bloem heb je? "))

eierenVoorPannenkoeken = eieren*4
melkVoorPannenkoeken = melk//30
bloemVoorPannenkoeken = bloem//12.5

aantalPannenkoeken = min(eierenVoorPannenkoeken, melkVoorPannenkoeken, bloemVoorPannenkoeken)
```

Je kan nu aantalPannenkoeken printen om te zien hoeveel pannenkoeken je kan maken.

## Stap 3

Als je te weinig bloem of melk ingeeft kan het zijn dat je 0 pannenkoeken kan maken, en dat gaat niet. We zullen nakijken of er wel genoeg is voor pannenkoeken.

```python
if aantalPannenkoeken < 1:
    print("Niet genoeg voor pannenkoeken!")
```

als er wel genoeg zijn printen we gewoon het resultaat.

```python
if aantalPannenkoeken < 1:
    print("Niet genoeg voor pannenkoeken!")
else:
    print(f"Je kan {aantalPannenkoeken} pannenkoek(en) maken.")
```

## Extras voor gevorderden

1. het woord "pannenkoek(en)" kan beter, kun je ervoor zorgen dat dit "pannenkoek" wordt bij 1 en "pannenkoek" bij 2?

2. Per pannenkoek is eer eigenlijk ook 5 gram boter nodig. Kun je boter toevoegen aan het programma?

3. (GEVORDERD) Kun je op het einde ook printen hoeveel er van alles overblijft na het bakken?

4. (GEVORDERD) Herschrijf de code in max. 4 lijnen

5. (EXTA GEVORDERD) Herschrijf de code in 1 lijn.

## Voorbeeldcode

```python
eggs = int(input("Amount of eggs: "))
milk = int(input("ml milk: "))
flour = int(input("grammes of flour: "))

eggsForPancakes = eggs*4
milkForPancakes = milk//30
flourForPancakes = flour//12.5

pancakeAmount = min(eggsForPancakes, milkForPancakes, flourForPancakes)

if pancakeAmount < 1:
    print("Not enough for pancakes!")
else:
    print(f"You can make {pancakeAmount} pancake(s)")


```

### Oplossing 1 lijn

```python
pancakeAmount = min(int(input("Amount of eggs: "))*4, int(input("ml milk: "))//30, int(input("grammes of flour: "))//12.5); print({True: "Not enough for pancakes!", False: f"You can make {pancakeAmount} pancake(s)"}[pancakeAmount < 1])
```
