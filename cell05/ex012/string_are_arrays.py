#!/usr/bin/env python3

import sys

parameters=sys.argv
if len(parameters)!=2 or( 'z' not in parameters[1]):
    print("none")
else :
    for i in parameters[1]:
        if i=='z':
            print(i , end="")
    print()
    