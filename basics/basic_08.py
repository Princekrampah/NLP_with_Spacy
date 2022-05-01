import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")

text = "The year 2022 is going to be the best"

# process text
doc = nlp(text)

matcher = Matcher(nlp.vocab)

pattern = [
    # make sure the the is lower case
    {"LOWER": "the"},
    {"LOWER": "year"},
    {"IS_DIGIT": True},
    {"LOWER": "is"},
    {"LOWER": "going"}
]

matcher.add("Custom_pattern", [pattern])

matches = matcher(doc)

for matche_id, start, end in matches:
    matche_span = doc[start:end]
    print(matche_span.text)

print(" ....")

