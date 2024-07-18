import pyodbc
from nltk.corpus import wordnet as wn
from emo_review_phr import review_eng, review_chi, tags, SNs
import json
from copy import deepcopy

#=============================================================
Server = 'tcp:140.136.155.46,1433'
DBName = 'movieDB'
ID = 'sa'
PWD = 'qazwsx'
Driver = '{ODBC Driver 18 for SQL Server}'
#=============================================================

def OneSQL(tSQL):
    try:
        conn = pyodbc.connect('DRIVER={};SERVER={};DATABASE={};ENCRYPT=yes;UID={};PWD={};TrustServerCertificate=yes;'.format(Driver,Server,DBName,ID,PWD))
        cursor = conn.cursor()
        cursor.execute(tSQL) 
        row = cursor.fetchone() 
        RV = row[0]
        conn.close
        return RV
    except:
        print("OneSQL Error:{}".format(tSQL))
        return False
    
def similarity(w1, w2):
    try:
        c1 = wn.synsets(w1)[0]
        c2 = wn.synsets(w2)[0]
        return c1.wup_similarity(c2)
    except:
        return 0
    
def writeJson(new_entry):
    # New data entry

    # Specify the file path
    file_path = r"C:\Users\85270\OneDrive\桌面\Python\study\syn_emo_review_20240306.json"

    # Write the updated data to the JSON file with indentation
    with open(file_path, 'w') as json_file:
        json.dump(new_entry, json_file, indent=2)

    return " - DATA LOGGED - "


# totalDataEntry = len(SNs)
# LS = []
# for i in range(totalDataEntry):
#     ls = []
#     ls.append(review_eng[i])
#     ls.append(review_chi[i])
#     ls.append(OneSQL(f"SELECT word_count FROM dbo.emo_review WHERE SN = {SNs[i]}"))
#     als = []
#     als.append(review_chi[i])
#     ls.append(als)
#     LS.append(ls)

# print("  --  finished compiling the initial list  --")
# print(writeJson(LS))

# Specify the file path
file_path = r'study\syn_emo_review_initiallist_20240304.json'

# Read data from the JSON file
try:
    with open(file_path, 'r') as json_file:
        LS = json.load(json_file)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")

# LS = [['we','我們', 50, ['我們']],['you','你', 20, ['你']],['sun','太陽', 30, ['太陽']],['sun','日', 30, ['日']]]
# saved_LS = deepcopy(LS)
# for i in range(0,(len(saved_LS)-1)):
#     for j in range((i+1), (len(saved_LS))):
#         X = saved_LS[i][0] #0 represents the english word
#         Y = saved_LS[j][0]

#         if (similarity(X,Y)>0.857):
#             LS[i][2] = LS[i][2] + LS[j][2] #2 represents the word count
#             als = LS[i][3] + LS[j][3] #3 represents the grouped chinese words 
#             LS[i][3] = als
#             LS.pop(j)

#         else:
#             continue

# print(LS)
i = 0
while i < (len(LS)-1):
    j = i + 1
    while j < len(LS):
        X = LS[i][0]  # 0 represents the english word
        Y = LS[j][0]

        if similarity(X, Y) > 0.857:
            LS[i][2] += LS[j][2]  # 2 represents the word count
            als = LS[i][3] + LS[j][3]  # 3 represents the grouped Chinese words
            LS[i][3] = als
            LS.pop(j)
            # Decrement j as the length of LS has been reduced by popping an element
            j -= 1
        j += 1

    i += 1
print(writeJson(LS))


# A 50 {A,C}
# B 30 {B}
# D 10 {D}

# >>

# A 50 {A,C}
# B 30 {B}


# LS = []
# for i in range(dCT):
#     ls = []
#     ls.append(strX)
#     ls.append(iCT)
#     als = []
#     als.append(strX)
#     ls.append(als)
#     LS.append(ls)

# i, j

# X = LS[i][0] 
# Y = LS[j][0]
# if (Compare(X,Y)>0.8):
#     LS[i][1] = LS[i][1] + LS[j][1]
#     als = LS[i][2] + LS[j][2]
#     LS[i][2] = als
#     LS.pop(j)