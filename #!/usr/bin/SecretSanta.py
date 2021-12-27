#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created in 2020

This program was originally created in 2020 and modified for Christmas 2021.
The idea is to give in my extended family a possibility to remember only one adult 
with good conscience instead of having pressure to remember all the adults.

Please feel free to use it for your own families.

@author: Joniniemelainen
"""

import random

family_members=["Jussi", "Niina", "Pekka", "Laura", "Anne", "Matti",\
                "Joni", "Helena", "Nestori", "Matilda", "Ismo"]

santa_list = ["Jussi", "Niina", "Pekka", "Laura", "Anne", "Matti",\
                "Joni", "Helena", "Nestori", "Matilda", "Ismo"]
    
## Check couples so that couples do not end in the program
def checkCouples(Santa, Child):
    if Santa=="Joni" and Child=="Helena":
        return False
    elif Santa=="Helena" and Child=="Joni":
        return False
    elif Santa=="Jussi" and Child=="Niina":
        return False
    elif Santa=="Niina" and Child=="Jussi":
        return False
    elif Santa=="Pekka" and Child=="Laura":
        return False
    elif Santa=="Laura" and Child=="Pekka":
        return False
    elif Santa=="Anne" and Child=="Matti":
        return False
    elif Santa=="Matti" and Child=="Anne":
        return False
    elif Santa=="Nestori" and Child=="Matilda":
        return False
    elif Santa=="Matilda" and Child=="Nestori":
        return False
    else:
        return True


def SecretSanta(family_members, santa_list):
    while True:
        Child = random.choice(family_members)
        Santa = random.choice(santa_list)
        if (Santa == Child):
            print("", end="")
        else:
            if checkCouples(Santa, Child) == False:
                print("", end="")
            else:
                family_members.remove(Child)
                santa_list.remove(Santa)
                break
    return Child, Santa


def main():
    print("This is a SecretSanta lottery program to the extended Family Niemeläinen \n")
    
    while len(family_members) > 0:
        result = SecretSanta(family_members, santa_list)
        print("\n")
        print("SecretSanta is:", result[1])
        print("The well-behaving child is:", result[0])
        print("Have a nice Christmas! \n")
        
    print("SecretSanta found all well-behaving children. Thanks!")
    return None

main()
