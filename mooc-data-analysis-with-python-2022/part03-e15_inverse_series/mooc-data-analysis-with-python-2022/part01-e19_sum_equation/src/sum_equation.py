#!/usr/bin/env python3

def sum_equation(stri):
    sum = 0
    if len(stri) == 0:
        return "0 = 0"
    streq = ""
    for i in range(len(stri)):
        if i == (len(stri)-1):
            sum = sum + stri[i]
            streq = streq + str(stri[i]) + " " + "=" + " "
        else:
            sum = sum + stri[i]
            streq = streq + str(stri[i]) + " " + "+" + " "
    streq = streq + str(sum)
    return streq

def main():
    pass

if __name__ == "__main__":
    main()
