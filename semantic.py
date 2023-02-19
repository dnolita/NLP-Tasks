import spacy

nlp = spacy.load('en_core_web_md')

# similarity in words

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("meow")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print(word4.similarity(word1))
print(word4.similarity(word2))
print()

'''
 I found it interesting that in running the code above:
 With the first 3 words:
 
    - there was a fair amount of similarity found between a monkey and a banana,spaCy 
    seems cognisant that monkeys like to eat bananas.
    - the higher similarity between cat and monkey would point to both being animals.
    
 Then with additional 4th word "meow":
 
    - there is an almost perfect similarity found between a cat and the word meow
    - a fair amount of similarity was found between monkey and meow which probably
     stems from the cat's relationship with meow and both the cat and monkey being animals.       
    
'''

# similarity in a series of words

tokens = nlp('cat meow monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print()

# similarity in sentences

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Felix"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
