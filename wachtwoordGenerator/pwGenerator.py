import random

ALLOWED_CHARS = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789*+-*/!?.,;:&="

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

# optional: calculate how long it would take

REVOLUTION = len(ALLOWED_CHARS)
IPS = 8000000

def calc_time(password):
    instruction_count = 0
    for c in password:
        # + digit
        instruction_count *= REVOLUTION
        # + index
        instruction_count += ALLOWED_CHARS.index(c)
    
    return instruction_count/IPS
seconds = calc_time(random_password)
minutes = seconds/60
hours = minutes/60
days = hours/24
months = days/30
years = days/365.25
print("Password", random_password, "takes", seconds, "seconds.")
print(f"That is {round(years, 2)} years")


