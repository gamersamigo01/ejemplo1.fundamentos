document = input("Write the name of your archive: ").lower()

if document.endswith(".jpg") or document.endswith(".png"):
    print("Your archive is an image")
elif document.endswith(".pdf") or document.endswith(".doc"):
    print("Your archive is a document")
else:
    print("unknown format")