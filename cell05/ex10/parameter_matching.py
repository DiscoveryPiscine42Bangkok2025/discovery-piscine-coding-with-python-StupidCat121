#!/usr/bin/env python3

import sys

def main(inp):

    if len(sys.argv) != 2:
        print("none")
        return
    
    if inp == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")



inp = input("What was the parameter? ") 
main(inp)