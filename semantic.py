# Import spacy and specify the model to be used.
import spacy
nlp = spacy.load('en_core_web_md')

# ======== Code extract 1 =========
# Create variables of processed strings.
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# Print the similarity between each word.
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print()

# Note: 'cat and 'monkey' are similar as they are both animals. Also 'monkey' has a greater similarity with 'banana' than 'cat' does with 'apple' reflecting its diet.

# My own example of code extract 1
# Create variables of processed strings.
word1 = nlp("car")
word2 = nlp("bicycle")
word3 = nlp("petrol")

# Print the similarity between each word.
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print()

# Note: 'car' and 'bicycle' are similar as they are both vehicles. 'car' has greater similarity with 'petrol' than 'bicycle' does relfecting its energy source.



# ======== Code extract 2 =========
# Create a variable of a processed string.
tokens = nlp('cat apple monkey banana')

# For each token in the sentence print the similarity with tokens of the same sentence.
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
    print()


# ======== Code extract 3 =========
# Create a string variable of the model sentence.
sentence_to_compare = "Why is my cat on the car"

# Create a list of sentences.
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"
             ]

# Create variable of the processed string.
model_sentence = nlp(sentence_to_compare)

# For sentence in sentences print the similarity compared with the model sentence.
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

print()


# ======== Using simpler language model for similarity check =========

# When using 'en_core_web_sm' with the example.py file the following was noted:
# 'complaints' were less similar when compared with other 'complaints'
# 'recipes' were less similar when compared with other 'recipes'
# 'complaints' were less similar when compared with 'recipes'
# It said no word vectors loaded, so the result of the Doc.similarity method was based on the tagger, parser and NER, which may not give useful similarity judgements.
