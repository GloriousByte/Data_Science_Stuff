#!/usr/bin/env python3

def word_frequencies(filename="src/alice.txt"):
    dic = {}
    with open(filename) as f:
        content = f.read()
        list_of_words = content.split()
        
        
        for key, word in enumerate(list_of_words):
            list_of_words[key] = (word.strip("""!"#$%&'()*,-./:;?@[]_"""))
    
    for word in list_of_words:
        if word not in dic:
            dic[word] = 1
            continue
        dic[word] += 1



    return dic

def main():
    word_frequencies("alice.txt")
    

if __name__ == "__main__":
    main()
