
from PIL import Image
import pyodbc
import cv2
import numpy as np
# from emo_st_phr_selected import st_chi

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

def get_dom_RGB(path, palette_size=16):
    # Resize image to speed up processing
    img = Image.open(path)
    img = img.copy()
    img.thumbnail((100, 100))

    # Reduce colors (uses k-means internally)
    paletted = img.convert('P', palette=Image.ADAPTIVE, colors=palette_size)

    # Find the color that occurs most often
    palette = paletted.getpalette()
    color_counts = sorted(paletted.getcolors(), reverse=True)
    palette_index = color_counts[0][1]
    dom_RGB = palette[palette_index*3:palette_index*3+3]

    return dom_RGB

def get_avg_RGB(path):
    img = Image.open(path)
    # width, height = img.size
    pixel_values = list(img.getdata())
    for i in pixel_values:
        R = []
        G = []
        B = []
        r = i[0]**2
        g = i[1]**2
        b = i[2]**2
        R.append(r)
        G.append(g)
        B.append(b)
        aR = int((sum(R)/len(R))**0.5)
        aG = int((sum(G)/len(G))**0.5)
        aB = int((sum(B)/len(B))**0.5)
    return [aR, aG, aB]  

def rgb2hsv(rgb: list):
    green = np.uint8([[rgb]])

    hsv = cv2.cvtColor(green, cv2.COLOR_RGB2HSV)
    # print("BGR Value:", bgr)
    h = hsv[0][0][0]
    s = hsv[0][0][1]
    v = hsv[0][0][2]
    
    return [h, s, v]

def get_TID_TIME():
    # list of all TID
    TID = []
    tid = AllSQL("SELECT TID FROM MovieTag.dbo.TagCase")
    for i in tid:
        for j in i:
            TID.append(j)

    # list of all TIME = [[StartTime, EndTime],[StartTime, EndTime]]
    TIME = []
    temporary = []
    time = AllSQL("SELECT StartTime, EndTime FROM MovieTag.dbo.TagCase")
    for i in time:
        for j in i:
            time = str(j).strip()
            temporary.append(float(time))
        TIME.append(temporary)
        temporary = []

    # TID w/ TIME
    TID_TIME = []
    for i in range(len(TID)):
        TID_TIME.append([TID[i], TIME[i]])

    return TID_TIME

def pathPrefix(tid):
    if "T01" in tid:
        return "T01f"
    elif "T02" in tid:
        return "T02f"
    elif "T03" in tid:
        return "T03f"
    elif "T04" in tid:
        return "T04f"
    elif "T05" in tid:
        return "T05f"
    elif "T06" in tid:
        return "T06f"
    elif "T07" in tid:
        return "T07f"

def find_in_list_of_list(mylist, char):
    for sub_list in mylist:
        if char in sub_list:
            return (mylist.index(sub_list), sub_list.index(char))
    raise ValueError("'{char}' is not in list".format(char = char))


IMG_PATH = r'C:\Users\user\OneDrive - 輔仁大學\桌面\Python\study\vidFrames'
EXTENSION = '.jpg'

TID_TIME = get_TID_TIME()
for i in range(262, 357+1):
    TID = TID_TIME[i][0]
    ST = TID_TIME[i][1][0]
    ET = TID_TIME[i][1][1]-1
    prefix = pathPrefix(TID)
    print(f"TID: {TID}, i index: {find_in_list_of_list(TID_TIME, TID)}")



    for j in range(int(ST), int(ET), 1):
        if j == 0:
            continue
        else:
            try: 
                ImgID = prefix + str(j)
                path = IMG_PATH + '\\' + ImgID + EXTENSION
                dom_RGB = get_dom_RGB(path)
                dom_HSV = rgb2hsv(dom_RGB)
                avg_RGB = get_avg_RGB(path)
                avg_HSV = rgb2hsv(avg_RGB)
                # print("dom_RGB: ",dom_RGB)
                # print("dom_HSV: ",dom_HSV)
                # print("avg_RGB: ",avg_RGB)
                # print("avg_HSV: ",avg_HSV)
                intoDB = MakeSQL(f"INSERT INTO MovieDB.dbo.ImgFeat (TID, ImgID, doR, doG, doB, avR, avG, avB, doH, doS, doV, avH, avS, avV) VALUES (N'{TID}', N'{ImgID}', '{dom_RGB[0]}', '{dom_RGB[1]}', '{dom_RGB[2]}', '{avg_RGB[0]}', '{avg_RGB[1]}', '{avg_RGB[2]}', '{dom_HSV[0]}', '{dom_HSV[1]}', '{dom_HSV[2]}', '{avg_HSV[0]}', '{avg_HSV[1]}', '{avg_HSV[2]}')")
                # p_ImgID = 'T04f'+ str(j)
                # intoDB = MakeSQL(f"UPDATE MovieDB.dbo.ImgFeat SET  
                #                  (doR = '{dom_RGB[0]}'), (doG = '{dom_RGB[1]}'), doB = ('{dom_RGB[2]}'),
                #                  (avR = '{avg_RGB[0]}'), (avG = '{avg_RGB[1]}'), avB = ('{avg_RGB[2]}'), 
                #                  (doH = '{dom_HSV[0]}'), (doS = '{dom_HSV[1]}'), doV = ('{dom_HSV[2]}'), 
                #                  (avH = '{avg_HSV[0]}'), (avS = '{avg_HSV[1]}'), avV = ('{avg_HSV[2]}')
                #                  WHERE  (TID = N'{TID}'), AND (ImgID = N'{p_ImgID}')")
            except FileNotFoundError as e:
                print(f"{e}: {ImgID}")
                continue
