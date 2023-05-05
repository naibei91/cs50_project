def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d2f = d.remove("$"):
    return round(d2f,1)")
    # TODO


def percent_to_float(p):
    p2f = p


main()