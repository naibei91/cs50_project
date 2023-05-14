def main():
    if 7.0<=convert(min)<=8.0:
        print("breakfast time ")
    elif 12.0<=convert(min)<=13.0:
        print("lunch time")
    elif 18.0<=convert(min)<=19.0:
        print("dinner time")


def convert(time):
    c = float(a+(time/60))
    return c

hours,min = input("What is the time ?").split(":")
if x == "7" or x == "8" or x == "12" or x == "13" or x == "18" or x =="19":
    main()