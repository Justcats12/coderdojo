# Geheime code

### Gevorderd

Round 100 v.C. vondt Julius Ceasar een geheime taal uit. Hij verschoof het alfabet met 3 karakters zodat zijn vijanden zijn brieven niet konden verstonen. A -> D, B -> E, F -> I ... Meer dan 2000 jaar later wordt dit concept nog steeds gebruikt voor encriptie. Maar vandaag gebruiken we een variant dat het alfabet met 13 letter opschuift.

## Stap 1

Python kent het alfabet niet vanbuiten. We moeten dit in een vareabele steken.

```python
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
```

Dit zullen we gebruiken om het alfabet te shiften.

## Stap 2

Nu kunnen we beginnen aan een funcie waarmee we een karkater 13 plaatsen kunnen opschuiven. Deze functie werkt als een zelfgemaakt blok in scratch die we later kunnen oproepen.

```python
def schuif_op(karakter):

```

Om zeker te zijn dat er één karakter werd ingevult zullen we een check uitvoeren. Dit kunnen we doen met `assert`.

```python
def schuif_op(karakter):
    assert len(karakter) == 1, "één enkel karakter toegestaan"
```

Probeer nu onder de code het volgende uit te voeren en je zal een error krijgen zoals deze:

```python
schuif_op("oogabooga")
```

```
Traceback (most recent call last):
  File "c:\Users\vdsja\Desktop\coderdojo\coderdojo\ceasarScript\ceasar.py", line 16, in <module>
    get_rot13("foobar")
  File "c:\Users\vdsja\Desktop\coderdojo\coderdojo\ceasarScript\ceasar.py", line 4, in get_rot13
    assert len(char) == 1, "één enkel karakter toegestaan"
           ^^^^^^^^^^^^^^
AssertionError: één enkel karakter toegestaan
```

## Stap 3

Nu moeten we het ingevoerd karakter 13 plaatsen opschuiven. We kunnen de index in het alfabet opvragen met `ALPHABET.index(karakter)`.

```python
def schuif_op(karakter):
    assert len(karakter) == 1, "één enkel karakter toegestaan"

    index = ALPHABET.index(karakter)
```

We kunnen de zoveelste letter van het alfabet opvragen met `ALPHABET[x]`. bv `ALPHABET[0]` -> a

```python
def schuif_op(karakter):
    assert len(karakter) == 1, "één enkel karakter toegestaan"

    index = ALPHABET.index(karakter)

    return ALPHABET[index]
```

Het enige wat we nog moeten doen is 13 bij de index optellen. Het probleem hierbij is als de index bv. 20 is dan wordt de index hoger dan een letter in het alfabet.

```python
def schuif_op(karakter):
    assert len(karakter) == 1, "één enkel karakter toegestaan"

    index = ALPHABET.index(karakter)
    index += 13

    return ALPHABET[index]
```

Probeer nu eens `schuif_op("a")` en je zou de letter n moeten krijgen, maar als je `schuif_op("t")` uitvoert zal je de volgende error krijgen:

```
Traceback (most recent call last):
  File "c:\Users\vdsja\Desktop\coderdojo\coderdojo\ceasarScript\ceasar.py", line 13, in <module>
    get_rot13("t")
  File "c:\Users\vdsja\Desktop\coderdojo\coderdojo\ceasarScript\ceasar.py", line 12, in get_rot13
    return ALPHABET[index]
           ~~~~~~~~^^^^^^^
IndexError: string index out of range
```

Daarom moeten we nog een check doen, als de index 26 of hoger is moeten 26 van de index afrekken

```python
    if index >= 26:
       index -= 26
```

Probeer nu nog eens wat we daarnet hebben geprobeert en het zou moeten werken.

## Stap 4

Nu moeten we onze functie aan het werk zetten. We zullen de gebruiker eers om invoer vragen, we gaan er wel van uit dat de gebruiker geen hoofdletters of speciale tekens gebruikt

```python
invoer = input("geef een woord: ")
```

Als volgt verkwerken we de invoer tot uitvoer, deze is voorlopig leeg.

```python
uitvoer = ""
```

Nu moeten we elk karakter opschuiven. We kunnen met een for loop elk karakter afgaan.

```python
for k in invoer:
    uitvoer += schuif_op(k)
```

Daarna printen we de uitvoer

```python
print(output)
```

Kun je nu de volgende texten ontcijferen

- `pbqreqbwb`
- `unpxref`
- `bagpvwsrera`

## Oefeningen voor gevorderden

1. Kan je de volgende texten ontcijferen

- `aofbjxxi` schuif het alfabet 3 keer
- `setuhteze` 10 keer
- `oxsgnm` 1 keer
- `vxumxgskxkt` 20 keer

2. kun je ervoor zorgen dat spaties genegeerd worden en geen error veroorzaken? Kraak de onderstaande text. (13 keer)

```
clguba vf snagnfgvfpu
```

3. Maak een nieuw programma, wat doet de volgende code?

```python
import codecs
t = codecs.encode("test", "rot_13")
print(t)

```

## Volledige code

```python
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def get_rot13(char):
    assert len(char) == 1, "No more than one char allowed"

    index = ALPHABET.index(char)

    index += 6
    if index >= 26:
       index -= 26

    return ALPHABET[index]
input_string = "programeren"
output = ""
for c in input_string:
    output += get_rot13(c)

print(output)
```
