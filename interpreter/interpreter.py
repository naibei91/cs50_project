x,y,z = input("Expression").split(" ")
match y:
    case "+":
        a = float(x) +float(z)
        print(round(a,1))