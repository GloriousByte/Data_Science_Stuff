import re

emailss = """
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my_work.net
"""

myPattern = re.compile(r'[a-zA-Z]+[\.\-a-zA-Z\d]+@[a-zA-Z_]+\.[a-z]+')
matches = myPattern.finditer(emailss)

for match in matches:
    print(match)
