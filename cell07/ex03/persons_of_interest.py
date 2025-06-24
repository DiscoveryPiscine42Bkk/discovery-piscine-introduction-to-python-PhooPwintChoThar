#!/usr/bin/env python3

def famous_births(scientists):

    for each in scientists:
        print(f"{scientists[each]["name"]} is a great scientist born in {scientists[each]["date_of_birth"]}.")


woman_scientists={
    "ada" :{"name" : "Ada Lovelace" , "date_of_birth" : "1815"},
    "cecilia" :{"name" : "Cecila Payne" , "date_of_birth" : "1900"},
    "lise" :{"name" : "Lise Meitner" , "date_of_birth" : "1878"},
    "grace" :{"name" : "Grace Hopper" , "date_of_birth" : "1906"},
}

famous_births(woman_scientists)