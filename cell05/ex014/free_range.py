#!/usr/bin/env python3

import sys
parameters=sys.argv
if len(parameters)==3:
    numbers=[]
    num1=int(parameters[1])
    num2=int(parameters[2])
    for i in range(num1, num2+1):
        numbers.append(i)
    print(numbers)
else:
    print("none")
