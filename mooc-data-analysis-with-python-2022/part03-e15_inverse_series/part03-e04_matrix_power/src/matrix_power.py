
from functools import reduce
import numpy as np

def matrix_power(a, n):
    if len(a) == False:
        return a

    if n == 0:
        return np.eye(2)

    if n  < 0:
        b = np.linalg.inv(a)
        return reduce(np.matmul, [b for __ in range(n*(-1))])

    res = reduce(np.matmul, [a for __ in range(n)])
    
    return res

def main():
    print(matrix_power(np.array([[2,3,4],[3,2,3],[3,6,5]]),-1))

if __name__ == "__main__":
    main()
