greetings = input("Greating : ").title().strip()

if greetings.find("Hello") != -1:
    print("$0")
elif greetings[0] == "H":
    print("$20")
else:
    print("$100")