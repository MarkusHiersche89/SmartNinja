
import numpy as np
import random

secret = random.randint(1, 100)
#secret1 = np.random.randint(1,29)
counter = 0

with open("score.txt", "r") as punkteliste:
    content = punkteliste.read()
    inhalt = content.split(":")
    name = inhalt[0]
    print(content)
    best_score = int(inhalt[1])
    print("Punkteliste: " + str(best_score))

while True:
    counter += 1
    guess = int(input("Input: "))
    if guess == secret:
        print("Zahl erraten mit " +  str(counter) + " Versuchen.")

        if counter < best_score:
            with open("score.txt", "w") as punkteliste:
                punkteliste.write(str(counter))

        break
    elif guess > secret:
        print("Zahl zu groß")
    else:
        print("Zahl zu klein")

print("Programmende")

#for y in range(10):
#    if y % 2 == 0:
#        print(y)

