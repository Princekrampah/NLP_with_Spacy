import spacy
from spacy.tokens import Doc, Span

# Perfect! Creating spaCy's objects manually and modifying the entities
# will come in handy later when you're writing your own information extraction
# pipelines.

nlp = spacy.blank("en")

words = ["I", "love", "Python", "programming", "language"]
spaces = [True, True, True, True, False]

# create a document obj
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

# create a span to label "Python" as a "Programming language"
span = Span(doc=doc, start=2, end=5, label="Programming language")
print(span.text, span.label_)


# Add the span to the newly created document
doc.ents = [span]

# print out the content
print([(ent.label_, ent.text) for ent in doc.ents])
