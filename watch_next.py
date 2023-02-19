# Compulsory Task 2 - Semantic Similarity(NLP) watch_next

# The program below will tell you what to watch next based on the word vector
# similarity of the description of the movies.

# Import spaCy

import spacy

# Loading language model:

nlp = spacy.load('en_core_web_md')

# Description of the main movie all movies will be compared with

hulk = '''Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''

sim_data = []
key_data = []
movies = {}
main_descr = nlp(hulk)


# Function below will read movie descriptions from textfile, reformatting them
# into dictionary items

def extract():

    with open('movies.txt', 'r') as movies_file:
        for i, line in enumerate(movies_file):
            try:
                key, value = line.strip().split(':')
            except ValueError:
                print(i, line)
            movies[key] = value


# Function below will compute similarity of descriptions to main movie description
# The movie with the highest similarity should then be returned

def most_similar(main_descr):

    for key, value in movies.items():
        similarity = nlp(value).similarity(main_descr)
        sim_data.append(similarity)
        key_data.append(key)

    new_dict = dict(zip(key_data, sim_data))
    most = max(new_dict, key=new_dict.get)
    return most


# Calling functions defined above and printing out the title of the most similar movie

extract()
most_similar(main_descr)
print(f'Most similar movie is {most_similar(main_descr)}')
