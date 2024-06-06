from nltk.corpus import wordnet as wn

with open(r'C:\Users\85270\OneDrive\桌面\Python\study\emo_st.txt', 'r', encoding="utf-8") as file:
    data = [line.strip() for line in file]


def get_synonyms(word):
    synonyms = []
    for syn in wn.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma)
    return synonyms

def reOrder(word):
        word = str(word).lstrip("Lemma('").rstrip("')")
        # print(a)
        b = word.split(".")
        c = str(b[3])+"."+str(b[1])+"."+str("01")
        # print(d)
        return c
