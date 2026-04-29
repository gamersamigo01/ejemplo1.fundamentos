name  = input("Write your full name: ")

if name.isupper() or name.islower():
    name = name.title().strip()
    print(f"your name is {name}")
elif not name.isupper() or name.islower():
    print("Accepted")
else:
    print("You didnt write something")