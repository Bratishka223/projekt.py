import random

print("Välkommen till mitt spel gissa talet (1-100) \n du har 7 försök \n\n ")

random_number = random.randint(1, 100)

tries = 7

while tries > 0:
    guess = int(input(f"Gissa mitt tal(du har {tries} försök kvar): "))
    tries -= 1

    if guess == random_number:
        print("Grattis! Du gissade rätt tal!")
        break
    elif guess < random_number:
        print("För lågt,kämpa på!")
    else:
        print("För högt,baby cheesus!")

else:
    print(f"Du förlorade, F i kursen! Rätt tal var {random_number}.")
