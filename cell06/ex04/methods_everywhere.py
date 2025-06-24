import sys

def shrink ( text ):
    return text[:8]

def enlarge ( text ):
    for i in range(len(text) , 8):
        text+='Z'

    return text

parameters=sys.argv

if len(parameters)==1:
    print("none")
else:
    for x in range(1 , len(parameters)):
        if len(parameters[x])<8:
            print(enlarge(parameters[x]))
        elif len(parameters[x])>8:
            print(shrink(parameters[x]))
        else:
            print(parameters[x])


