import re

text_for_search = """
dance little drops of water made a mighty ocean
It was pee. From a bird up above
And that's about all that bird ever did
after flying with the clouds, and bein inspired
by the stars.
It's biggest dream was to pee.

ababababab. cacacaca dance
Chicken don't pee
dance There's a plan. A destination. A route. An estimation of arrival. Wommack
It's frustrating that chickens cant dance
But stopping does that. Getting frustrated and stopping does this.
dance You have gotta move to get there. The only way to get heo there is to move
Eat vegies for your sanity heo
Corn for your sanity dance
Unless they cut of feeding entirely, doing own helllo thing. Doing club. Doing studies
Club necessary boom boom dance hewo
She loves me a whole lot.

abcabcabcggggg
acacaddac
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

tellme = re.search("dance",text_for_search)
print("I am tellme",tellme)

#Btellme = re.split("dance",text_for_search)
#print("I am Btellme",Btellme)

Ctellme = re.findall("dance",text_for_search)
print(Ctellme)

Dtellme = re.findall("[a][a-d]",text_for_search)
print("Dtellme",Dtellme)

Etellme = re.findall("[a][a|b|c|d]",text_for_search)
print("SEE ME!!!",Etellme)

for match in Ctellme:
    print(match)

print("hiiiiiiii"[0])


"""for match in tellme:
    print(match)
print("helloo")
"""



'''with open("data.txt","r") as myFileAPI:
    contents = myFileAPI.read()

    matches = pattern.finditer(contents)

    for match in matches:
        print(match)
'''

blueprint = re.compile(r'\she\w*o\s[a-zA-Z]')
matcheblue = blueprint.finditer(text_for_search)

for match in matcheblue:
        print(match)