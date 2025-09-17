#!/usr/bin/env python3

import sys

def main():

    if len(sys.argv) == 1:
        print("none")
        return
    
    count = len(sys.argv) - 1
    print(f"parameter : ",count)
    for i in range(1, len(sys.argv)):
        print(f"{sys.argv[i]}: {len(sys.argv[i].strip())}")


main()



