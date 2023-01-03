#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():

    print(triangle.hypothenuse(2,3))
    print(triangle.area(3,3))
    # Call the functions from here

if __name__ == "__main__":
    main()
