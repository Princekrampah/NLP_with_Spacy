import spacy

# how NLP works using pipelines
# text >> tok2vec >> tagger >> parser >> ner(name entity recognizer) >> textcat (text classifier)


nlp = spacy.load("en_core_web_sm")

# you can get the entire pipeline of the nlp as follows
print(nlp.pipe_names)

# more descriptive >> For a list of component name and component function tuples,
#  you can use the nlp.pipeline attribute.
# woow!! print inside of a print works :(
print(print(nlp.pipeline))

doc = nlp("Hello world, with love")

# What the tagger section does: token.tag, token.pos

for token in doc:
    print(token.tag)
    print(token.pos)


# what the parser does: Token.dep, Token.head, Doc.sents, Doc.noun_chunks

for token in doc:
    print("token.dep ", token.dep)
    print("token.head ", token.head)



for sent in doc.sents:
    print("doc.sents", sent)


for noun_chunk in doc.noun_chunks:
    print("doc.noun_chunks", noun_chunk)
    

# What the ner does: Doc.ents, Token.ent_iob, Token.ent_type

for ent in doc.ents:
    print("Doc.ents ", ent)


for token in doc:
    print("token.ent_iob", token.ent_iob)
    print("token.ent_type ", token.ent_type)


# What textcat does: Doc.cats


# Because text categories are always very specific, 
# the text classifier is not included in any of the 
# trained pipelines by default. But you can use it 
# to train your own system.
for category in doc.cats:
    print("doc.cats", category)
