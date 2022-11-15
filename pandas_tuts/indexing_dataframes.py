import pandas as pan
df = pan.read_csv('/home/sir/Data_Science_Stuff/python_with_Corey/files_and_regex/contacts.txt', index_col=0)
print(df.head(),'\n')
print(df.index,'\n')
#df['keykey'] = df.index
df = df.set_index('random')
#print(df['keykey'], '\n')
df = df.reset_index()

print(df,'\n')
print(df['random'].unique(),'\n')
print(df['random'] == 5,'\n')
print(df[df['random'] == 5],'\n')

columns_to_keep = ['random','mail','lname']
df = df[columns_to_keep]
print(df,'\n')

new_df =df.set_index(['random','mail'])
print(new_df,'\n')
print(new_df.loc[[(4,"JA@JA.boo"),(9,"AB@AB.boo")]])