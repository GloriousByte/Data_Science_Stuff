#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    flag = 0
    reg = re.compile(r"\d+\s+\d+\s+\d+[\s\t]+[a-zA-Z\d]+\s*\w*")
    regx = r"(\d+)\s+(\d+)\s+(\d+)[\s\t]+([a-zA-Z\d]+\s*\w*)"
    ls = []
    with open(filename) as f:
        for line in f:
            if flag == 0:
                flag = 1
                continue
            foundlist = reg.findall(line)
         
            ls.append((re.sub(regx,r"\1\t\2\t\3\t\4",foundlist[0])))


    for key, string in enumerate(ls):
       if ls[key][-1] == "\n":
           ls[key] = ls[key][0:len(string)-1]
    print(ls)
    return ls


def main():
    hi = red_green_blue("rgb.txt")
   
if __name__ == "__main__":
    main()
