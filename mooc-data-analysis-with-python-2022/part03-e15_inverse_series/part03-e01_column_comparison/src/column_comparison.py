#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    res = a[:,1] > a[:,-2]
    return a[res]
    
def main():
    hi = np.array([[8,9,3,8,8],[0,5,3,9,9],[5,7,6,0,4],[5,7,6,0,4],[2,1,3,5,8]])
    print(column_comparison(hi))

if __name__ == "__main__":
    main()
