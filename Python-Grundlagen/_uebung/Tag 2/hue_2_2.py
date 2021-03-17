"""

Homework 2.2: FizzBuzz
User enters a number between 1 and 100
FizzBuzz program starts to count to that number (it prints them in the Terminal).
In case the number is divisible with 3, it prints "fizz" instead of the number.
If the number is divisible with 5, it prints "buzz".
If it's divisible with both 3 and 5, it prints "fizzbuzz".

Example:

Select a number between 1 and 100
16

1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
A tip for this project:

How to find a division remainder

If a division remainder is 0, that means some number is divisible with another (without remainder).

Example:

print(15 % 5)
print(15 % 4)
15 is divisible with 5, so the remainder is 0. But 15 is not divisible with 4, so the remainder is not 0.

When you finish, paste your code on GitHub Gist and share it on the SmartNinja forum.

=== === ===

Hausaufgabe 2.2: FizzBuzz
Der Benutzer gibt eine Zahl zwischen 1 und 100 ein
Das FizzBuzz-Programm beginnt, bis zu dieser Nummer zu zählen (es druckt sie im Terminal aus).
Falls die Zahl durch 3 teilbar ist, wird anstelle der Zahl "fizz" ausgegeben.
Wenn die Zahl durch 5 teilbar ist, wird "Buzz" ausgegeben.
Wenn es mit 3 und 5 teilbar ist, wird "fizzbuzz" gedruckt.

Beispiel:

Wählen Sie eine Zahl zwischen 1 und 100
16

1
2
Sprudel
4
summen
Sprudel
7
8
Sprudel
summen
11
Sprudel
13
14
Fizzbuzz
16
Ein Tipp für dieses Projekt:

So finden Sie einen Teilungsrest

Wenn ein Teilungsrest 0 ist, bedeutet dies, dass eine Zahl mit einer anderen teilbar ist (ohne Rest).

Beispiel:

Drucken (15% 5)
Drucken (15% 4)
15 ist mit 5 teilbar, also ist der Rest 0.
Aber 15 ist nicht mit 4 teilbar, also ist der Rest nicht 0.

Wenn Sie fertig sind, fügen Sie Ihren Code in GitHub Gist ein und teilen Sie ihn im SmartNinja-Forum.

"""

ende = int(input("Endzahl: "))

for i in range(1, ende):
    if (i % 3 == 0 and i % 5 == 0): # Methematisch gesehen könnte man auch mit "i % 15 == 0" abfragen...
        print("fizzbuzz")
    elif(i % 3 == 0):
        print("fizz")
    elif(i % 5 == 0):
        print("buzz")
    else:
        print(i)
print("Programmende erreicht")