def main():
    display()

def display():
    x = (input("input first value : "))
    y = x.rfind()
    z = int(input("Choose 1 for sum 2 for differences 3 for multiplication 4 for remainder 5 for "))
    if(y == +):
        sum(x,y)
    elif(y == -):
        diff(x,y)
    elif( == *):
        mult(x,y)
    elif(y == %):
        rem(x,y)
    else:
        return z

def sum(a,b):
    print(f"The sum is of {a} and {b}: {a+b}")

def diff(c,d):
    print(f"The difference is {c} and {d} : {c-d}")

def mult(e,f):
    print(f"The sum is of {e} and {f}: {e*f}")

def rem(g,h):
    print(f"The remainder is of {g} dividing {h} is : {g%h}")

main()