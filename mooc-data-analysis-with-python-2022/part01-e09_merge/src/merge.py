#!/usr/bin/env python3

def merge(L1, L2):
    res = L1+ L2
    return sortit(res)
   
    
def sortit(list):
    for i in range(len(list)-1):
        flag = 0
        for j in range((len(list)-1) - i):
            if (list[j] > list[j+1]):
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp
                flag = 1
        if(flag == 0):
            break
    return list

def main():
    a=[4,8,3,5,0]
    b =[3,5,5,4,2,1,]
    hello = merge(sorted(a),sorted(b))
    print(hello)

if __name__ == "__main__":
    main()
