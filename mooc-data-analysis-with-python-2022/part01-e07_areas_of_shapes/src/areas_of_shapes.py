#!/usr/bin/env python3

import math


def main():
    
    # enter you solution here
    A = ['triangle','rectangle','circle']
    while True:
        shape = input(f"Choose a shape (triangle, rectangle, circle):")
        if shape == "":
            break
        if shape not in A:
            print(f"Unknown shape!")
            continue
        if shape == A[0]:
            base = float(input("Give base of the triangle"))
            height = float(input("Give height of the triangle"))
            area = ((1/2)*base)*height
            print(f"The area is {area:6f}")
        elif shape == A[1]:
            width = float(input(f"Give width of the rectangle:"))
            height = float(input(f"Give height of the rectangle:"))
            area = width * height
            print(f"The area is {area:6f}")
        elif shape == A[2]:
            radius = float(input(f"Give radius of the circle:"))
            area = math.pi * radius**2
            print(f"The area is {area:6f}")

        
        



if __name__ == "__main__":
    main()
