#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) != 3:
        print("none")
        return

    first = int(sys.argv[1])
    last = int(sys.argv[2])
    list = []

    for i in range(first, last + 1):
        list.append(i)

    print(list)

main()
    