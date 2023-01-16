#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    a = np.square(a)
    a = np.sum(a,axis=1)
    a = np.sqrt(a)
    return a

def main():
    a = np.arange(12).reshape(2,6)
    print(vector_lengths(a))
    
if __name__ == "__main__":
    main()
