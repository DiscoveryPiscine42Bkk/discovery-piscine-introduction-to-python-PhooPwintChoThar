#!/usr/bin/env python3
def find_the_redheads (members):
    redheads=filter(lambda k : members[k]=="red" , members)

    return list(redheads)

dupont_family={
    "florian" : "red",
    "marie" : "blond",
    "virgine" : "bunette",
    "david" : "red",
    "franck" : "red"
}

print(find_the_redheads(dupont_family))
