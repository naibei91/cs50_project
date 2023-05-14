greetings = input("Greating : ").title().strip()
x = greetings[0]
y = greetings.strip("Hello")

match x and y:
    case "Hello":
        print("$0")
    case "H":
        print("$20")
    case _:
        print("$100")