#!/usr/bin/env python3

import sys

parameters=sys.argv
if len(parameters)!=2:
    print("none")
else :
    print(parameters[1].lower())