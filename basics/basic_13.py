# Word vectors and semantic similarities
import spacy

# here we use the move advanced medium model since it has word vectors
# the en_core_we_sm will not work in this case, use either the md or the lg models
nlp = spacy.load("en_core_web_md")

doc1 = nlp("I love python programming")
doc2 = nlp("I love java programming language")

# compare the two docs, it will return a value between 0 and 1
print(doc1.similarity(doc2))

