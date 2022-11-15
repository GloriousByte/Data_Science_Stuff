import pandas as pan

df = pan.read_csv('/home/sir/Data_Science_Stuff/python_with_Corey/files_and_regex/contacts.txt')
print(df.head(),'\n')

#notice the error with 'fname '. We shouldn't have added a space. Therefore, it won't change the name 

new_df = df.rename(columns = {'fname ':'firstname','lname':'lastname','mail':'mail'})
print(new_df.head(),'\n')

#now, let's fix our mistake

Bnew_df = new_df.rename(columns={'fname':' FirsTnaMe'})
print(Bnew_df.head(),'\n')

#another method is to use a fuction to strip off white spaces. Over here, we are using the strip()
#from the str class. Note that we aren't calling the function immediately. Pandas would call it when
#creating the new data frame. We tell it to do so by using the 'mapper' method/arrtibute? -not sure.
#havn't looked at the docs

Cnew_df = Bnew_df.rename(mapper=str.strip, axis='columns')
print(Cnew_df,'\n')

#returning a copy of Bnew_df but with all lowercase

cols = list(Bnew_df.columns)
print(cols,'\n')

#cols = [x.lower().strip() for x in cols]
def new_word(word):
    boo = list(word)
    boo[0] = 'h'
    wordy=""
    for x in boo:
        wordy += x
    return wordy

cols = [ new_word(x) for x in cols]
Bnew_df.columns = cols
print(Bnew_df.head())