greetings = input("Greating : ").title().strip()
x = greetings[0]

match greetings:
    case "Hello":
        print("$0")
match x:
    case "H":
        print("$20")
    case _:
        print("$100")