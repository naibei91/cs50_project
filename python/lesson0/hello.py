"""#print hello world
print("Hello,world")

#print hello and the persons name on same line
name = input("what's your name? ")
print("Hello," + name)

#print hello and the persons name on new line
print("Hello,")
print(name)

#print hello and the persons name on different line
print("Hello,")
print(name)

#print hello and the persons name on same line using end=""
print("Hello," ,end="")
print(name)

#print hello and the persons name on same line using end="" and without separator sep = "00"
print("Hello," ,name ,end="",sep = "00")
print(name)


#take multiple arguments
name1 = input("what's your second name? ")
print("Hello,",name,name1)

#print with space removed from input and Capitalizing the first letters of the code
name = name.strip().title()
name1 = name1.upper()
print("Hello,",name,name1)

#using a format string

print(f"Hello,\"{name}\"{name1}",sep=' ')

"""
#using it in one line of code
name2 = input("What are your names ?").strip().title().rstrip('naibei').split(',',maxsplit=1)
print(f"Hi,{name2}")