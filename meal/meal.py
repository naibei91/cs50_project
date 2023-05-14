def main():
    meal = convert(b)
    if 7.0<=meal<=8.0:
        print("breakfast time")
    elif 12.0<=meal<=13.0:
        print("lunch time")
    elif 18.0<=meal<=19.0:
        print("dinner time")


def convert(time):
    c = float(round(a+(time/60),1))
    return c

x,y = input("What is the time ?").split(":")
a=float(x)
b=float(y)
if x == "7" or x == "8" or x == "12" or x == "13" or x == "18" or x =="19":
    main()