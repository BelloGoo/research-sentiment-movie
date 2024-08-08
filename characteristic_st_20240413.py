import pyodbc
from emo_st_phr_selected import st_chi
import pysrt
from math import floor
import csv
from opencc import OpenCC


#=============================================================
Server = 'tcp:140.136.155.47,64873'
DBName = 'MovieTag'
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

def timeformat(seconds):
    seconds = seconds % (24 * 3600)
    hour = floor(seconds // 3600)
    seconds %= 3600
    minutes = floor(seconds // 60)
    seconds = floor(seconds % 60)
    return hour, minutes, seconds #"%d:%02d:%02d" % (hour, minutes, seconds)

# use TID time to extract dialogues from subtitle files
def extract_dialogues_from_srt(file_path, start_time, end_time):
    subs = pysrt.open(file_path, encoding='utf-8')
    extracted_dialogues = []
    for sub in subs:
        if sub.start >= start_time and sub.end <= end_time:
            sceneDialogues = sub.text
            extracted_dialogues.append(cc.convert(sceneDialogues))
    return extracted_dialogues

def filePathIndicator(tid):
    if "T01" in tid:
        return 0
    elif "T02" in tid:
        return 1
    elif "T03" in tid:
        return 2
    elif "T04" in tid:
        return 3
    elif "T05" in tid:
        return 4
    elif "T06" in tid:
        return 5
    elif "T07" in tid:
        return 6


if __name__ == "__main__":

    # getting subtitle files
    MID = [
        26648249, #moonlight
        26752852, #the shape of water
        27060077, #green book
        27010768, #parasite
        30458949, #nomadland
        35048413, #CODA
        30314848, #evrything everywhere all at once
    ]
    filepath = [
        r"C:\Users\85270\OneDrive - 輔仁大學\文件\subjective well-being\raw_st\26648249\月光男孩.Moonlight.2016.2160p.UHD.BluRay.X265-IAMABLE.srt",
        r"C:\Users\85270\OneDrive - 輔仁大學\文件\subjective well-being\raw_st\26752852\The Shape of Water\26752852.srt",
        r"C:\Users\85270\OneDrive - 輔仁大學\文件\subjective well-being\raw_st\27060077\绿皮书.Green.Book.2018.2160p.UHD.BluRay.X265-IAMABLE.srt",
        r"C:\Users\85270\OneDrive - 輔仁大學\文件\subjective well-being\raw_st\27010768\Parasite.2019.KOREAN.2160p.CHT.srt",
        r"C:\Users\85270\OneDrive - 輔仁大學\文件\subjective well-being\raw_st\30458949\Nomadland (Chinese Traditional).srt",
        r"C:\Users\85270\OneDrive - 輔仁大學\文件\subjective well-being\raw_st\35048413\35_Chinese.srt",
        r"C:\Users\85270\OneDrive - 輔仁大學\文件\subjective well-being\raw_st\30314848\Everything.Everywhere.All.at.Once.2022.1080p.BluRay.srt",
    ]

    cc = OpenCC('s2t')

    # list of all TID
    TID = []
    tid = AllSQL("SELECT TID FROM dbo.TagCase")
    for i in tid:
        for j in i:
            TID.append(j)

    # list of all TIME = [[StartTime, EndTime],[StartTime, EndTime]]
    TIME = []
    temporary = []
    time = AllSQL("SELECT StartTime, EndTime FROM dbo.TagCase")
    for i in time:
        for j in i:
            time = str(j).strip()
            time = timeformat(float(time))
            temporary.append(time)
        TIME.append(temporary)
        temporary = []

    # TID w/ TIME
    TID_TIME = []
    for i in range(len(TID)):
        TID_TIME.append([TID[i], TIME[i]])
    # print(TID_TIME)

    # get the extracted dialogues from the subtitle file
    TID_charV = []
    for scene in TID_TIME:
        tid = scene[0]
        file_path = filepath[filePathIndicator(tid)]
        hours, minutes, seconds = TID_TIME[TID.index(tid)][1][0]
        start_time = pysrt.SubRipTime(hours, minutes, seconds) #0,0,0 #"%s, %s, %s" % TID_TIME[T02_start][1][0]
        hours, minutes, seconds = TID_TIME[TID.index(tid)][1][1]
        end_time = pysrt.SubRipTime(hours, minutes, seconds) #0,3,0 #"%s, %s, %s" % TID_TIME[T02_start][1][1]
        extracted_dialogues = extract_dialogues_from_srt(file_path, start_time, end_time)

        # compile the characteristic values vector
        charV = []
        for word in st_chi:
            word = cc.convert(word)
            if word in extracted_dialogues:
                charV.append(1)
            else:
                charV.append(0)
        TID_charV.append([tid, charV])
    
    # write the TID_charV to a csv file
    filename = "TID_charV_20240425.csv"
    with open(fr'C:\Users\85270\OneDrive - 輔仁大學\桌面\Python\study\{filename}', 'w', encoding='utf-8', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for value in TID_charV:
            csvwriter.writerow(value)
        print(f"{filename} has been created successfully!")

