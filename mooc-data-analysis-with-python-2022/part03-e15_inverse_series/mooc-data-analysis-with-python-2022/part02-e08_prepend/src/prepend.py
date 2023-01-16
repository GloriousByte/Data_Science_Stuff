#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self, string:str) -> None:
        self.start = string
    
    def write(self,st:str):
        self.s = self.start +  st
        print(self.s)
        

def main():
    ins = Prepend("Hello")
    ins.write("+++")

if __name__ == "__main__":
    main()
