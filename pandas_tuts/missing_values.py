import pandas as pan
df = pan.read_csv('/home/sir/Data_Science_Stuff/python_with_Corey/files_and_regex/contacts.txt')
mask = df.isnull()
print(mask,'\n')

#df.fillna(0, inplace=True)
print(df,'\n')

new_df = df.dropna(0)
print(new_df,'\n')

print(df.replace(5,500),'\n')

print(df,'\n')

print(df.replace(to_replace="(?<=\.)[a-zA-Z]+", value="domain", regex=True))