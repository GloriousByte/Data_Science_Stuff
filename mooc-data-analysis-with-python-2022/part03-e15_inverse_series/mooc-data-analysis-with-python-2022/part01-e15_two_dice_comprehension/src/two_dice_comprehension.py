#!/usr/bin/env python3

def main():


    dices = [(a,b) for a in range (1,7)
             for b in range (1,7)
             if a+b ==5]
    for die in dices:
        print((die))


if __name__ == "__main__":
    main()
