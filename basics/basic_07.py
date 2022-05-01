import spacy

from spacy.matcher import Matcher

############### Rule-based Matching ##############

# This is very similar to regex, with the exception 
# that rule-based matching can work with Doc, Token attributes 
# and Token types in spacy. You can customize this b writing your own rules.
# example find a word in its noun form only and not its verb form, this 
# leverages the use of the trained model predictions


# match rules are usually a list of dictionary. The keys are the names of 
# token attributes, mapped to their expected values. 
# >> [{"TEXT": "iPhone"}, {"TEXT": "X"}]


# We can also match the lower case of the same text, since IPhone == iphone
# >> [{"LOWER": "iphone"}, {"LOWER": "x"}]


# We can even write patterns using attributes predicted by a model. Here, 
# we're matching a token with the lemma "buy", plus a noun. The lemma is 
# the base form, so this pattern would match phrases like "buying milk" 
# or "bought flowers". >> [{"LEMMA": "buy"}, {"POS": "NOUN"}]

nlp = spacy.load("en_core_web_sm")

text = "KSH100 Billion is a lot of money in Kenya"

# process text

doc = nlp(text)

for ent in doc.ents:
    print(ent, ent.label_)

# We can notice that the ents does not include KSH100 so how can we
# create a matcher to do just that.



# initialize the matcher with shared vocab
matcher = Matcher(nlp.vocab)

# create patter
pattern = [{"TEXT": "KSH100"}, {"TEXT": "Billion"}]
lower_pattern = [{"LOWER": "ksh100"}, {"LOWER": "billion"}]



# add pattern
matcher.add("KSH_pattern", [pattern, lower_pattern])


matches = matcher(doc)

# print(matches)

for id, start, end in matches:
    matche_span = doc[start:end]
    print(matche_span.text)




