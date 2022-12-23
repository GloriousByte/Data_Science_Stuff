#!/usr/bin/env python3

def reverse_dictionary(d):
    newdic = {}
    for key, val in d.items():
        for i in val:
            if i in newdic.keys():
                newdic[i].append(key)
            else:
                newdic[i] = [key]
    return newdic

def main():
    pass

if __name__ == "__main__":
    main()
