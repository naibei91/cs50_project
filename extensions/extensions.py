x = input("FIle name : ").strip()
y = x.find(".")
z = x[y+2]
match z:
    case img:
        print(f{x}).replace(".img","/gif")

