import pyodbc
import json

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
    
def numSyn(num, i): #num = len(scources[0][4])
    condition = "WHERE "
    for j in range(num):
        conString = f"(word = N'{scources[i][4][j]}' AND tag = N'{scources[i][5][j]}') "
        op = 'OR '
        condition += conString
        if j == (num - 1):
            # notLast = False
            continue
        else:
            condition += op
    return condition


if __name__ == '__main__':

    filepath = r'C:\Users\85270\OneDrive - 輔仁大學\桌面\Python\study\syn_emo_st_20240429.json'
    # Assuming your JSON data is stored in a file named data.json
    with open(filepath, 'r', encoding='utf-8') as f:
        scources = json.load(f)

    for i in range(len(scources[:5])):
        repChi = scources[i][1]
        repTag = scources[i][2]
        synChi = scources[i][4]

        # print(scources[:3])
        MakeSQL(f"UPDATE t_SWords SET word = N'{repChi}', tag = N'{repTag}' {numSyn(len(synChi),i)};")

    print(" --- all FINSIHED !! ---")

#     UPDATE t_Swords
# SET word = '偶', tag = 'r'
# WHERE word = '我', tag = 'r'