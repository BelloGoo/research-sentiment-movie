import pyodbc


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
        fw = open('BadSQL.txt', 'RCtag_list+', newline='', encoding='utf-8-sig')
        fw.write(tSQL + "\r\n\r\n")
        fw.close
        return False

def wordBreaker_review():
    MCT = int(OneSQL("SELECT count(*) FROM dbo.review_ WHERE haddone = 0"))
    TOTAL = int(OneSQL("SELECT count(*) FROM dbo.review_"))

    while (MCT > 0):
        print('unprocessed: ', MCT, '/', TOTAL)
        #取得一個沒完成的RID
        newRID = OneSQL("select top 1 rid from dbo.review_ where haddone = 0 order by newid()")
        newRID = str(newRID).rstrip()
        newMID = str(OneSQL(f"SELECT mid FROM dbo.review_ WHERE RID = {newRID}")).rstrip()
        # print('RID: ',newRID)
        print(f"processing RID: {newRID}")
        # get the RCtag with that newRID
        RCtag = str(OneSQL(f"SELECT RCtag FROM dbo.review_ WHERE RID = {newRID}")).strip("[]") #delete the [] at the beginning and end
        # text = "[我|r][愛|v][特|n][拉沃|nz][塔|j][的|uj][舞|n][。|x]".strip("[]")
        # make RCtag into a list, splitting by ']['
        RCtag_list = RCtag.split('][')
        # print(RCtag_list)
        serial_number = 0
        for i in RCtag_list:
            # getting word and tag (elements) in i
            element = i.split('|')
            # print(element)
            word = element[0]
            tag = element[1]
            query = f"INSERT INTO dbo.wb_review (serial_number, rid, mid, word, tag) VALUES ({serial_number}, {newRID},  {newMID}, N'{word}', N'{tag}')"
            # print(query)
            MakeSQL(query)
            serial_number += 1

    # 先進行這次抓了的電影的更新, 把haddone改成1
        uSQL = f"Update dbo.review_ SET haddone = 1 WHERE RID = '{newRID}'; "
        MakeSQL(uSQL)
        MCT = int(OneSQL("SELECT count(*) FROM dbo.review_ WHERE haddone = 0"))

def wordBreaker_st():
    MCT = int(OneSQL("SELECT count(*) FROM dbo.st WHERE haddone = 0"))
    TOTAL = int(OneSQL("SELECT count(*) FROM dbo.st"))

    while (MCT > 0):
        print('unprocessed: ', MCT, '/', TOTAL)
        #取得一個沒完成的RID
        newSN = str(OneSQL("select top 1 SN from dbo.st where haddone = 0 order by newid()")).rstrip()
        newMID = str(OneSQL(f"SELECT mid FROM dbo.st WHERE SN = {newSN}")).rstrip()
        sn_sentencewise = str(OneSQL(f"SELECT serial_number FROM dbo.st WHERE SN = {newSN}")).rstrip()
        # print('SN: ',newSN)
        print(f"processing SN: {newSN}")
        # get the RCtag with that newRID
        tTag = str(OneSQL(f"SELECT tTag FROM dbo.st WHERE SN = {newSN}")).strip("[]").replace(']|[','|') #delete the [] at the beginning and end
        # text = "[我|r][愛|v][特|n][拉沃|nz][塔|j][的|uj][舞|n][。|x]".strip("[]")
        # make RCtag into a list, splitting by ']['
        tTag_list = tTag.split('][')
        # print(RCtag_list)
        sn_wordwise = 0
        check_verify = OneSQL(f"SELECT verify FROM dbo.st WHERE SN = {newSN}")
        if check_verify != 1:
            alter_verify = MakeSQL(f"UPDATE dbo.st SET verify = 1 WHERE SN = {newSN}")
            for i in tTag_list:
                # getting word and tag (elements) in i
                element = i.split('|')
                # print(element)
                try:
                    word = element[0]
                    tag = element[1]
                    query = f"INSERT INTO dbo.wb_st (sn_sentencewise, sn_wordwise, SN_dbost, mid, word, tag) VALUES ({sn_sentencewise}, {sn_wordwise}, {newSN},  {newMID}, N'{word}', N'{tag}')"
                    # print(query)
                    MakeSQL(query)
                    sn_wordwise += 1
                except Exception as e:
                    print(e)
                    failed = MakeSQL(f"Update dbo.st SET haddone = 2 WHERE SN = '{newSN}'; ")
        else:
            print(f"{newSN} is done, getting a new one.")
            continue

    # 先進行這次抓了的電影的更新, 把haddone改成1
        uSQL = f"Update dbo.st SET haddone = 1 WHERE SN = '{newSN}'; "
        MakeSQL(uSQL)
        MCT = int(OneSQL("SELECT count(*) FROM dbo.st WHERE haddone = 0"))


if __name__ == "__main__":
    # wordBreaker_review()
    wordBreaker_st()
