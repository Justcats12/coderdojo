quiz = {
    "In welke taal is dit geschreven": "python",
    "Welke extensie gebruiken python bestanden?": ".py",
    "Waar of fout? Python is sneller in uitvoer dan Java.": "fout",
}

lives = 3

for question in quiz:

    correct = False

    while not correct and lives > 0:
        print(question)
        answer = input("Answer: ")
        
        correct = answer == quiz[question]

        if not correct:
            lives -=1
            print("Wrong, try again")
    if lives == 0:
        break
else:
    print("Good job you won!")
