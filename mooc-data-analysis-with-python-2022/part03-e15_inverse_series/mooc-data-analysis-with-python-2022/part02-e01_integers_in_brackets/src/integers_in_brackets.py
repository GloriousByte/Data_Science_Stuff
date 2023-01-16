#!/usr/bin/env python3
import re

from numpy import empty

def integers_in_brackets(string):
    reg = re.compile(r"(\[[\s\t]*[-+]?\d+\s*\])")
    num = re.compile(r"([-]?\d+)")
    ls = []
    for match in reg.findall(string):
        ls.append(match)
    
    for key, match in enumerate(ls):
        res = num.search(ls[key])
        ls[key] = int(res.group(1))
    return ls

def main():
    print("result: ",integers_in_brackets("afd [asd] [12 ] [a34]  [	 -43 ]tt [+12]xxx!")) 

if __name__ == "__main__":
    main()
