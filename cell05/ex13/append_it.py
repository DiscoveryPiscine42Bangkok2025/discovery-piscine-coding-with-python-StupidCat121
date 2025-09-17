#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) == 1:
        print("none")
        return

    for i in range(1, len(sys.argv)):
        if sys.argv[i].endswith('ism'):
            pass
        else:
            print(sys.argv[i] + 'ism')

main()