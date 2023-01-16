#!/usr/bin/env python3

def main():
    count = 0
    for i in range (1,7):
        for j in range(1,7):
            if((i + j) == 5):
                print((i,j))
            count += 1

if __name__ == "__main__":
    main()
