# Task 21 - Compulsory Task 2

import spacy  # importing spaCy
from pathlib import Path # import Path

nlp = spacy.load('en_core_web_md')

# open the movie.txt file
with open(f"movies.txt", "r") as file:
    file_contents = file.read()


# Planet Hulk description
Hulk_des = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the 
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk lands on the 
planet Sakaar where he is sold into slavery and trained as a gladiator.'''

# Runs Hulk_des through spaCy
model_sentence = nlp(Hulk_des)

def movie_recommendation(Movie_description):
    # Runs Hulk_des through spaCy
    model_sentence = nlp(Movie_description)
    highest_sim_score = -1.0
    most_similar = ""
    
    # Opens file
    movies = Path("movies.txt").read_text().splitlines() 
    
    for other_movie_des in movies:  # for movie description in text file
        # find similarity score = compare OG description with txt.file descriptions(run through spacy)
        similarity_score = model_sentence.similarity(nlp(other_movie_des)) 
        
        if similarity_score > highest_sim_score: # if similarity score higher than highest similarity score
            highest_sim_score = similarity_score # then highest similarity score becomes highest similarity score
            most_similar = other_movie_des # update most_similar list to descsription with highest similarity
    
    return most_similar

print(f"Based on your previous movie it sounds like you would really enjoy:\n {movie_recommendation(model_sentence)}")
    
