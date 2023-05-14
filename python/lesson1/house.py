name = input("Search users to know thier department : ").title().strip(" ")
if name == "John" or "Jane" or "Peter":
    print("Sales")
elif name == "Onyango" or "Jane" or "Sarah":
    print("Purchases")
elif name == "Mwangi" or "Waweru" or "Kimani":
    print("Finance")
else:
    print("Who?")