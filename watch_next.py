# Import spacy and specify the model to be used.
import spacy
nlp = spacy.load('en_core_web_md')

# Create a string variable of the Hulk description.
hulk_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

def similar_movie(description):
    """This function takes a description of a watched movie and returns the movie that is most similar to it."""
    # Create a processed string and empty list to store similarity levels.
    nlp_watched = nlp(description)
    similarity_list = []

    # For each movie in the list add its similarity level with the watched movie to the list.
    for movie in movie_list:
        similarity_list.append(nlp_watched.similarity(nlp(movie)))

    # Get the movie that is most similar and return its title.
    most_similar_position = similarity_list.index(max(similarity_list))
    most_similar = movie_list[most_similar_position].split(" :")
    
    return most_similar[0]

# Read the movies.txt file and store the movies as a list of strings.
with open("movies.txt", "r", encoding="utf-8") as movies_file:
    movie_list = movies_file.readlines()

# Call the function to print the most similar movie to the Hulk.
print(f"The most similar movie to the Hulk is: {similar_movie(hulk_description)}")