#!/usr/bin/env python3

import sys

parameters=sys.argv
if len(parameters)!=2:
    print("none")
else :
    ans=input("What was the parameter? : ")
    if ans==parameters[1]:
        print("Good job!")
    else :
        print("Nope , sorry ...")