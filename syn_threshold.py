import nltk
from nltk.corpus import wordnet as wn


# with open(r'C:\Users\85270\OneDrive\桌面\Python\study\emo_review.txt', 'r', encoding="utf-8") as file:
#     data = [line.strip() for line in file]

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


# grouped_data = {}

# for text in data:
#     tokens = text.split()  # Tokenize the text into words
#     for token in tokens:
#         synonyms = get_synonyms(token)
#         for synonym in synonyms:
#             if synonym in grouped_data:
#                 grouped_data[synonym].append(text)
#             else:
#                 grouped_data[synonym] = [text]

# for synonym, texts in grouped_data.items():
#     print(f"Synonym: {synonym}")
#     for text in texts:
#         print(f"- {text}")


pool = [
    
]


similarity_list = []
for w in pool:
    # print(get_synonyms(w))
    syn_list = get_synonyms(w) #[reOrder(r) for r in ['still', 'hush', 'stillness', 'still', 'still', 'distillery', 'still', 'calm', 'calm_down', 'quiet']] 
    # print(len(syn_list))
    for i in range(0,(len(syn_list)-1)):
        # print(reOrder(syn_list[i]))
        w1 = reOrder(syn_list[i]) 
        for j in range((i+1),(len(syn_list))):
            w2 = reOrder(syn_list[j]) 
            print(f"[{w}, {w1}, {w2}]")
            print(f"[{w}|{i}|{j}]")
            try:
                c1 = wn.synset(w1)
                c2 = wn.synset(w2)
            except Exception as e:
                print(f"skipping {w2}, Exception: {e}")
            similarity = c1.wup_similarity(c2)
            print(similarity)
            similarity_list.append(similarity)






