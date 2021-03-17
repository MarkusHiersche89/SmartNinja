#
# Session 2 | File 1
#

secret = 22
guess = 0
number = 0

while guess != secret:
    guess = int(input("Secret-Number: "))

    if guess == secret:
        print("Secret erraten")
    else:
        print("Falsches Secret")

print("Programm endet")

for x in range(10):     # 0 bis 9
    print(x)            # in Java, C# wird "item" verwendet | in Python "x"

secret = 23
while True:
    guess = int(input("Secret: "))
    if guess == secret:
        print("Secret erraten")
        break
    else:
        print("Falsches Secret")

# break bricht die schleife ab
# continue unterbricht den schleifendurchlauf
#          und geht hoch zum schleifenkopf

