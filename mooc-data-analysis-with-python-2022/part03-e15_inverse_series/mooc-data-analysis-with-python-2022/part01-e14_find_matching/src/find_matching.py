#!/usr/bin/env python3

def find_matching(lst,str):
    indexes = []
    for indx,i in enumerate(lst):
        if str in i:
            indexes.append(indx)
    return indexes
def main():
    pass

if __name__ == "__main__":
    main()
