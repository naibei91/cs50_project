name = input("Search users to know thier department : ").title().strip(" ")
"""
if name == "John" or name == "Jane" or name == "Peter":
    print("Sales")
elif name == "Onyango" or name == "Jane" or name == "Sarah":
    print("Purchases")
elif name == "Mwangi" or name == "Waweru" or name == "Kimani":
    print("Finance")
else:
    print("Who?")
"""

match name:
    case "John": #or "Jane" or "Peter" :
        print("Sales")
    case "Onyango": # or "Jane" or "Sarah" :
        print("Purchases")
    case "Mwangi": #or "Waweru" or "Kimani":
        print("Finance")
    case _:
        print("Who?")