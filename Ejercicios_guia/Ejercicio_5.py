sentence = input("write a sentence to check if it is palindrome: ").lower().replace(" ", "")

if len(sentence) > 0 and sentence == sentence[::-1]:
    print("Is palindrome")
elif len(sentence) <= 0:
    print("you didnt write anything")
else:
    print("The sentence is not palindrome")