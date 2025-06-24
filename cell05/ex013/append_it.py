#!/usr/bin/env python3

import sys
parameters=sys.argv
if len(parameters)>1:
    for i in range(1 , len(parameters)):
        if parameters[i].endswith("ism"):
            continue
        else:
            parameters[i]+="ism"
            print(parameters[i])
else:
    print("none")
