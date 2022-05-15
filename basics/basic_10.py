# creating docs manually
import spacy
from spacy.tokens import Doc

nlp = spacy.blank("en")

words = ["NLP", "is", "awesome"]
# spaces basically tell if there is a space 
# after a given word or not
spaces = [True, True, False]

# create a document
doc = Doc(nlp.vocab, words=words, spaces=spaces)

print(doc.text)
