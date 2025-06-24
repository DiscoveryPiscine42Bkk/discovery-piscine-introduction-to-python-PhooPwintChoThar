#!/usr/bin/env python3

import sys

parameters=sys.argv
if len(parameters)!=3 or( parameters[1] not in parameters[2]):
    print("none")
else :
    print( parameters[2].count(parameters[1]))
    