#!/usr/bin/env python3


def main():
    for i in range(1,11):
        for j in range(1,10):
            print("{:4d} ".format(i*j),end="")
        print("{:4d} ".format(i*10))

if __name__ == "__main__":
    main()
