import spacy

########## Parts-of-speech Tags ############


# load pretrained model
nlp  = spacy.load("en_core_web_sm")

text = "Hello this is a boy, he likes coding addictively"

# process text into a spacy doc
doc = nlp(text)

for token in doc:
    print(token.text, token.pos_)

