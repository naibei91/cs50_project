def main():
    if convert(y) == 7.5:
        print(7.5)
    elif 7.0<=convert(y)<=8.0:
        print("breakfast time ")
    elif 12.0<=convert(y)<=13.0:
        print("lunch time")
    elif 18.0<=convert(y)<=19.0:
        print("dinner time")


def convert(time):
    c = round(x+(time/60))
    return c

hours,min = input("What is the time ?").split(":")
x = float(hours)
y = float(min)
if hours == "7" or hours == "8" or hours == "12" or hours == "13" or hours == "18" or hours =="19":
    main()