vragen = ["Wat is een haai? ", "Hoe noemt de haai van de Ikea? ", "Wat eet een haai? ", "Is een haai een dolfijn? "]
antwoorden = ["Een haai", "Blahaj", "vis", "nee"]
levens = 3

for i in range(len(vragen)):

    juist_antwoord = False

    while (not juist_antwoord) and (levens > 0) :

        antwoord = input(vragen[i])
        juist_antwoord = antwoord == antwoorden[i]

        if juist_antwoord:
            print("Goed antwoord")
        elif levens > 0:
            print("Fout antwoord, probeer opnieuw")
            levens -= 1
        else:
            print("Je bent verloren")
            break
