import pandas as pan
import numpy as n

students_classes = {
    'Kofi' : 'English',
    'Ama' : 'twi',
    'Okyere' : 'Physics'
}

s = pan.Series(students_classes)
print(s)
print(s.iloc[0])
print(s.iloc[2])
print(s.loc['Kofi'])

"""
slow methods.
grades = pan.Series([10,30,56,78])
sum = 0
for grade in grades:
    sum = sum + grade

print('The aum using pandas is',sum)

Bgrades = [10,30,56,78]
Bsum = 0
for grade in Bgrades:
    Bsum = Bsum + grade

print('The aum using pandas is',Bsum)
"""

#method using numpy
grades = pan.Series([34,56,34])
total = n.sum(grades)
print(total)

grades+=5
print(grades)