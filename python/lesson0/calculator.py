#using integers

x = int(input("Enter first value:"))
y = int(input("Enter second value:"))

print(x+y)

z = int(x)+int(y)

print(f"sum of first value and second value is {z}")

#using float
a = float(input("Enter first value:"))
b = float(input("Enter second value:"))

print(a+b)

c = a+b
print(f"sum of first value and second value is {c}")

#using round
d = round(a+b,4)
print(f"sum of first value and second value is {d}")


#to add commas to values using fstring for numeric formating
print(f"{d:,}")

#division

g = round (x/y,2)
print(g)

#division alterntive using fstring

h = x / y
print(f"{z:}")