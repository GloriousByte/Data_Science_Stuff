import re

text_for_search = """

little drops of water and gradually you would get there
level 100 was just yesterday
level 200 was just yesterday
after WASSCE dots life  is fresh in memory
it's like 7 years

ababababab. cacacaca
There's a target.
There's a plan. A destination. A route. An estimation of arrival. Wommack
It's frustrating that we are not there still
But stopping does that. Getting frustrated and stopping does this
You have gotta move to get there. The only way to get there is to move
Kdrama for your sanity
Wommack for your sanity
Unless they cut of feeding entirely, doing own thing. Doing club. Doing studies
Club necessary to account for inactiveness for scholarship application.
Wommack
Intership with AI guys too. That's why I am typing this even

abcabcabcggggg

345-456-433
095---456-433
689.345.222
2ommack
dommack
hommack

Mr.     Schafer
Mrs Smith
Mr W
Mr& Joe
Mrs Haha hha
Mw Jones
Mz Boness
Mrs   
"""

sentence = "start a sentence. Now bring it to an end"
#pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d')
pattern = re.compile(r'Mr\.?\s[A-Z][A-Za-z]*')
#groups use parenthesis
matches = pattern.finditer(text_for_search)
patternB = re.compile(r'(Mr|Mrs|Mw|Mz|Mr&)\.?\s+(\w+\s\w+\n|w+)')
matchesB = patternB.finditer(text_for_search)
#for match in matches:
 #   print(match)

for match in matchesB:
    print(match)
print("helloo")


'''with open("data.txt","r") as myFileAPI:
    contents = myFileAPI.read()

    matches = pattern.finditer(contents)

    for match in matches:
        print(match)
'''