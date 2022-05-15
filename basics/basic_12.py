import spacy

# program to return all proper nouns that appear 
# before a verb in a sentence

# load the english model
nlp = spacy.load("en_core_web_sm")
# create a document obj
doc = nlp("Berlin looks like a nice city")


for token in doc:
    # check if a given word is a Proper noun in POS
    if token.pos_ == "PROPN":
        # to avoid the code failing in case the last word is a proper noun
        if len(doc) < token.i + 1:
            # check if the word is a verb
            if doc[token.i + 1].pos_ == "VERB":
                print(f"Proper nouns before a verb: {token.text}")

