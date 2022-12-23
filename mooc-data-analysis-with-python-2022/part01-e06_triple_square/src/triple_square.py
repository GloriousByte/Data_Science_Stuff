#!/usr/bin/env python3


def main():
    for i in range(1,11):
        trip = triple(i)
        sq = square(i)
        if sq > trip:
            break
       
        print(f"triple({i})=={trip} square({i})=={sq}")

def triple(x):
    return x * 3
        

def square(x):
    return x**2

if __name__ == "__main__":
    main()
