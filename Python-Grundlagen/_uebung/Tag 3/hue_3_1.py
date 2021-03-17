"""
CSV files are the ones that end with .csv. They are very common for spreadsheets.
CSV means "comma-separated values". This means that values in the file are separated with a comma: ,.
You can create a CSV file the same way as you created a TXT file, except that you'd use .csv instead of .txt at the end of the file.
Let's take a look at how a CSV file may look like:
Name,Age,Gender
Tina,23,female
Jakob,35,male
Barbara,44,female
If you would import this CSV file in a spreadsheet (like Excel), you'd see a table with three columns (Name, Age, Gender).
But you can also process this file with Python. So your task is to create a Python program, that will go through this CSV file and print the following text in the Terminal:
Tina is female and 23 years old.
Jakob is male and 35 years old.
Barbara is female and 44 years old.
Hint: You will also need a string method called split(). ;)
When you complete the homework, store it on GitHub and share the link to it on Slack.
"""
counter = 0

lineList = []
with open("person.csv", "r") as item:
    for line in item:
        if counter > 0:
            line = line.rstrip("\n")
            line = line.split(",")
            print(line[0] + " is " + line[2] + " and " + line[1] + " years old.")
        counter += 1