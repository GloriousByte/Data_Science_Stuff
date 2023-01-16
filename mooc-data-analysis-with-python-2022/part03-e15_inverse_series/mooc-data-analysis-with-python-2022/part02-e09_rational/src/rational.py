#!/usr/bin/env python3

class Rational(object):
    def __init__(self,a,b):
        self.__boom = f"{str(a)}/{str(b)}"
        self.__vals = self.__boom.split('/')
        self.conum = round(float(int(self.__vals[0])/int(self.__vals[1])),3)

    
    def __str__(self):
        
        return f"{self.__vals[0]}/{self.__vals[1]}"
    
    def __add__(self,other_r):
        
        if type(other_r) == Rational:
            val = float(int(self.__vals[0])/int(self.__vals[1])) + float(int(other_r.__vals[0])/int(other_r.__vals[1]))
            ls = val.as_integer_ratio()
            return Rational(ls[0],ls[1])
        else:
            val = float(int(self.__vals[0])/int(self.__vals[1])) + other_r
            ls = val.as_integer_ratio()
            return Rational(ls[0],ls[1])

    def __radd__(self,other_r):
        return self.__add__(other_r)
        
    def __sub__(self,other_r):
        if type(other_r) == Rational:
             val = float(int(self.__vals[0])/int(self.__vals[1])) - float(int(other_r.__vals[0])/int(other_r.__vals[1]))
             ls = val.as_integer_ratio()
             return Rational(ls[0],ls[1])
        else:
            val = float(int(self.__vals[0])/int(self.__vals[1])) + other_r
            ls = val.as_integer_ratio()
            return Rational(ls[0],ls[1])

    def __rsub__(self,other_r):
 
            return  other_r - float(int(self.__vals[0])/int(self.__vals[1])) 


    def __mul__(self,other_r):
        if type(other_r) == Rational:
            val = round(float(int(self.__vals[0])/int(self.__vals[1])) * float(int(other_r.__vals[0])/int(other_r.__vals[1])),6)
            ls = val.as_integer_ratio()
            return Rational(ls[0],ls[1])
        else:
            val=  round(float(int(self.__vals[0])/int(self.__vals[1])) * other_r,6)
            ls = val.as_integer_ratio()
            return Rational(ls[0],ls[1])

    def __rmul__(self,other_r):
        return round(self.__mul__(other_r),6)

    def __truediv__(self,other_r):
         if type(other_r) == Rational:
            return float(int(self.__vals[0])/int(self.__vals[1])) / float(int(other_r.__vals[0])/int(other_r.__vals[1]))
         else:
            return float(int(self.__vals[0])/int(self.__vals[1])) / other_r

    def __rtruediv__(self,other_r):
        return  other_r / int(int(self.__vals[0])/int(self.__vals[1])) 

    def __eq__(self,other_r):
        if type(other_r) == Rational:
            if self.conum == other_r.conum:
                return True
            else:
                return False
        else:
            return self.conum == other_r

    def __lt__(self,other_r):
        if self.conum < other_r.conum:
            return True
        else:
            return False

    def __rt__(self,other_r):
        if self.conum > other_r.conum:
            return True
        else:
            return False

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))
    print((1/2)==(2/4))
    print((1/2)>(2/4))
    print((1/2)<(2/4))

if __name__ == "__main__":
    main()
