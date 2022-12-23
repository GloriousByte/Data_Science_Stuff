#!/usr/bin/env python3

def interleave(*boo):
  
    result = zip(*boo)
    l =[]
    for i in result:
        for j in i:
            l.append(j)

        print(i)
    return l



def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
