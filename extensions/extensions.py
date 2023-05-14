def main():
    x = input("FIle name : ").strip().title()
    y = x+" "
    z1 = int(y.index("."))
    z2 = int(y.rindex("."))
    a = y[z1+1]+y[z1+2]+y[z1+3]+y[z1+4].strip()
    if z1 == z2 :
        onyesha(a)
    #else:
     #   print("application/octet-stream")

def onyesha(b):
    match b:
        case "gif" :
            print("image/gif")
        case "jpeg" | "jpg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "text":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

main()