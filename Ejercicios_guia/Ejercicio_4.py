email = input("Write your email: ").strip()

if not email.startswith("@") and email.count("@") == 1 and email.endswith(".com") or email.endswith(".org"):
    print("Your email was sussesfully entered")
elif email.startswith("@") or email.count("@") != 1:
    print("Error writing the @")
else:
    print("Error with the last value, its have to be .com or .org")

