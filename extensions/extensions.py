def main():
    x = input("FIle name : ").title()
    y = x+" "
    z1 = int(y.index("."))
    z2 = int(y.rindex("."))
    a = y[z1+1]+y[z1+2]+y[z1+3]+y[z1+4].strip()
    if z1 == z2 :
        onyesha(a)
    else:
       print("application/octet-stream")

def onyesha(b):
    match b:
        case "Gif" :
            print("image/gif")
        case "Jpeg" | "Jpg":
            print("image/jpeg")
        case "Png":
            print("image/png")
        case "Pdf":
            print("application/pdf")
        case "Txt":
            print("text/plain")
        case "Zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

main()