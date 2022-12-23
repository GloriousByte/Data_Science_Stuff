import csv
import pandas as pan

def boo():
    jerry = []
    for x in range(0,12):
        for y in range(0,12):
            print((x*y)," ", end="")
            jerry.append(x*y)
        print("\n")
    return jerry

jerry= [x*y for x in range(0,12) for y in range(0,12)]
hahaho = boo()
print("IS JERRY EQUAL TO HAHAHO\?", jerry==hahaho)



df = pan.read_csv('/home/sir/Data_Science_Stuff/python_with_Corey/files_and_regex/contacts.txt')
mask = df.isnull()
print(mask,'\n')

#df.fillna(0, inplace=True)
print(df,'\n')

new_df = df.dropna(0)
print(new_df,'\n')

print(df.replace(5,500),'\n')

print(df,'\n')

print(df.replace(to_replace="(?<=\.)j[a-zA-Z]+", value="domain", regex=True))