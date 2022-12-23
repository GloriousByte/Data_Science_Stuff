#!/usr/bin/env python3

import sys

from numpy import empty

def file_count(filename="test.txt"):
    lines = 0
    words = 0
    chr = 0
    with open(filename) as file:
        for line in file:
            lines += 1
            list_of_words = line.split()
         
            if len(list_of_words) == 0:
                continue
              
         
            
            words += len(list_of_words)
            for word in list_of_words:
                for ch in word:
                    chr += 1

        
    return (lines, words, chr)

def main():
    #res = file_count("test.txt")
    #print(f"{res[0]}\t{res[1]}\t{res[2]}")
  
    for i in range(1,len(sys.argv)):
        res = file_count(sys.argv[i])
        print(f"{res[0]}\t{res[1]}\t{res[2]}\t{sys.argv[i]}")
    

    
if __name__ == "__main__":
    main()
