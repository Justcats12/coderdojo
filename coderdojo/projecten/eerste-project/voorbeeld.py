naam = input("Wat is jouw naam? ")
code = 1234


if naam != "Alice":
    print("Jij mag niet binnen")
else:
    for i in range(3):
        poging = input("Geef wachtwoord: ")
        if poging == str(code):
            print(f"Hallo {naam}")
            break