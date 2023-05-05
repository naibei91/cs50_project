x = int(input("What is x :"))
y = int(input("What is y :"))

if x < y:
    print(f"{x} is less than {y}")
elif x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{x} is equal to {y}")


#using or
if x < y or x>y:
    print(f"{x} not equal to {y}")
else:
    print("{x} is greater than {y}")


