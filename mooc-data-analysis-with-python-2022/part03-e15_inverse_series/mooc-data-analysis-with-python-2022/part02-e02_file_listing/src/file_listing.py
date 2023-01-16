#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    string = '0123456789'
    reg = re.compile(r"(\d+)\s+(\w+)\s+(\d+)\s+(\d{2}):(\d{2})\s+([.]?[_]?\w+[\w_.-]*\.?\w*)")
    ls=[]
    newls=[]
    num = 0
    with open (filename) as f:
        for line in f:
            match = reg.findall(line)
            ls.append(match)
           
            

    for key, l in enumerate(ls):
        ls[key] = list(ls[key][0])

    for l in ls:
        for key, item in enumerate(l):
            match = 0
            for i in range(0,len(item)):
                if item[i] in string:
                    match += 1
            if match == len(item):
                l[key] = int(item)

    for key, l in enumerate(ls):
        ls[key] = tuple(ls[key])

    print(ls)
    return ls


def main():
    pass

if __name__ == "__main__":
    file_listing()
    main()
