
# NLP pipline architecture:
# text >> tokenizer >> tagger >> parser >> ner ...

# After the text is tokenized and a Doc object has been created, 
# pipeline components are applied in order. spaCy supports a 
# range of built-in components, but also lets you define your own.

# Custom components are executed automatically when you call the nlp object on a text.
# They're especially useful for adding your own custom metadata to documents and tokens.
# You can also use them to update built-in attributes, like the named entity spans.

# Anatomy of a component:
# Function that takes a doc, modifies it and returns it
# Registered using the Language.component decorator
# Can be added using the nlp.add_pipe method

# Fundamentally, a pipeline component is a function or callable that takes a doc, modifies 
# it and returns it, so it can be processed by the next component in the pipeline.

import spacy
from spacy.language import Language

nlp = spacy.load("en_core_web_sm")


@Language.component("my_custom_component")
def my_custom_component(doc):
    print(f"Length of the doc obj: {len(doc)}")
    return doc

# add it to the pipeline

# nlp.add_pipe("my_custom_component", before="tagger")

# add if as first component of the pipeline
# nlp.add_pipe("my_custom_component", first=True)

# add it as the last component of the pipeline
nlp.add_pipe("my_custom_component", last=True)

print(nlp.pipe_names)


doc = nlp("Hello world")

# custome components can be used to achieve the following:
# Computing your own values based on tokens and their attributes
# Adding named entities, for example based on a dictionary

