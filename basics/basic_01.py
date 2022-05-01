# Import spaCy
import spacy

################### Working with languages #######################

# Create the English nlp object
# nlp = spacy.load("en_core_web_sm")

# Create the German nlp object
nlp = spacy.load("de_core_news_sm")

# Create the Spanish nlp object
# nlp = spacy.load("es_core_news_sm")

# Process English text
# doc = nlp("This is a sentence.")

# Process German text
doc = nlp("Liebe Grüße!")

# Process spanish text
# doc = nlp("¿Cómo estás?")

# Print the document text
print(doc.text)



