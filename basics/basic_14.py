import spacy

# word vectors word2vector

nlp = spacy.load("en_core_web_md")

doc = nlp("This is the sport car")

# Spacy implements vectors under the hood to 
# find out the similarity between words
print(doc[4].vector)



