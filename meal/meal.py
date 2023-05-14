def main():
    meal = convert(y)
    if 7.0<=meal<=8.0:
        print("breakfast time")
    elif 12.0<=meal<=13.0:
        print("lunch time")
    elif 18.0<=meal<=19.0:
        print("dinner time")


def convert(time):
    return round(x+time/60,2)

x,y = input("What is the time ?").split(":")
if x == "7" or x == "8" or x == "12" or x == "13" or x == "18" or x =="19":
    main()