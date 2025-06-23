text=input("Enter a text : ")
for a in text:
    if a.isupper():
        print(a.lower() , end="")
    else :
        print(a.upper() , end="")