import spacy
from spacy import displacy 
from nltk.stem.snowball import SnowballStemmer as SBS
import re

def conv_txt(fname):
    nlp = spacy.load("en_core_web_sm")
    normal_sub = ""
    with open(fname,'r') as subs:
        normal_sub = subs.read()
    doc = nlp(normal_sub)
    # for token in doc:
    #     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
    #             token.shape_, token.is_alpha, token.is_stop)
    new_sub = ""
    for token in doc:
        if token.pos_ == "CONJ":
            new_sub += '. '
        elif token.pos_ == "PUNCT" and token.text != '.':
            new_sub += ''
        elif token.pos_ == "SYM" or token.pos_ == "X" or token.pos_ == "DET" or token.pos_ == "CCONJ" or token.tag_ == "IN":
            new_sub += ''
        elif token.text == 'I':
            new_sub += ' me'
        else:
            new_add = token.lemma_
            new_sub += " "+new_add
    doc = nlp(new_sub[1:])
    sbs = SBS(language='english')
    for token in doc:
        if(token.text == 'me'):
            continue
        check_token = nlp(token.lemma_)[0]
        if(check_token.pos_ == "VERB" and check_token.tag_ not in ['VBP','VBZ','VB']):
            new_sub = new_sub.replace(" "+token.text+" ", " "+sbs.stem(check_token.text)+" ")
        elif(check_token.text != token.text):
            new_sub = new_sub.replace(token.text,check_token.text)
        
    doc = nlp(new_sub[1:])
    new_sent = []
    new_sent_dep = []
    new_sent_pos = []
    for x in doc.sents:
        new_sent.append(x.text)
        cur_sent_dep = []
        cur_sent_pos = []
        for token in x:
            cur_sent_dep.append(token.dep_)
            cur_sent_pos.append(token.pos_)
        new_sent_dep.append(cur_sent_dep)
        new_sent_pos.append(cur_sent_pos)

    n_sent = len(new_sent)
    for i in range(n_sent):
        cur_sent = nlp(new_sent[i])
        n_cur_sent = len(new_sent[i])
        cur_mod_sent = []
        cur_sent_dep = new_sent_dep[i]
        # for token in cur_sent:
        #     print(token.text, token.lemma_, token.pos_, token.dep_)
        for token in cur_sent:
            cur_mod_sent.append(token.text)
        temp_i = 0
        after = 1
        for token in cur_sent:
            next_sub = ''
            if(token.pos_ in ["VERB","ADV"] and token.dep_[-4:] != 'subj'):
                # print(1)
                for x in new_sent_dep[i][temp_i:]:
                    if x[-3:] == "obj":
                        next_sub = x
                        break
                try:
                    next_i = new_sent_dep[i][temp_i:].index(next_sub)+temp_i+after
                except ValueError: 
                    next_i = -1
                el = cur_mod_sent[temp_i]
                # print(el)
                del cur_mod_sent[temp_i]
                cur_mod_sent.insert(next_i,el)
            elif(token.tag_ == 'TO' and token.dep_[-4:] != 'subj'):
                for x in new_sent_dep[i][temp_i:temp_i+4]:
                    if x[-4:] == "subj":
                        next_sub = x
                        break
                try:
                    next_i = new_sent_dep[i][temp_i:].index(next_sub)+1
                    el = cur_mod_sent[temp_i]
                    # print(el)
                    del cur_mod_sent[temp_i]
                    cur_mod_sent.insert(next_i,el)
                except ValueError: 
                    pass
            temp_i += 1
        new_sent[i] = " ".join(cur_mod_sent)
    doc = nlp("".join(new_sent))
    words = []
    for token in doc.sents:
        words.append(token.text)

if __name__ == "__main__":
    conv_txt("script.txt")
