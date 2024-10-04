ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def get_rot13(char):
    assert len(char) == 1, "No more than one char allowed"
    if char == " ":
        return " "
    index = ALPHABET.index(char)

    index += 13
    if index >= 26:
       index -= 26

    return ALPHABET[index]
input_string = "python is fantastisch"
output = ""
for c in input_string:
    output += get_rot13(c)

print(output)