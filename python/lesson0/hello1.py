def main():
    name = input("what is your name ?").title()
    hello1(name)
    hello()
def hello ():
    print("hello",end = " ")

def hello1(to = "world"):    
    print("hello "+ to)


main()


