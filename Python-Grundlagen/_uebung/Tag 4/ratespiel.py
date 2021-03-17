import datetime
import json
import random

secret = random.randint(1, 30)
attempts = 0

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

for score_dict in score_list:
    print("Name: " + score_dict.get("name") + "; date: " + score_dict.get("date") + "; attempts: " + str(score_dict.get("attempts")) + "; wrong guesses: " + str(score_dict.get("wrong_guesses")) + "; secret " + str(score_dict.get("secret")))

wrong_guesses = 0

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        print("wrong_guesses: " + str(wrong_guesses))

        name = input("Your name: ")
        score_list.append({"attempts": attempts, "wrong_guesses": wrong_guesses, "date": str(datetime.datetime.now()), "name": name, "secret": secret})

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
    wrong_guesses += 1