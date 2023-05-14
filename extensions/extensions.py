x = input("FIle name : ").strip()
y = x+" "
z = y.find(".")
a = y[z+1]+y[z+2]+y[z+3]+y[z+4]
match a:
    case gif:
        print(f"{x}").replace(".gif","/gif")
    case jpg:
        print(f"{x}").replace(".jpg","/jpg")
    case jpeg:
        print(f"{x}").replace(".jpeg","/jpeg")
    case png:
        print(f"{x}").replace(".gif","/gif")
    case pdf:
        print(f"{x}").replace(".gif","/gif")
    case text:
        print(f"{x}").replace(".gif","/gif")
    case zip:
        print(f"{x}").replace(".gif","/gif")

