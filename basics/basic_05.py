import spacy

########## Predicting Syntatic-dependencies ############


# load pretrained model
nlp  = spacy.load("en_core_web_sm")

text = "Hello this is a boy, he likes coding addictively"


# process text into a spacy doc
doc = nlp(text)

for token in doc:
    # the .dep_ predicts the depencies and the .head.text 
    # returns the work the parent token the current word is attached too
    print(token.text, token.pos_, token.head.text, token.dep_)


# spacy explain 

print(spacy.explain("dobj"))
print(spacy.explain("DET"))
print(spacy.explain("INTJ"))

