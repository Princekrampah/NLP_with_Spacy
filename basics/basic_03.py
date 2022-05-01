import spacy

nlp = spacy.blank("en")

doc = nlp("Hello word, this is a greate day to work on NLP and machine learning. 100% new to spacy. What about you 40-30%?")


for token in doc:
    # print(token)
    # print(token.i)

    if token.like_num:
        # get the next token
        next_token = doc[token.i + 1]

        if next_token.text == "%":
            print(token.text + next_token.text)
            

