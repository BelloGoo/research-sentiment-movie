import os, re
import pyodbc
import chardet


# # getting a list of filenames in subtitle
# def get_filenames():
#     # getting a list of filenames in subtitle
#     fnames = os.listdir('c:\\subtitle')
#     filenames = []
#     for fname in fnames:
#         s1=re.sub("[^0-9]","",fname)
#         filenames.append(s1)
#     return filenames


# #=============================================================
# Server = 'tcp:140.136.155.46,1433'
# DBName = 'movieDB'
# ID = 'sa'
# PWD = 'qazwsx'
# Driver = '{ODBC Driver 18 for SQL Server}'
# #=============================================================

# def OneSQL(tSQL):
#     try:
#         conn = pyodbc.connect('DRIVER={};SERVER={};DATABASE={};ENCRYPT=yes;UID={};PWD={};TrustServerCertificate=yes;'.format(Driver,Server,DBName,ID,PWD))
#         cursor = conn.cursor()
#         cursor.execute(tSQL) 
#         row = cursor.fetchone() 
#         RV = row[0]
#         conn.close
#         return RV
#     except:
#         print("OneSQL Error:{}".format(tSQL))
#         return False
    
# def MakeSQL(tSQL):
#     try:
#         conn = pyodbc.connect('DRIVER={};SERVER={};DATABASE={};ENCRYPT=yes;UID={};PWD={};TrustServerCertificate=yes;'.format(Driver,Server,DBName,ID,PWD))
#         cursor = conn.cursor()
#         conn.autocommit = True
#         cursor.execute(tSQL) 
#         conn.close
#         return True
#     except:
#         #print("MakeSQL Error:{}".format(tSQL))
#         fw = open('BadSQL.txt', 'a+', newline='', encoding='utf-8-sig')
#         fw.write(tSQL + "\r\n\r\n")
#         fw.close
#         return False

# # input all st MID in database
# for MID in get_filenames():
#     query = f"INSERT INTO st_MID (MID, haddone) VALUES (N'{MID}', {0})"
#     # print(query)
#     MakeSQL(query)


# # check encoding
# def try_utf8(data):
#     "Returns a Unicode object on success, or None on failure"
#     try:
#        return data.decode('utf-8')
#     except UnicodeDecodeError:
#        return None
    
# def detect_encoding(file_path):
#     try:
#         with open(file_path, 'rb') as file:
#             rawdata = file.read()
#         result = chardet.detect(rawdata)
#         encoding = result['encoding']
#         confidence = result['confidence']
#         if encoding == 'UTF-16':
#             utf16.append(MID)
#         elif encoding == "Big5":
#             big5.append(MID)
#         else:
#             other[MID] = encoding
#         print(f"UTF-16: {utf16}",f"(count: {len(utf16)})")
#         print(f"Big5: {big5}",f"(count: {len(big5)})")
#         print(f"other encoding type: {other}",f"(count: {len(other)})")
#         # return encoding, confidence

#     except Exception as e:
#         print(f"An error occurred: {str(e)}")
#         return None, None


# count = 0
# not8 = [] 
# utf16 = []
# big5 = []
# other = {}   
# for filename in get_filenames():
#     file_path = f"C:\\subtitle\\{filename}.srt"
#     with open(file_path, 'rb') as file:
#         data = file.read()
#         udata = try_utf8(data)
#         if udata is None:
#             # Not UTF-8.  Do something else
#             # print(f'{file_path} not utf-8')
#             not8.append(filename)
#             count += 1
# print(f"total not utf-8: {count}")

# for MID in not8:
#     file_path = f"C:\\subtitle\\{MID}.srt"
#     type = detect_encoding(file_path)
    # print(type)

        # else:
        #     # Handle unicode data
        #     pass


# # Example usage
# if __name__ == "__main__":
#     for filename in get_filenames():
#         file_path = f"{filename}.srt"  # Replace with the path to your text file
#         encoding, confidence = detect_encoding(file_path)

#         if encoding:
#             print(f"Detected Encoding: {encoding} with confidence {confidence * 100:.2f}%")
#         else:
#             print("Encoding detection failed.")

#=================================================================

# # encoding converting
# BIG5 = ['1292230', '1292268', '1292550', '1292656', '1292660', '1292765', '1292781', '1292849', '1292941', '1293004', '1293050', '1293172', '1293229', '1293755', '1293818', '1293838', '1294240', '1294503', '1294620', '1294925', '1294941', '1295124', '1295688', '1296223', '1296260', '1296467', '1296827', '1297531', '1297628', '1297991', '1297995', '1298056', '1299235', '1299879', '1300220', '1300374', '1300685', '1301061', '1301168', '1301890', '1306029', '1306604', '1307535', '1307748', '1307749', '1309070', '1309085', '1388216', '1389949', '1418834', '1422957', '1431617', '1437774', '1483944', '1485260', '1498818', '1777612', '1857099', '1858711', '1866264', '1905790', '1917171', '1945780', '1950148', '19973780', '2028677', '2062678', '21263666', '2129039', '2132495', '2209573', '2209575', '2336737', '26303622', '26389148', '26628282', '27010768', '3006772', '3011072', '3011093', '3023164', '30458949', '3071509', '3077791', '3089638', '3094909', '3135483', '3205624', '3552028', '3569969', '3793783', '4023638', '4164444', '6860160', '6873657', '7015714']
# count = 0
# total = 97
# exception = []
# for i in BIG5:
#     try:
#         inputfile = f"C:\\subtitle\\{i}.srt"
#         outputfile = f"C:\\subtitle\\utf8\\{i}.srt"
#         encodingtype = 'big5'


#         with open(inputfile,'r', encoding = f'{encodingtype}') as file:
#             originalcontent = file.read()

#         with open(outputfile,'w', encoding = 'utf8') as newfile:
#             newfile.write(originalcontent)
#         count += 1
#         print(f'remaining: {total-count}/{total}')
#     except:
#         exception.append(i)
#         print(f'fail to convert')
# print(f'num of exception: {len(exception)}, ',f'exception: {exception}' )
# # ===================================================================

# # list all filenames
# filenames = os.listdir(r'C:\subtitle')
# print(filenames)

# =======================================================================
# utf8 = []
allfilenames = ['10463953.srt', '10741220.srt', '11525673.srt', '1291548.srt', '1291552.srt', '1291571.srt', '1291572.srt', '1291832.srt', '1291833.srt', '1291834.srt', '1291835.srt', '1291840.srt', '1291841.srt', '1291853.srt', '1291870.srt', '1291872.srt', '1292052.srt', '1292062.srt', '1292063.srt', '1292067.srt', '1292222.srt', '1292224.srt', '1292225.srt', '1292230.srt', '1292233.srt', '1292238.srt', '1292260.srt', '1292268.srt', '1292269.srt', '1292271.srt', '1292348.srt', '1292349.srt', '1292403.srt', '1292472.srt', '1292541.srt', '1292550.srt', '1292563.srt', '1292566.srt', '1292591.srt', '1292656.srt', '1292658.srt', '1292660.srt', '1292667.srt', '1292720.srt', '1292722.srt', '1292759.srt', '1292764.srt', '1292765.srt', '1292766.srt', '1292781.srt', '1292849.srt', '1292862.srt', '1292869.srt', '1292874.srt', '1292891.srt', '1292927.srt', '1292932.srt', '1292941.srt', '1293004.srt', '1293037.srt', '1293050.srt', '1293094.srt', '1293104.srt', '1293155.srt', '1293158.srt', '1293172.srt', '1293194.srt', '1293200.srt', '1293203.srt', '1293204.srt', '1293219.srt', '1293228.srt', '1293229.srt', '1293307.srt', '1293341.srt', '1293348.srt', '1293371.srt', '1293374.srt', '1293396.srt', '1293399.srt', '1293413.srt', '1293505.srt', '1293530.srt', '1293544.srt', '1293561.srt', '1293566.srt', '1293626.srt', '1293688.srt', '1293706.srt', '1293715.srt', '1293736.srt', '1293755.srt', '1293764.srt', '1293767.srt', '1293785.srt', '1293796.srt', '1293804.srt', '1293809.srt', '1293818.srt', '1293838.srt', '1293889.srt', '1293917.srt', '1293926.srt', '1294000.srt', '1294070.srt', '1294087.srt', '1294240.srt', '1294245.srt', '1294408.srt', '1294477.srt', '1294503.srt', '1294508.srt', '1294584.srt', '1294587.srt', '1294620.srt', '1294638.srt', '1294639.srt', '1294768.srt', '1294849.srt', '1294925.srt', '1294941.srt', '1294950.srt', '1295124.srt', '1295137.srt', '1295184.srt', '1295260.srt', '1295425.srt', '1295467.srt', '1295480.srt', '1295688.srt', '1295692.srt', '1295713.srt', '1295742.srt', '1295805.srt', '1296147.srt', '1296180.srt', '1296223.srt', '1296260.srt', '1296282.srt', '1296467.srt', '1296617.srt', '1296717.srt', '1296736.srt', '1296805.srt', '1296821.srt', '1296827.srt', '1296908.srt', '1296987.srt', '1297009.srt', '1297205.srt', '1297229.srt', '1297398.srt', '1297531.srt', '1297602.srt', '1297628.srt', '1297630.srt', '1297737.srt', '1297965.srt', '1297991.srt', '1297995.srt', '1298026.srt', '1298056.srt', '1298192.srt', '1298308.srt', '1298468.srt', '1298517.srt', '1298624.srt', '1298812.srt', '1299026.srt', '1299131.srt', '1299193.srt', '1299235.srt', '1299330.srt', '1299879.srt', '1300106.srt', '1300220.srt', '1300365.srt', '1300374.srt', '1300422.srt', '1300487.srt', '1300520.srt', '1300685.srt', '1300725.srt', '1300891.srt', '1301061.srt', '1301168.srt', '1301890.srt', '1304641.srt', '1305666.srt', '1306029.srt', '1306604.srt', '1306860.srt', '1307535.srt', '1307697.srt', '1307748.srt', '1307749.srt', '1308831.srt', '1309016.srt', '1309070.srt', '1309085.srt', '1315316.srt', '1322848.srt', '1388216.srt', '1389949.srt', '1417676.srt', '1418834.srt', '1422957.srt', '1431617.srt', '1437774.srt', '1438652.srt', '1469159.srt', '1483944.srt', '1485260.srt', '1498818.srt', '1652587.srt', '1777612.srt', '1793929.srt', '1857099.srt', '1858711.srt', '1866264.srt', '1889242.srt', '1905790.srt', '1917171.srt', '1929463.srt', '1945780.srt', '1947729.srt', '1950148.srt', '1950330.srt', '1978709.srt', '19973780.srt', '2028645.srt', '2028677.srt', '20438962.srt', '2056093.srt', '2062678.srt', '21263666.srt', '2129039.srt', '21324900.srt', '2132495.srt', '21339682.srt', '2209573.srt', '2209575.srt', '2213597.srt', '2336735.srt', '2336737.srt', '24815950.srt', '25724855.srt', '25773932.srt', '25864085.srt', '25908051.srt', '25934014.srt', '25954475.srt', '25980443.srt', '2609258.srt', '26220650.srt', '26303622.srt', '26305582.srt', '26325320.srt', '26348103.srt', '26389148.srt', '26588314.srt', '26607693.srt', '26611804.srt', '26615208.srt', '26628282.srt', '26648249.srt', '26688480.srt', '26716348.srt', '26752852.srt', '26761416.srt', '26799731.srt', '26809592.srt', '26820621.srt', '26920842.srt', '26990609.srt', '27000981.srt', '27010768.srt', '27060077.srt', '27066152.srt', '27087724.srt', '27119724.srt', '27133913.srt', '27202818.srt', '27605105.srt', '2997076.srt', '3001114.srt', '3006772.srt', '3011072.srt', '3011093.srt', '3013046.srt', '30170546.srt', '3023164.srt', '30252495.srt', '30314848.srt', '3042261.srt', '30450313.srt', '30458949.srt', '30464264.srt', '30481476.srt', '3071509.srt', '3077791.srt', '3078514.srt', '3089638.srt', '3094909.srt', '3135483.srt', '3205624.srt', '33432655.srt', '33437152.srt', '34461705.srt', '34463995.srt', '34884712.srt', '34888057.srt', '34969348.srt', '35048413.srt', '35240917.srt', '35299584.srt', '35390098.srt', '3541415.srt', '35430833.srt', '3552028.srt', '3569969.srt', '3592854.srt', '3610676.srt', '3626372.srt', '3793783.srt', '4023638.srt', '4058933.srt', '4116480.srt', '4164444.srt', '4206436.srt', '4319218.srt', '4798707.srt', '4811774.srt', '5300054.srt', '5327268.srt', '6097775.srt', '6307447.srt', '6390825.srt', '6430835.srt', '6538833.srt', '6538866.srt', '6549903.srt', '6722879.srt', '6860160.srt', '6873657.srt', '6879185.srt', '6893932.srt', '6981153.srt', '7015714.srt']
# for i in allfilenames:
#    with open(f"C:\\subtitle\\{i}",'r') as file:
#       if try_utf8(file.read()):
#          utf8.append(i)
# print(f'num of utf8: {len(utf8)}')

# ========================================================================

import shutil
# list = []
# convertlist2set = ['11525673', '1291548', '1291833', '1291835', '1291840', '1292233', '1292260', '1292566', '1292720', '1292722', '1292869', '1292932', '1293037', '1293104', '1293158', '1293200', '1293204', '1293530', '1293561', '1293785', '1294584', '1294587', '1295480', '1295742', '1296717', '1297009', '1297229', '1297630', '1297737', '1297965', '1298192', '1300106', '1306860', '1322848', '1438652', '1793929', '2028645', '21324900', '25724855', '25908051', '25934014', '26325320', '26607693', '26761416', '26920842', '27060077', '3592854', '4116480', '4206436', '4798707', '5327268', '6430835', '6538833', '6549903', '6722879', '6981153','1291832', '1291872', '1292222', '1292230', '1292268', '1292550', '1292656', '1292660', '1292765', '1292781', '1292849', '1292941', '1293004', '1293050', '1293172', '1293229', '1293755', '1293818', '1293838', '1294240', '1294503', '1294620', '1294925', '1294941', '1295124', '1295688', '1296223', '1296260', '1296467', '1296827', '1297531', '1297628', '1297991', '1297995', '1298056', '1299235', '1299879', '1300220', '1300374', '1300685', '1301061', '1301168', '1301890', '1306029', '1306604', '1307535', '1307748', '1307749', '1309070', '1309085', '1388216', '1389949', '1418834', '1422957', '1431617', '1437774', '1483944', '1485260', '1498818', '1777612', '1857099', '1858711', '1866264', '1905790', '1917171', '1945780', '1950148', '19973780', '2028677', '2062678', '21263666', '2129039', '2132495', '2209573', '2209575', '2336737', '26303622', '26389148', '26628282', '27010768', '3006772', '3011072', '3011093', '3023164', '30458949', '3071509', '3077791', '3089638', '3094909', '3135483', '3205624', '3552028', '3569969', '3793783', '4023638', '4164444', '6860160', '6873657', '7015714','1292052', '1293341', '1293715', '1308831']
# for i in convertlist2set:
#     i += '.srt'
#     list.append(i)
# new_set = set(list)
# set_allfilenames = set(allfilenames)
# utf8 = set_allfilenames.difference(new_set)
# print(utf8, len(utf8))

utf8 = ['1300487.srt', '1292062.srt', '1292591.srt', '1947729.srt', '1293371.srt', '34969348.srt', '1292067.srt', '25864085.srt', '1293399.srt', '1293396.srt', '26348103.srt', '1294639.srt', '27202818.srt', '1292667.srt', '1292891.srt', '21339682.srt', '1292862.srt', '1294849.srt', '1417676.srt', '3610676.srt', '1293917.srt', '20438962.srt', '26799731.srt', '26611804.srt', '4319218.srt', '10741220.srt', '1291552.srt', '27133913.srt', '1294408.srt', '1299330.srt', '1294950.srt', '35048413.srt', '1293228.srt', '6893932.srt', '1307697.srt', '1294000.srt', '1294638.srt', '1293804.srt', '1295713.srt', '27066152.srt', '27087724.srt', '1297398.srt', '35390098.srt', '6390825.srt', '1296736.srt', '1300891.srt', '30464264.srt', '1298517.srt', '1292658.srt', '1296147.srt', '1299026.srt', '1293796.srt', '25773932.srt', '1293706.srt', '1292348.srt', '10463953.srt', '1291841.srt', '34884712.srt', '1292759.srt', '1309016.srt', '6879185.srt', '1292271.srt', '1294087.srt', '1296805.srt', '1293809.srt', '26615208.srt', '1292874.srt', '3013046.srt', '35299584.srt', '4811774.srt', '1295692.srt', '3541415.srt', '1292238.srt', '1299193.srt', '34461705.srt', '1889242.srt', '26820621.srt', '1300422.srt', '1294768.srt', '30450313.srt', '1298026.srt', '1292764.srt', '1291571.srt', '1294070.srt', '1298308.srt', '2056093.srt', '25954475.srt', '1978709.srt', '1291834.srt', '1293626.srt', '1293219.srt', '1293094.srt', '1293736.srt', '1292224.srt', '27000981.srt', '1295805.srt', '1295425.srt', '3001114.srt', '2609258.srt', '30252495.srt', '1292269.srt', '35430833.srt', '1298468.srt', '3042261.srt', '1293413.srt', '1292349.srt', '6307447.srt', '26588314.srt', '1293505.srt', '1293764.srt', '1292063.srt', '1292563.srt', '1305666.srt', '3626372.srt', '1295184.srt', '1299131.srt', '1293348.srt', '1293688.srt', '1293889.srt', '1296617.srt', '1294508.srt', '1296282.srt', '1295467.srt', '34463995.srt', '1293374.srt', '2997076.srt', '26648249.srt', '33437152.srt', '1292927.srt', '1300725.srt', '6538866.srt', '35240917.srt', '1293307.srt', '1950330.srt', '1297602.srt', '1293194.srt', '30170546.srt', '1296821.srt', '1292225.srt', '1292766.srt', '1294477.srt', '26305582.srt', '1469159.srt', '2213597.srt', '4058933.srt', '33432655.srt', '1296908.srt', '26809592.srt', '26716348.srt', '1291853.srt', '24815950.srt', '1295260.srt', '1298624.srt', '1292472.srt', '3078514.srt', '1297205.srt', '1293767.srt', '6097775.srt', '1293544.srt', '26220650.srt', '26688480.srt', '2336735.srt', '26752852.srt', '27119724.srt', '1295137.srt', '1300520.srt', '1291572.srt', '1294245.srt', '1293203.srt', '1315316.srt', '1300365.srt', '34888057.srt', '1296180.srt', '1292403.srt', '25980443.srt', '1293926.srt', '1929463.srt', '26990609.srt', '30314848.srt', '1304641.srt', '5300054.srt', '1293566.srt', '1296987.srt', '1292541.srt', '1652587.srt', '1293155.srt', '30481476.srt', '1298812.srt', '27605105.srt', '1291870.srt']
for i in utf8:
    src = f"C:\\subtitle\\{i}"
    dst = r"C:\subtitle\utf8"
    shutil.copy2(src,dst)