x = input("FIle name : ").strip().title()
y = x+" "
z = y.find(".")
a = y[z+1]+y[z+2]+y[z+3]+y[z+4].strip()
if z[1] == null:
       match a:
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

else:
    print("application/octet-stream")

