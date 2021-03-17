import json

with open("people.json") as file:
    data = json.load(file)

print(type(data))
print(data)

print("\n***\n")

for user in data:
    print(user)

print("\n***\n")

for user in data:
    print(user.get("first_name") + " " + user.get("last_name"))
    print(user.get("SSN"))
    print(user["country"])

print("\n***\n")

