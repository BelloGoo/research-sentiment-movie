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
                    tseg_list = pseg_.cut(subtitle_text)
                    for word, flag in tseg_list:
                        tTag += f"[{word}]|[{flag}]"
                    print('tTag finished')
                    query = f"INSERT INTO st (serial_number, MID, start_time, end_time, text, tTag) VALUES (N'{serial_number}', N'{filename}',  {starttime}, {endtime}, N'{text}', N'{tTag}')"
                    # print(query)
                    MakeSQL(query)
                    serial_number += 1


        # return subtitle_list

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    count = 0
    for filename in get_filenames():
        srt_file_path = f"C:\\subtitle\\{filename}.srt"  # Replace with the path to your .srt file
        print(f"processing: {filename}")
        subtitles = extract_srt_info(srt_file_path)
        count += 1
        print(f"unprocessed: {len(get_filenames())-count}/{len(get_filenames())}","\n=====")

        # if subtitles:
        #     for index, subtitle in enumerate(subtitles, start=1):
        #         print(f"Subtitle {index}:")
        #         print(f"Start Time: {subtitle['start_time']}")
        #         print(f"End Time: {subtitle['end_time']}")
        #         print(f"Subtitle Text: {subtitle['text']}\n")
