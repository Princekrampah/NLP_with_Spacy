import spacy

########## Predicting name entities ###########


# load pretrained model
nlp = spacy.load("en_core_web_sm")


text = "This is an awesome $100 billion project called wilio"

text2 = "FaceBook change its name to Metamask now Metamask is the parent company of WhatsApp. Whatsapp was purchased for $19 billion."

# process text into a spacy doc
doc = nlp(text2)

for ent in doc.ents:
    print(ent.text, ent.label_)



print(spacy.explain("ORG"))
print(spacy.explain("MONEY"))


