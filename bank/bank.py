greetings = input("Greating : ").title().strip()

match greetings:
    case "Hello":
        print("$0")
    case "H":
        print("$20")
    case _:
        print("$100")