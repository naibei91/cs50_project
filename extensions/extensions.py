x = input("FIle name : ").strip()
y = x.find(".")
z = x[y+1][y+3][y+4].strip()
match z:
    case img:
        print(f"{x}").replace(".img","/gif")

