import spacy

nlp = spacy.blank("en")
doc = nlp("Hello world, this is the world")

hash_code = nlp.vocab.strings["world"]
print(hash_code)


string_value = nlp.vocab.strings[hash_code]
print(string_value)

