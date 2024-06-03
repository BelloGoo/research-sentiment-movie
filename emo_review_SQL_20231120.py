from emo_review_phr import review_chi, review_eng, SNs, tags
import pyodbc
# from emo_review_phr import review_eng, review_chi, tags

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

for i in range(1036,len(SNs)):
    query = f" INSERT INTO emo_review_eng (SN,chi,eng,tag) VALUES ({SNs[i]},N'{review_chi[i]}',N'{review_eng[i]}',N'{tags[i]}')"
    MakeSQL(query)
    print(f"finished: {i}")