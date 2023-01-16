#!/usr/bin/env python3

def transform(str1, str2):
    l = map(int,str1.split())
    l2 = map(int,str2.split())
    zipr = list(zip(l,l2))
    for indx, i in enumerate(zipr):
        zipr[indx] = [i[0] * i[1]]
    return zipr

    return []

def main():
    pass

if __name__ == "__main__":
    main()
