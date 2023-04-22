import spacy

nlp = spacy.load("en_core_web_sm")
normal_sub = ""
with open('script.txt','r') as subs:
    normal_sub = subs.read()
doc = nlp(normal_sub)
new_sub = ""
for token in doc:
    if token.pos_ == "CONJ":
        new_sub += '. '
    elif token.pos_ == "PUNCT" and token.text != '.':
        new_sub += ''
    elif token.pos_ == "SYM" or token.pos_ == "X" or token.pos_ == "DET" or token.pos_ == "CCONJ":
        new_sub += ''
    elif token.text == 'I':
        new_sub += ' me'
    elif token.text == "'d":
        new_sub += ' would'
    elif token.text == "'re":
        new_sub += ' are'
    elif token.text == "'s":
        new_sub += ' is'
    else:
        new_sub += " "+token.text; 
doc = nlp(new_sub[1:])
for x in doc.sents:
    print(x.text)

