# Datatypes in python
**OPGEPAST!** Dit is geen project 
## Deel 1: basistypes
### String
Een String (str) is een woord, zin of verzameling karakters. Het begint en eindigd altijd met aanhalingstekens.
```Python
naam = "Alice"
code = "14ABC"
zin = "Hello world, how are you?"
```
### Integer
Een integer (int) is een geheel getal (een getal zonder komma).
```py
getal = 12
som = 0
teller = 1
groot_getal = 894000000
```
### Boolean
Een boolean (bool) is waar of onwaar. 0 of 1. Of in python `True` of `False`.
```Python
waar = True
niet_waar = not waar #omgekeerde van waar => False
vergelijking: 1 + 1 == 2 #==> True
```
Een boolean kan in een if statement gestoken worden
```py
doe_het = True
if doe_het:
    print("gedaan")
```
### Float
Een float is een kommagetal. Maar door limieten van computers zal dit nooit heel exact zijn.
```py
pi = 3.14
nul_komma_twee = 0.2
groot_getal = 147000.124789
```
## Verzamelingen
zie ook: lijsten
### List
Een list, of lijst in het Nederlands is een verzameling van vareabelen:
```py
getallen = [1, 2, 3, 4, 5]
fruit = ["appel", "banaan"]
mix = ["woord", 1337, True, False "lol"]
```
Om een waarde uit een lijst te krijgen schrijven we de naam van de lijst en daar achter tussen vierkante haakjes de index.
#### Voorbeeld code
```py
lijst = ["Item 1", "Ding 2", "Zaak 3"]
print(lijst[0]) # Eerste
print(lijst[-1]) # Laatste
print(lijst[2]) # Derde
```
### Dictionary
Een dictionairy, woordenboek in het nederlands, is zoals een lijst, maar nu mogen we de index zelf kiezen.
```py
quiz_antwoorden = {"A":"Python", "B":"Scratch", "C":"JavaScript" }
postcodes = {9000: "Gent", 9052:"Zwijnaarde", 1000:"Brussel"}
```
Zo kunnen we aan een waarde in een dictionary met zijn bijhorende sleutel op deze manier: `dictionary_naam[sleutel]`
```py
quiz_antwoorden = {"A":"Python", "B":"Scratch", "C":"JavaScript" }
print(quiz_antwoorden["A"])
```
### Tuple
Een tuple is een verzameling elementen die heel dicht bij elkaar liggen, meestal coordinaten.
```py
coords = (100, 150)
drie_getallen = (22, 55, 47)
```
Een tuple werkt ongeveer hetzelfde als een list

## Speciale types

### formated string (f-string)
Een f-string een string waar nog zaken ingevuld moeten worden.
```py
naam = "Alice"
groet = f"Hallo {naam}"
```
### NoneType
Een NoneType is een waarde zonder type, dit zien we vaak in errors. Misschien moet je een waarde niet gelijkstellen aan een void functie...
```py
niets = None
foute_code = print("blablabla")
```

### range
Een range is een verzameling getallen. Je kan instellen welke getallen er allemaal insteken. Wij gaan dit enkel gebruiken voor for-loops
```py
nul_tot_negen = range(10)
twee_tot_vier = range(2,5)
```

## Voor de echte kenners
Deze gaan we (bijna nooit) nodig hebben, maar als je graag alle datatypes kent heb ik ze hiet opgelijst!

### Complex
Complex getal. Zal je nog zien in het middelbaar!
### Sets en Frozensets
Een set is een verzameling waarden in geen volgorde en onveranderbaar, je kunt geen enkel item in een set aanpassen of verwijderen.
```py
deze_set = {"Appel", "Banaan", "Citrien"}
```

### bytes, bytearray, memoryview
ééntjes en nulletjes, dit is voor de echte nerds.
```py
voorbeeld_bytes = b"Hallo"
voorbeeld_bytearray = bytearray(b'\x00\x00\x00\x00\x00')
voorbeeld_memoryview = <memory at 0x00B08FA0>
```