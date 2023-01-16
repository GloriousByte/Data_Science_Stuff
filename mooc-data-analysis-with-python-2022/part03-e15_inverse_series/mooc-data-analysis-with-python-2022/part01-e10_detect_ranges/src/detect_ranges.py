#!/usr/bin/env python3
def range_finder(start_index,list):
    i = start_index
    count = 0
    con = True
    while con:
        if (i < len(list)-1):
            if (list[i]+1 == list[i+1]):
                i +=1
                count +=1
            else:
                con = False
        else:
            con = 0
           

    return start_index,i,count

  

def detect_ranges(lst):
    list = sorted(lst)
    next_step = 0
    while next_step < (len(list)-1):
  
        result = range_finder(next_step,list)

        start = result[0]
        end = result[1]
        next = result[2]
        next_step = start + 1
        if(start != end):
            list[start] = (list[start],(list[end]+1))
          
            del_from = start + 1
            while del_from <= end:
                del(list[start + 1])
                del_from += 1
           
        else:
            next_step = start + 1
        return list
def main():
    L = [-4, -2, 0, 2, 4]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
