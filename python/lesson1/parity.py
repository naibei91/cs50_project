
def main():
    even(value())

def value():
    details = int(input("Enter an even number : "))
    return details

def even (x):
    if x % 2 ==0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")