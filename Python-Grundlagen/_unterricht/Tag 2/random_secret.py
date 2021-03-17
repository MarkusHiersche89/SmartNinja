
#from random import randint
#secret = randint(1, 20)

import numpy as np

import random
secret = random.randint(1, 20)

secret1 = np.random.randint(1,29)

counter = 0

while True:
    counter += 1
    guess = int(input("Input: "))
    if guess == secret:
        print("Zahl erraten mit " +  str(counter) + " Versuchen.")
        break
    elif guess > secret:
        print("Zahl > Secret")
    else:
        print("Zahl < Secret")

print("Programmende")

for y in range(10):
    if y % 2 == 0:
        print(y)

