f = open("datei.txt", "r")
for line in f:
    line.rstrip("\n")
    print(line)
f.close()

print("\n***\n")

with open("datei.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        print(line)

print("\n***\n")

my_txt = "Hier steht dein Text"
with open("datei.txt", "a") as file:
    file.write("\n" + my_txt)

print("\n***\n")

with open("datei.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        print(line)

print("\n***\n")

with open("datei.csv", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        woerter = line.split(",")
        print(woerter[0] + " " + woerter[1] + " ist " + woerter[2] + " Jahre alt und lebt in " + woerter[3] + ".")

print("\n***\n")

import random
import json

with open("scores.txt", "r") as file:
    points = json.loads(file.read())
    points.sort()
    print("Top scores: " + str(points))

number = random.randint(1, 100)
points.append(number)
with open("scores.txt", "w") as score_file:
    score_file.write(json.dumps(points))

with open("scores.txt", "r") as file:
    points = json.loads(file.read())
    points.sort()
    print("Top scores: " + str(points))