import pandas as pan

record1 = pan.Series({'Name':'Kay',
                      'class' : 'beauty',
                      'score' : 89
                     })

record2 = pan.Series({'Name':'Jane',
                      'class' : 'beauty',
                      'score' : 87
                     })

record3 = pan.Series({'Name':'Kwadwo',
                      'class' : 'beauty',
                      'score' : 60
                     })

record4 = pan.Series({'Name':'Saah',
                      'class' : 'beauty',
                      'score' : 67
                     })

df = pan.DataFrame([record1,record2,record3,record4],index=['school1','school2','school3','school3'])

print(df)

print(type(df.loc['school2']))

print(df.loc['school3','score'])
print('\n')
#how to print out only columns
print('hello',df['Name'])
print('\n')
print('hi',df)
print('\n')
print(df.T)

print(df.T.loc['Name'])
print('hello',df['Name'])
print('\n')
print(type(df.loc['school3']))
print('\n')
print(df.loc[:,['Name','class']],'\n')

df_copy = df.copy()
df_copy.drop('score', inplace=True, axis = 1)
print(df_copy,'\n')
df_copy['status'] = None
print(df_copy)