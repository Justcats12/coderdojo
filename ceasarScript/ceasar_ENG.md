# Ceasar cypher

### Advanced

Around 100 b.C. Julius Ceasar invented a secret language. He shifted the alphabet by three letters so his enemies wouldn't understand his letters. A -> D, B -> E, F -> I ... More than 2000 years later this system is still used in encryption, only today we shift the alphabet 13 letters.

## Step 1

On itself, python does not know the alphabet, we'll have to tell it what it is..

```python
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
```

We'll be using this to shift trough the alphabet.

## Step 2

Now we'll write a function that will take a character and shift it 13 spots. This function is a little like a self-made block in scratch that we can use whenever we like.

```python
def shift(character):

```

To check if there's only 1 character in the parameter we'll use `assert`.

```python
def shift(character):
    assert len(character) == 1, "no more than 1 character allowed!"
```

If you now try to call the function with more than one character (e.g.`shift("foobar")`) you'll get an error:

```
Traceback (most recent call last):
  File "c:\Users\vdsja\Desktop\coderdojo\coderdojo\ceasarScript\ceasar.py", line 16, in <module>
    get_rot13("foobar")
  File "c:\Users\vdsja\Desktop\coderdojo\coderdojo\ceasarScript\ceasar.py", line 4, in get_rot13
    assert len(char) == 1, "no more than 1 character allowed"
           ^^^^^^^^^^^^^^
AssertionError: no more than 1 character allowed
```

## Step 3

Now we'll have to shif the character. We can ask for the index in the alphabet with `ALPHABET.index(character)`.

```python
def schuif_op(karakter):
    assert len(karakter) == 1, "één enkel karakter toegestaan"

    index = ALPHABET.index(karakter)
```

We kunnen de zoveelste letter van het alfabet opvragen met `ALPHABET[x]`. bv `ALPHABET[0]` -> a

```python
def shift(character):
    assert len(character) == 1, "no more than 1 character allowed!"

    index = ALPHABET.index(character)

    return ALPHABET[index]
```

We now only have to add 13 to the index. The problem is, if the index is e.g. 20 the index will be bigger than the alphabet.

```python
def shift(character):
    assert len(character) == 1, "no more than 1 character allowed!"

    index = ALPHABET.index(character)
    index += 13

    return ALPHABET[index]
```

Try `shift("a")` and you should get the letter n, but if you try `shift("t")` you'll get this error:

```
Traceback (most recent call last):
  File "c:\Users\vdsja\Desktop\coderdojo\coderdojo\ceasarScript\ceasar.py", line 13, in <module>
    get_rot13("t")
  File "c:\Users\vdsja\Desktop\coderdojo\coderdojo\ceasarScript\ceasar.py", line 12, in get_rot13
    return ALPHABET[index]
           ~~~~~~~~^^^^^^^
IndexError: string index out of range
```

We still have to do a check, if the index is 26 or bigger we need to subtract 26 from the index.

```python
    if index >= 26:
       index -= 26
```

Try again what you tried earlier and it should work.

## Step 4

Now we have to put this function to use. We'll ask the user for input, we'll assume the user doesn't use any capital letters.

```python
userInput = input("give a word: ")
```

We'll turn this input into output, this one remains empty for now.

```python
output = ""
```

Now well shift every character in `userInput` induvidually and add it to `output`.

```python
for c in userInput:
    output += shift(c)
```

After that we'll print the output

```python
print(output)
```

Can you decrypt the following?

- `whyvhf`
- `unpxref`
- `frpergf`

## Exercises for pros

1. Can you decryot the following?

- `xtbpljb` shift the alphabet 3 times
- `ayjjudi` 10 times
- `dzrxodzrx` 1 time
- `hahhrky` 20 times

2. Can you make it so spaces don't cause an error? Decrypt the following text?. (13 keer)

```
clguba vf nznmvat
```

3. Make a new program, what does the following code do?

```python
import codecs
t = codecs.encode("test", "rot_13")
print(t)

```

## Entire code

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
