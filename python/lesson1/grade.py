score = int(input("What is the score of the student : ").replace("%",""))
if score >=90 and score <=100:
    print(f"A : {score}%")
elif score >=80 and score<90:
    print(f"B : {score}%")
elif score >=70 and score<80:
    print(f"C : {score}%")
elif score >=60 and score<70:
    print(f"D : {score}%")
else:
    print(f"F : {score}%")


#also...

if 100>=score>=90:
    print(f"A : {score}%")
elif 80>=score<90:
    print(f"B : {score}%")
elif 70>=score<80 :
    print(f"C : {score}%")
elif 60>=score<70 :
    print(f"D : {score}%")
else:
    print(f"F : {score}%")

#also
if score>=90:
    print(f"A : {score}%")
elif score>=80:
    print(f"B : {score}%")
elif score >=70:
    print(f"C : {score}%")
elif score >=60:
    print(f"D : {score}%")
else:
    print(f"F : {score}%")

