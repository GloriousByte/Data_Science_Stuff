with open('opentest.txt','r') as a:
    a_contents = a.readline()
    print(a_contents)

    a_contents = a.readline()
    print(a_contents)

print("Moment of truth")
print(a_contents)
  


"""with open('opentest.txt','r') as a:
    size_to_read = 3
    a_contents = a.read(size_to_read)
    while len(a_contents) > 0:
        print(a_contents, end='*')
        a_contents = a.read(size_to_read)
    print(a_contents)
"""
