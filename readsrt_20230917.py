import re
import os
import jieba.posseg as pseg
import pyodbc


#=============================================================
Server = 'tcp:140.136.155.46,1433'
DBName = 'movieDB'
ID = 'sa'
PWD = 'qazwsx'
Driver = '{ODBC Driver 18 for SQL Server}'
#=============================================================
pseg_ = pseg

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
        #print("MakeSQL Error:{}".format(tSQL))
        fw = open('BadSQL.txt', 'a+', newline='', encoding='utf-8-sig')
        fw.write(tSQL + "\r\n\r\n")
        fw.close
        return False

def get_filenames():
    # getting a list of filenames in subtitle
    fnames = os.listdir('c:\\subtitle')
    filenames = []
    for fname in fnames:
        s1=re.sub("[^0-9]","",fname)
        filenames.append(s1)
    return filenames

def extract_srt_info(file_path):
    try:
# for filename in os.listdir(src_dir):
#     if filename.endswith('.srt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            srt_data = file.read()

            # Split subtitles based on empty lines
            subtitles = srt_data.strip().split('\n\n')

            # subtitle_list = []
            starttime = ''
            endtime = ''
            text = ''
            tTag = ''

            serial_number = 0
            for subtitle in subtitles:
                lines = subtitle.split('\n')
                if len(lines) >= 2:
                    # Extract timestamp
                    timestamp_match = re.match(r'(\d+:\d+:\d+,\d+) --> (\d+:\d+:\d+,\d+)', lines[1])
                    if timestamp_match:
                        start_time, end_time = timestamp_match.groups()
                    else:
                        start_time, end_time = '', ''

                    # Extract subtitle text
                    subtitle_text = ' '.join(lines[2:])

                    # Append data to the list
                    # subtitle_list.append({
                    #     'start_time': start_time,
                    #     'end_time': end_time,
                    #     'text': subtitle_text
                    # })
                    starttime = start_time
                    endtime = end_time
                    text = subtitle_text
                    tTag = ''
                    tseg_list = pseg_.cut(subtitle_text)
                    for word, flag in tseg_list:
                        tTag += f"[{word}]|[{flag}]"
                    # print(f'tseg_list: {tseg_list}')
                    query = f"INSERT INTO st (serial_number, MID, start_time, end_time, text, tTag) VALUES (N'{serial_number}', N'{newMID}',  N'{starttime}', N'{endtime}', N'{text}', N'{tTag}')"
                    # print(query)
                    MakeSQL(query)
                    serial_number += 1
        # return subtitle_list

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        # return None

# Example usage
if __name__ == "__main__":
    count = 0
    MCT = int(OneSQL("SELECT count(*) FROM dbo.st_MID WHERE haddone = 0"))
    while (MCT > 0):
        print('unprocessed: ', MCT, '/349')
        #取得一個沒完成的MID
        newMID = OneSQL("select top 1 mid from dbo.st_MID where haddone = 0 order by newid()")
        newMID = str(newMID).rstrip()
        print('MID: ',newMID)

        srt_file_path = f"C:\\subtitle\\utf8\\{newMID}.srt"  # Replace with the path to your .srt file
        print(f"processing: {newMID}")
        subtitles = extract_srt_info(srt_file_path)
    # 先進行這次抓了的電影的更新, 把haddone改成1
        uSQL = f"Update dbo.st_MID SET haddone = 1 WHERE MID = '{newMID}'; "
        MakeSQL(uSQL)
        MCT = int(OneSQL("SELECT count(*) FROM dbo.st_MID WHERE haddone = 0"))

