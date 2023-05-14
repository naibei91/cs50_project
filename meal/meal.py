def main():
    if 7.0<=convert(b)<=8.0:
        print("breakfast time")
    elif 12.0<=convert(b)<=13.0:
        print("lunch time")
    elif 18.0<=convert(b)<=19.0:
        print("dinner time")


def convert(time):
    return float(round(a+(time/60),1))

x,y = input("What is the time ?").split(":")
a=float(x)
b=float(y)
if x == "7" or x == "8" or x == "12" or x == "13" or x == "18" or x =="19":
    main()