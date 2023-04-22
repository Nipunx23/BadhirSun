import spacy

nlp = spacy.load("en_core_web_sm")
normal_sub = ""
with open('script.txt','r') as subs:
    normal_sub = subs.read()
doc = nlp(normal_sub)
new_sub = ""
for token in doc:
    if token.pos_ == "CCONJ":
        new_sub += '. '
    elif token.pos_ == "PUNCT" and token.text != '.':
        new_sub += ''
    else:
        new_sub += " "+token.text; 
doc = nlp(new_sub[1:])
for x in doc.sents:
    print(x.text)

