from opencc import OpenCC
import pyodbc

#=============================================================
Server = 'tcp:140.136.155.47,64873'
DBName = 'MovieDB'
ID = 'sa'
PWD = 'qazwsx'
Driver = '{ODBC Driver 18 for SQL Server}'
#=============================================================

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

cc = OpenCC('s2t')

simpChi = []
chunks_T07 = AllSQL("SELECT SN, text, tTag FROM dbo.m_Scripts WHERE TCID LIKE '%T07%'")
# print(chunks_T07[:2])
for chunk in chunks_T07:
    temp_store = []
    temp_store.append(chunk[0])
    temp_store.append(cc.convert(chunk[1]))
    temp_store.append(cc.convert(chunk[2]))
    simpChi.append(temp_store)    
# print(simpChi)

for line in simpChi:
    SN = line[0]
    text = line[1]
    tTag = line[2]
    # print(SN, text, tTag)
    MakeSQL("UPDATE dbo.m_Scripts SET text = N'{}', tTag = N'{}' WHERE SN = {}".format(text, tTag, SN))
    print("UPDATE dbo.m_Scripts SET text = N'{}', tTag = N'{}' WHERE SN = {}".format(text, tTag, SN))
    print("Done.")
    print("\n")
