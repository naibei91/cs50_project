def main():
    display()

def display():
    x = float(input("input first value : "))
    y = float(input("input next value : "))
    z = int(input("Choose 1 for sum 2 for differences 3 for multiplication 4 for remainder 5 for "))
    if(z == 1):
        sum(x,y)
    elif(z == 2):
        diff(x,y)
    elif(z == 3):
        mult(x,y)
    elif(z == 4):
        rem(x,y)
    else:
        return 0

def sum(a,b):
    print(f"The sum is of {a} and {b}: {a+b}")

def diff(c,d):
    print(f"The difference is {c} and {d} : {c-d}")

def mult(e,f):
    print(f"The sum is of {e} and {f}: {e*f}")

def rem(g,h):
    print(f"The remainde is of {g} dividing {h}: {g%h}")

main()