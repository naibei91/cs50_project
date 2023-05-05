def main() :
    x = float(input("Enter the first value : "))
    print(f"square of {x:.2f} is ",round(square(x),2))
    print(f"cubed of {x:.2f} is ",cubed(x))

def square(y):
    return y*y

def cubed(z):
    return pow(z,3)

main()

