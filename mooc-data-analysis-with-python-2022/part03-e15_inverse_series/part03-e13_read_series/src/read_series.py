#!/usr/bin/env python3

from logging import raiseExceptions
import pandas as pd

def read_series():
    dic = {}
    try:
        while True:
            val = input("please enter two strings separted by white space")

            if val == "":
                break

            keyval = val.split()
            if len(keyval) == 1:
                raise Exception("split at whitespace is false")
            dic[keyval[0]] = keyval[1]
    except:
        raise Exception("")
    return pd.Series(dic)

def main():
   hello = read_series()
   print(hello["haha"])

if __name__ == "__main__":
    main()
