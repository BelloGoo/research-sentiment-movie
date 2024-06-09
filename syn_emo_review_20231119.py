from nltk.corpus import wordnet as wn
import pyodbc
from emo_review_phr import review_eng, review_chi, tags, SNs
import json

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
    
def MakeSQL(tSQL):
    try:
        conn = pyodbc.connect('DRIVER={};SERVER={};DATABASE={};ENCRYPT=yes;UID={};PWD={};TrustServerCertificate=yes;'.format(Driver,Server,DBName,ID,PWD))
        cursor = conn.cursor()
        conn.autocommit = True
        cursor.execute(tSQL) 
        conn.close
        return True
    except:
        print("MakeSQL Error:{}".format(tSQL))
        # fw = open('BadSQL.txt', 'RCtag_list+', newline='', encoding='utf-8-sig')
        # fw.write(tSQL + "\r\n\r\n")
        # fw.close
        return False

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

def writeJson(new_data):
    
    file_path = r"C:\Users\85270\OneDrive\桌面\Python\study\TRIAL_syn_emo_review_20240111.json"

    with open(file_path, 'a') as json_file:
        file_data = json.load(json_file)
        file_data.append(new_data)
        json.dump(file_data, json_file, indent=2)
    return " - DATA LOGGED - "


THRESHOLD = 0.857

haddone_count = int(OneSQL("SELECT count(*) FROM dbo.emo_review_eng WHERE haddone = 0"))

while (haddone_count > 0):
    print("unprocessed: ", haddone_count,"/4303")
    pick_one_SN = int(OneSQL("SELECT TOP 1 SN FROM dbo.emo_review_eng WHERE haddone = 0 ORDER BY newid()"))
    MakeSQL(f"UPDATE dbo.emo_review_eng SET haddone = 1 WHERE SN = {pick_one_SN}")
    # w1 = str(OneSQL(f"SELECT eng FROM dbo.emo_review_eng WHERE SN = {pick_one_SN} ORDER BY newid()"))
    num = SNs.index(pick_one_SN)
    w1 = review_eng[num]
    w1_SN = num
    w1_chi = review_chi[num]
    w1_tag = tags[num]
    print("SN-processing: ", pick_one_SN, f"[{w1}]")
    SNs.remove(pick_one_SN)
    review_eng.remove(w1)

    for i in range(0,(len(review_eng)-1)):
        # print(reOrder(syn_list[i]))
        # w1 = reOrder(review_eng[i]) 
        # w1i = reOrder(w1) 
        word_cnt = 0
        for j in range((i+1),(len(review_eng))):
            w2 = review_eng[j]
            w2_SN = SNs[j]
            w2_chi = review_chi[j]
            w2_tag = tags[j]
            # w2i = reOrder(w2) 
            # print(f"[{w1}, {w2}]")
            # print(f"[{i}|{j}]")
            try:
                c1 = wn.synsets(w1)[0]
                c2 = wn.synsets(w2)[0]
                similarity = c1.wup_similarity(c2)
                # print(similarity)
                if similarity >= THRESHOLD:
                    # put two phrases into a same group
                    # MakeSQL(f"INSERT INTO dbo.syn_review (w1_SN, w1_chi, w1_eng, w1_tag, w2_SN, w2_chi, w2_eng, w2_tag, sim) VALUES ({w1_SN},N'{w1_chi}',N'{w1}',N'{w1_tag}',{w2_SN},N'{w2_chi}',N'{w2}',N'{w2_tag}',{similarity})")
                    data = {
                        "w1_SN":w1_SN,
                        "w1_chi":w1_chi,
                        "w1_eng":w1,
                        "w1_tag":w1_tag,
                        "w2_SN":w2_SN,
                        "w2_chi":w2_chi,
                        "w2_eng":w2,
                        "w2_tag":w2_tag,
                        "sim":similarity,
                    }

                    print(writeJson(data))
                    MakeSQL(f"UPDATE dbo.emo_review_eng SET haddone = 1 WHERE SN = {w2_SN}")
                    print("changed haddone")
                    # print("PASS")
                else:
                    # put w2 into an independent group
                    MakeSQL(f"UPDATE dbo.emo_review_eng SET haddone = 1 WHERE SN = {pick_one_SN}")
                    word_cnt += 1
                    if word_cnt == 1000:
                        print("word_cnt = 1000")
                    elif word_cnt == 2000:
                        print("word_cnt = 2000")
                    elif word_cnt == 3000:
                        print("word_cnt = 3000")
                    elif word_cnt == 4000:
                        print("word_cnt = 4000")

                    # print("changed haddone")
                    # print("NOT pass")
            except:
                # print(f"[{w1}|{w2}], without candidate")
                MakeSQL(f"UPDATE dbo.emo_review_eng SET haddone = 2 WHERE SN = {pick_one_SN}")
                word_cnt += 1
                if word_cnt == 1000:
                    print("word_cnt = 1000")
                elif word_cnt == 2000:
                    print("word_cnt = 2000")
                elif word_cnt == 3000:
                    print("word_cnt = 3000")
                elif word_cnt == 4000:
                    print("word_cnt = 4000")
                # print("changed haddone")
                continue

    print(f"finished: {pick_one_SN}|[{w1}]")
    haddone_count = int(OneSQL("SELECT count(*) FROM dbo.emo_review_eng WHERE haddone = 0"))
    print(f"{haddone_count}/4303 remaining")
    

