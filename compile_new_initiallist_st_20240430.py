from emo_st_phr import st_eng, st_chi, tags, SNs
import json
import pyodbc

#=============================================================
Server = 'tcp:140.136.155.47,64873'
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


def writeJson(new_entry):
    # New data entry

    # Specify the file path
    file_path = r"C:\Users\user\Desktop\python\syn_emo_st__initiallist_20240429.json"

    # Write the updated data to the JSON file with indentation
    with open(file_path, 'w') as json_file:
        json.dump(new_entry, json_file, indent=2)
    return " - DATA LOGGED - "


totalDataEntry = len(SNs)
LS = []
for i in range(totalDataEntry):
    ls = []
    ls.append(st_eng[i])
    ls.append(st_chi[i])
    ls.append(tags[i])
    ls.append(OneSQL(f"SELECT sum(word_count) FROM dbo.Xemo_st WHERE word = N'{st_chi[i]}'"))
    als = []
    als.append(st_chi[i])
    ls.append(als)
    tagls = []
    tagls.append(tags[i])
    ls.append(tagls)
    LS.append(ls)

print("  --  finished compiling the initial list  --")
print(writeJson(LS))
