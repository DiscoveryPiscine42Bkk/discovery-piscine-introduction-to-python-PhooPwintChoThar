#!/usr/bin/env python3

num=input("Give me a number : ")
f=float(num)

if f.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")