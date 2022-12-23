#!/usr/bin/env python3

def distinct_characters(lst):
    dic = {}
    j = 0
    for i in lst:
        dic[i] = len(set(lst[j]))
        j += 1
    return dic
 

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
