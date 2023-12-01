getal1 = int(input("Geef getal 1: "))

teken = input("Geef teken: ")

getal2 = int(input("Geef getal 2: "))

match teken:
    case "+":
        oplossing = int(getal1) + int(getal2)
    case "-":
        oplossing = int(getal1) - int(getal2)
    case "*":
        oplossing = int(getal1) * int(getal2)
    case "/":
        oplossing = int(getal1) / int(getal2)
    case _:
        oplossing = "Ongeldig teken!"
print(oplossing)