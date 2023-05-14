greetings = input(Greating : ).title().strip()

match greetings:
    case greetings == "Hello":
        print("$0")
    case greetings = "H":
        print("$20")
    case _:
        print("$100")