#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    ind = []
    series = []
    for index,val in s.items():
        ind.append(index)
        series.append(val)
    return pd.Series(ind, index = series)

def main():
    l1 = pd.Series([1,2,3,1],index = list("abcd"))
    hello = inverse_series(l1)
    print(hello)

if __name__ == "__main__":
    main()
