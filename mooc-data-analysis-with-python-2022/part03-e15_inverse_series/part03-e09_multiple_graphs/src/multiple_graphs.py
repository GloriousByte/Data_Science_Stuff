#!/usr/bin/env python3

import matplotlib.pyplot as plt

def main():
    x = [2,4,6,7]
    y = [4,3,5,1]

    a = [1,2,3,4]
    b = [4,2,3,1]

    plt.plot(x,y)
    plt.plot(a,b)
    plt.xlabel("x-axix")
    plt.ylabel("y-axis")
    plt.title("title")
    plt.show()

    

if __name__ == "__main__":
    main()
