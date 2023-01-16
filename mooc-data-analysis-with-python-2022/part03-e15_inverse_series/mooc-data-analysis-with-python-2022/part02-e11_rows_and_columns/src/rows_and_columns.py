#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    ls = []
    for i in a:
        ls.append(i)
    return ls

def get_columns(a):
    b = a.T
    ls = []
    for i in b:
        ls.append(i)
    return ls

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
