#!/usr/bin/env python3


def acronyms(str):
    lst = []
    strlist = str.replace(","," ").split()
    print(strlist)
    for word in strlist:
        print(word)
        count = 0
        strl = ""
        for letter in word:
            if (letter.isupper() or letter in "123456789"):
                count += 1
                strl = strl + letter
               
                print(count)
            elif (count < 2):
                    count = 0
                    strl = ""
    
        if (count >= 2):
            lst.append(strl)
        for i in lst:
            count = 0
            for j in i:
                if j in "123456789":
                    count+=1
            if len(i) == count:
                lst.remove(i)

    return lst


def main():
    print(acronyms("""For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""))


if __name__ == "__main__":
    main()
