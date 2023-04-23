import spacy
from spacy import displacy 
from nltk.stem.snowball import SnowballStemmer as SBS
import re

nlp = spacy.load("en_core_web_sm")
normal_sub = ""
with open('script.txt','r') as subs:
    normal_sub = subs.read()
doc = nlp(normal_sub)
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)
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
    else:
        new_add = token.lemma_
        new_sub += " "+new_add
doc = nlp(new_sub[1:])
sbs = SBS(language='english')
count = 0
for token in doc:
    if(token.text == 'me'):
        continue
    check_token = nlp(token.lemma_)[0]
    if(check_token.pos_ == "VERB" and check_token.tag_ not in ['VBP','VBZ','VB']):
        new_sub = new_sub.replace(" "+token.text+" ", " "+sbs.stem(check_token.text)+" ")
        print('[',token.text,']',new_sub)
    elif(check_token.text != token.text):
        new_sub = new_sub.replace(token.text,check_token.text)
    
doc = nlp(new_sub[1:])
for x in doc.sents:
    print(x.text)
for token in doc:
    print(token.dep_)
