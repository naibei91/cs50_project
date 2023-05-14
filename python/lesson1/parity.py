
def main():
     if even():
         print("It is even")
     else:
         print("Odd")


def value():
    details = int(input("Enter an even number : "))
    return details

"""
def even ():
    x = value()
    if x % 2 ==0:
        print(" is even")
    else:
        print(" is odd")
"""
"""
def even ():
    if value() % 2 ==0:
        return True
    else:
        return False
"""
def even ():
        return True if value() % 2 ==0 else False

main()