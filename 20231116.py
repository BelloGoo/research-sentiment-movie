# from nltk.corpus import wordnet as wn

# def get_synonyms(word):
#     synonyms = []
#     for syn in wn.synsets(word):
#         for lemma in syn.lemmas():
#             synonyms.append(lemma.name())
#     return synonyms

# print(get_synonyms("shot"))

LS = [1,2,[3,4]]
LS[2].append("a")
LS[2].append("b")
print(LS)