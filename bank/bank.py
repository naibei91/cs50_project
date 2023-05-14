greetings = input("Greating : ").title().strip()

if greetings.find("Hello") == "Hello":
    print("$0")
elif greetings[0] == "H":
    print("$20")
else:
    print("$100")