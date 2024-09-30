from PIL import Image
import pyodbc
import cv2
import numpy as np

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

    # convert the color to HSV
    hsvGreen = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)

    # here insert the bgr values which you want to convert to hsv
    # bgr = np.uint8([[[106,76,89]]])
    hsv = cv2.cvtColor(green, cv2.COLOR_RGB2HSV)
    # print("BGR Value:", bgr)
    h = hsv[0][0][0]
    s = hsv[0][0][1]
    v = hsv[0][0][2]
    
    return [h, s, v]


print(get_avg_RGB(r'C:\Users\85270\OneDrive - 輔仁大學\桌面\Python\study\vidFrames\T01f150.jpg'))


    # MakeSQL(f"INSERT INTO MovieDB.dbo.ImgFeat (TID, ImgID, avR, avG, avB, avH, avS, avV) VALUES ('{TID}', '{ImgID}', '{}', '{}', '{}')"
