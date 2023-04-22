import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("he went to school and they went to club.")
new = ""
for token in doc:
    if token.pos_ == "CCONJ":
        new += '. '
    else:
        new += " "+token.text; 
doc = nlp(new[1:])
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)

print(doc)
