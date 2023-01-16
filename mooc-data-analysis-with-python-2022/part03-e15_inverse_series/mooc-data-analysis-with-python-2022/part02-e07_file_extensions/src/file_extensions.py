#!/usr/bin/env python3
import re

def file_extensions(filename):
    ls = []
    dic = {}
    regex = re.compile(r"^[a-zA-Z]+$")
    Bregex = re.compile(r"([a-zA-Z1-9]+)([.][a-z]+)?[.]([a-z]+)")
    with open(filename) as f:
        for line in f:
            if regex.search(line):
                match = regex.search(line)
                ls.append(match.group(0))

            elif Bregex.search(line):
                 match = Bregex.search(line)
                 if match.group(3) in dic.keys():
                     dic[match.group(3)].append(match.group(0))
                 else:
                     dic[match.group(3)] = [match.group(0)]
               
                 

    return (ls, dic)

def main():
    hi = file_extensions("filenames.txt")   
    print(f"{len(hi[0])} files with no extension")
    for key, value in hi[1].items():
        print(f"{key}\t{len(value)}")
            

           

if __name__ == "__main__":
    main()
