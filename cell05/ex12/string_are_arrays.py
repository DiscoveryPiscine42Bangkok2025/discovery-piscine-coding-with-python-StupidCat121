#!/usr/bin/env python3

import sys

def main():
    list = []
    if len(sys.argv) != 2:
        print("none")
        return
    
    list = sys.argv[1]
    lizt = []
    for i in range(len(list)):
        strip = []
        strip.append(list[i].strip())
        if 'z' in strip:
            lizt.append(strip)
            my_str = ''.join(strip)
            print(my_str, end = '')
    if lizt == []:
        print("none")
    
        # for j in range(len(strip)):
        #     if strip[j] == 'z':
        #         print("z", end = '')

main()
