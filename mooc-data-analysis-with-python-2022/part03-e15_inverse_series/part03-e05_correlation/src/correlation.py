#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    arr = load()
    sep_len = arr[:,0]
    pet_len = arr[:,2]
    res = scipy.stats.pearsonr(sep_len,pet_len)
    return np.array(res)[0]

def correlations():
    arr = load()
    sep_len = arr[:,0]
    pet_len = arr[:,2]
    sep_width = arr[:,1]
    pet_width = arr[:,3]
    res = np.corrcoef([sep_len,sep_width,pet_len,pet_width])
    return res

def main():
    print(lengths())
    print(correlations())
    #print(load())

if __name__ == "__main__":
    main()
