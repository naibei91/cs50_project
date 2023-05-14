greetings = input("Greating : ").title().strip()
x = greetings[0]

match greetings and x:
    case "Hello":
        print("$0")
    case "H":
        print("$20")
    case _:
        print("$100")