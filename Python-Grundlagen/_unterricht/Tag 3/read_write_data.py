
# unsicher
# Optionen:
# r => read
# r+ => read and more <= nicht in Python
# a => append
# w => write
# x => create
# t => text mode
# b => binary mode

#f = open("ninja.txt")
#f.append("!")
#print(f.read())
#print(f.read(5)) # v. 2.7
#f.close()

with open("ninja.txt", "r") as file:
    #print(file.read())
    lines = file.readlines()
    for line in lines:
        print(line)

with open("ninja1.txt", "w") as file1:
    file1.write("Hallo neues File")

with open("ninja1.txt", "a") as file:
    file.append("\nappend")         # unter Win: "\r\n"