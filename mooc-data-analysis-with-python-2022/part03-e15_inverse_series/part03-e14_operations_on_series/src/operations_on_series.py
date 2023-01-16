#!/usr/bin/env python3
import pandas as pd

def create_series(L1, L2):
    return (pd.Series(L1,index=list("abc")), pd.Series(L2, index=list("abc")))
    
def modify_series(s1, s2):
    s1["d"] = s2["b"]
    del(s2["b"])
    return (s1, s2)
    
def main():
    ls, ls2 = create_series([1,2,3],[2,3,4])
    hello,hi = modify_series(ls,ls2)
    print(hello + hi)



if __name__ == "__main__":
    main()
