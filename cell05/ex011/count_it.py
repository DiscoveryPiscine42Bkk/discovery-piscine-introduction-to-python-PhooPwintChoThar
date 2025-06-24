#!/usr/bin/env python3

import sys

parameters=sys.argv

print("parameterss : " , len(parameters)-1)
for i in range(1 , len(parameters)):
    print(parameters[i] , " : " , len(parameters[i]))