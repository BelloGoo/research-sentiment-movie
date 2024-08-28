import pyodbc
from emo_st_phr_selected import st_chi

#=============================================================
Server = 'tcp:140.136.155.47,64873'
DBName = 'MovieDB'
ID = 'sa'
PWD = 'qazwsx'
Driver = '{ODBC Driver 18 for SQL Server}'
#=============================================================

def MakeSQL(tSQL):
    try:
        conn = pyodbc.connect('DRIVER={};SERVER={};DATABASE={};ENCRYPT=yes;UID={};PWD={};TrustServerCertificate=yes;'.format(Driver,Server,DBName,ID,PWD))
        cursor = conn.cursor()
        conn.autocommit = True
        cursor.execute(tSQL) 
        conn.close
        return True
    except:
        #print("MakeSQL Error:{}".format(tSQL))
        fw = open('BadSQL.txt', 'a+', newline='', encoding='utf-8-sig')
        fw.write(tSQL + "\r\n\r\n")
        fw.close
        return False

def AllSQL(tSQL):
    try:
        conn = pyodbc.connect('DRIVER={};SERVER={};DATABASE={};ENCRYPT=yes;UID={};PWD={};TrustServerCertificate=yes;'.format(Driver,Server,DBName,ID,PWD))
        cursor = conn.cursor()
        cursor.execute(tSQL) 
        row = cursor.fetchall() 
        # RV = row[0]
        conn.close
        return row
    except:
        print("OneSQL Error:{}".format(tSQL))
        return False

st_chi_tag = []
words = AllSQL("SELECT word, tag FROM MovieDB.dbo.Xemo_st;")
for word in st_chi:
    for pair in words:
        temp_store = []
        if word == pair[0]:
            temp_store.append(word)
            temp_store.append(pair[1])
            st_chi_tag.append(temp_store)
#             print(temp_store)
print(st_chi_tag)
st_chi_tag_set = set()
for i in st_chi_tag:
    st_chi_tag_set.add(i[0])
# print(st_chi_tag_set, len(st_chi_tag_set))

    

# st_chi_tag_new = []
# for i in st_chi_tag:
#     if i not in st_chi_tag_new:
#         st_chi_tag_new.append(i)
# print(st_chi_tag_new, len(st_chi_tag_new))
# print(len(st_chi))

# st_chi_tag = set(tuple(i[0]) for l in st_chi_tag for i in l)
st_chi = set(st_chi)
st_chi_minus = st_chi - st_chi_tag_set
print(st_chi_minus, len(st_chi_minus))
# print(len(st_chi_tag))

# MakeSQL(f"INSERT INTO MovieDB.dbo.emo_st (word, tag) VALUES (N'{pair[0]}', N'{pair[1]}');")
            
# for i in st_chi:
#     MakeSQL(f"INSERT INTO MovieDB.dbo.emo_st_selected (word) VALUES (N'{i}');")

# print(st_chi, len(st_chi))