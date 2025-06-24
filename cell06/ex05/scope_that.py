#!/usr/bin/env python3

def scope_that( num ):
    num+=1
    return

value=3
print(f"Original value : {value}")
scope_that(value)
print(f"After function is called : {value}")