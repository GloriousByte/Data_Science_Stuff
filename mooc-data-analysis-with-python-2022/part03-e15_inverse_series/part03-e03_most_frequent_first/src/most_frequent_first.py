#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    arr = np.unique(a[:,c],return_index=True, return_counts=True, )
    return arr

def main():
    arr = np.array([[2,3,4,5],[2,1,7,5],[8,9,5,2],[8,10,5,5],[9,9,5,2],[2,3,1,0]])
    print(most_frequent_first(arr,-1))

if __name__ == "__main__":
    main()
