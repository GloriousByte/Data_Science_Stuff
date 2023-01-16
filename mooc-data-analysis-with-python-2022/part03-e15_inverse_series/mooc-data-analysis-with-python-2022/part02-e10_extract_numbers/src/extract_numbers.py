#!/usr/bin/env python3

def extract_numbers(s):
    ls = s.split()
    arr = []
    for i in ls:
        try: 
            arr.append(int(i))
    
        except ValueError:
            try:
                arr.append(float(i))
            except ValueError:
                pass

    return arr

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
