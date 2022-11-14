import pandas as pan
students = ['Alice','Jack','MOlly']
print(pan.Series(students))

Bstudents = ['Alice','Jack','MOlly',None]
print(pan.Series(Bstudents))

Cstudents = [1,2,4,None]
print(pan.Series(Cstudents))

students_scores = {
    'Kofi': 'pysics',
    'Ama' : 'chemistry',
    'Adjetey' : 'English'
}

res =pan.Series(students_scores)
print(res)
print(res.index)

Dstudents = [('Alice','Jane',5),('Jack',45),('MOlly','Jay'),None]
Bres = pan.Series(Dstudents)
print(Bres)

print(pan.Series(['Alice','Adams','Kofi'], index = ['constipation','vulgar','gentleman']))