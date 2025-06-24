#!/usr/bin/env python3
def array_of_names( namelist ):

    names=[]

    for key in namelist:
        names.append((key+' '+namelist[key]).title())

    return names


persons={
    "jean" : "valjean",
    "grace" : "hopper",
    "xavier" : "niel",
    "fifi" : "brindacier"
}

print(array_of_names(persons))