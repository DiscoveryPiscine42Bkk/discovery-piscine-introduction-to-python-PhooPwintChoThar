#!/usr/bin/env python3

import sys

parameters=sys.argv
if len(parameters)<=2:
    print("none")
else :
    for i in range(len(parameters)-1 , 0 , -1):
        print(parameters[i])