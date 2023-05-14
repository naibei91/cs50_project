x = input("FIle name : ").strip()
y = x.find(".")
z = x[y+1][y+2][y+3].strip()
match z:
    case img:
        print(f"{x}").replace(".img","/gif")

