name = input("Search users by department : ").title().strip(" ")
if name == "Sales":
    print("1.John\n2.Jane\n3.Peter")
elif name == "Purchases":
    print("1.Onyango\n2.Jane\n3.Sarah")
elif name == "Finance":
    print("1.Mwangi\n2.Waweru\n3.Kimani")
else:
    print("Which department ?")