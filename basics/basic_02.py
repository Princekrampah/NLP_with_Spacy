import spacy

################# Working with Doc object #######################
# When you call nlp on a string, spaCy first tokenizes the text and 
# creates a document object. In this exercise, 
# you’ll learn more about the Doc, as well as its views Token and Span.

# this is using a pretrained model
# nlp = spacy.load("en_core_web_sm")

# use a non-pretrained model
nlp = spacy.blank("en")

doc = nlp("Hello world, this is me")

print(doc)

print(doc[0])
print(doc[2:-1])

print(doc[0].text)