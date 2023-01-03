#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    table = np.arange(n)
    scaler = np.arange(n).reshape(n,1)
    result = table * scaler
    return result

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
