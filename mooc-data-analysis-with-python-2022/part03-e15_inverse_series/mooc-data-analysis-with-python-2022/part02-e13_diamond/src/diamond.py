#!/usr/bin/env python3

import numpy as np

def diamond(val):
    if val == 1:
        return np.eye(1).reshape(1,1)
   
  
    rightupper = np.eye(val,dtype=int)
    rightlower = rightupper[1:,::-1]
    right = np.concatenate((rightupper,rightlower))
    #print(right)
    left = right[:,1:]
    newleft = left[:,::-1]
    #print(newleft)
    full = np.concatenate((newleft,right),axis = 1)
    return full

def main():
    print(diamond(5))

if __name__ == "__main__":
    main()
