#!/usr/bin/env python3
from math import sqrt
import sys
import sys

def summary(filename="example.txt"):
    Sum = 0
    count = 0
    li = []

    with open(filename) as f:
    
        for line in f:
            if line[0] in "abcdefghijklmnopqrstuvwxyz":
               continue
            
            
            li.append(float(line))
            Sum += float(line)
            count += 1
            
    
    if Sum > 0:
       
        ave = Sum/count
    else:
         return(0.0,0.0,li[0])
    
    for key,val in enumerate(li):
        li[key] = (val - ave)**2
    sd = (sum(li))/(len(li)-1)
    sd = sqrt(sd)

    return (Sum,ave,sd)

def main():
    """res = summary("example3.txt")
    if res == None:
        pass
    else:
        print(f"Sum: {res[0]:.6f}: Average: {res[1]:.6f} Stddev: {res[2]:.6f}")

    """

    for i in range(1,len(sys.argv)):
        
        res = summary(sys.argv[i])
        print(f"File: {sys.argv[i]} Sum: {res[0]:.6f} Average: {res[1]:.6f} Stddev: {res[2]:.6f}")
    
if __name__ == "__main__":
    main()
