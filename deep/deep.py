x = input("What is the answer to the Great Question of Life, the Universe and Everything?").title().strip()
match x:
    case "42" | "Forty-Two" | "Forty Two":
        print("Yes")
    case _:
        print("No")