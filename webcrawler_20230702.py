import urllib.request as req
from bs4 import BeautifulSoup as bs
import pyodbc
from opencc import OpenCC
import jieba.posseg as pseg
import time
import random as rd

#=============================================================
Server = 'tcp:140.136.155.46,1433'
DBName = 'movieDB'
ID = 'sa'
PWD = 'qazwsx'
Driver = '{ODBC Driver 18 for SQL Server}'
#=============================================================
cc = OpenCC('s2t')
pseg_ = pseg

class MovieInfo():
    def __init__(self) -> None:
        self.MID = ''
        self.director = ''
        self.starring = ''
        self.genre = ''
        self.region = ''
        self.duration = ''
        self.release_date = ''

#     def getMID(self):
#         IMDb = ['tt0056172',
# 'tt0056197',
# 'tt0056262',
# 'tt0056264',
# 'tt0056592',
# 'tt0056825',
# 'tt0056937',
# 'tt0056085',
# 'tt0057251',
# 'tt0057590',
# 'tt0057877',
# 'tt0057012',
# 'tt0058331',
# 'tt0058385',
# 'tt0057831',
# 'tt0059084',
# 'tt0059113',
# 'tt0059712',
# 'tt0059742',
# 'tt0059798',
# 'tt0375173',
# 'tt0060665',
# 'tt0060921',
# 'tt0060934',
# 'tt0061184',
# 'tt0061418',
# 'tt6673612',
# 'tt0061722',
# 'tt0061735',
# 'tt0061811',
# 'tt15309272',
# 'tt0063227',
# 'tt0063385',
# 'tt0063483',
# 'tt0063518',
# 'tt0064030',
# 'tt0064115',
# 'tt0064418',
# 'tt0064665',
# 'tt0065234',
# 'tt0065377',
# 'tt0065724',
# 'tt0066011',
# 'tt0066026',
# 'tt0066206',
# 'tt0066921',
# 'tt0067093',
# 'tt0067116',
# 'tt0067328',
# 'tt0067483',
# 'tt0068327',
# 'tt0068473',
# 'tt0067919',
# 'tt0068646',
# 'tt0069303',
# 'tt0069704',
# 'tt0069467',
# 'tt0070047',
# 'tt0070735',
# 'tt0070819',
# 'tt0071315',
# 'tt0071360',
# 'tt0071562',
# 'tt0071746',
# 'tt0072308',
# 'tt0072684',
# 'tt0072890',
# 'tt0073195',
# 'tt0073440',
# 'tt0073486',
# 'tt0074119',
# 'tt0074235',
# 'tt0074958',
# 'tt0075148',
# 'tt0075314',
# 'tt0075686',
# 'tt0076095',
# 'tt0071754',
# 'tt0076759',
# 'tt0076843',
# 'tt0077362',
# 'tt0077416',
# 'tt0077663',
# 'tt0077928',
# 'tt0078444',
# 'tt0078754',
# 'tt0078788',
# 'tt0078902',
# 'tt0079417',
# 'tt0079638',
# 'tt0080549',
# 'tt0080678',
# 'tt0081283',
# 'tt0081398',
# 'tt0080009',
# 'tt0080388',
# 'tt0082158',
# 'tt0082846',
# 'tt0082971',
# 'tt0082979',
# 'tt0083866',
# 'tt0083987',
# 'tt0084335',
# 'tt0084805',
# 'tt0084855',
# 'tt0085244',
# 'tt4247618',
# 'tt0086197',
# 'tt0086423',
# 'tt0086425',
# 'tt0086879',
# 'tt0087553',
# 'tt0087892',
# 'tt0087921',
# 'tt0088146',
# 'tt0088939',
# 'tt0089424',
# 'tt0089755',
# 'tt0089841',
# 'tt0090329',
# 'tt0090830',
# 'tt0091167',
# 'tt0091530',
# 'tt0091763',
# 'tt0091867',
# 'tt0092699',
# 'tt0093010',
# 'tt0093209',
# 'tt0093389',
# 'tt0093565',
# 'tt0094606',
# 'tt0094947',
# 'tt0095647',
# 'tt0095953',
# 'tt0096463',
# 'tt0096969',
# 'tt0097165',
# 'tt0097239',
# 'tt0097351',
# 'tt0097937',
# 'tt0099077',
# 'tt0099348',
# 'tt0099653',
# 'tt0099674',
# 'tt0099685',
# 'tt0101414',
# 'tt0101516',
# 'tt0102138',
# 'tt0102713',
# 'tt0102926',
# 'tt0104036',
# 'tt0104257',
# 'tt0104454',
# 'tt0105323',
# 'tt0105695',
# 'tt0106977',
# 'tt0107207',
# 'tt0107822',
# 'tt0107943',
# 'tt0108052',
# 'tt0109830',
# 'tt0109831',
# 'tt0110912',
# 'tt0110932',
# 'tt0111161',
# 'tt0112384',
# 'tt0112431',
# 'tt0112573',
# 'tt0110877',
# 'tt0114388',
# 'tt0116209',
# 'tt0116282',
# 'tt0116695',
# 'tt0117589',
# 'tt0081505',
# 'tt0119822',
# 'tt0119164',
# 'tt0119217',
# 'tt0119488',
# 'tt0120338',
# 'tt0127536',
# 'tt0118799',
# 'tt0120815',
# 'tt0138097',
# 'tt0120863',
# 'tt0169547',
# 'tt0124315',
# 'tt0120689',
# 'tt0140352',
# 'tt0167404',
# 'tt0241303',
# 'tt0190332',
# 'tt0195685',
# 'tt0172495',
# 'tt0181865',
# 'tt0268978',
# 'tt0280707',
# 'tt0247425',
# 'tt0120737',
# 'tt0203009',
# 'tt0299658',
# 'tt0217505',
# 'tt0274558',
# 'tt0167261',
# 'tt0253474',
# 'tt0167260',
# 'tt0335266',
# 'tt0311113',
# 'tt0327056',
# 'tt0329575',
# 'tt0338751',
# 'tt0308644',
# 'tt0405159',
# 'tt0350258',
# 'tt0375063',
# 'tt0388795',
# 'tt0379725',
# 'tt0375679',
# 'tt0433383',
# 'tt7475578',
# 'tt0449467',
# 'tt0407887',
# 'tt0498380',
# 'tt0449059',
# 'tt0436697',
# 'tt0783233',
# 'tt0467406',
# 'tt0465538',
# 'tt0477348',
# 'tt0469494',
# 'tt0421715',
# 'tt0870111',
# 'tt1013753',
# 'tt0976051',
# 'tt1010048',
# 'tt0499549',
# 'tt0878804',
# 'tt1136608',
# 'tt1174732',
# 'tt0887912',
# 'tt0361748',
# 'tt0929632',
# 'tt1019452',
# 'tt1049413',
# 'tt1193138',
# 'tt0947798',
# 'tt0964517',
# 'tt1375666',
# 'tt0842926',
# 'tt1504320',
# 'tt1542344',
# 'tt1285016',
# 'tt0435761',
# 'tt1403865',
# 'tt1399683',
# 'tt1655442',
# 'tt1033575',
# 'tt0477302',
# 'tt1454029',
# 'tt0970179',
# 'tt1605783',
# 'tt1210166',
# 'tt0478304',
# 'tt1568911',
# 'tt1602620',
# 'tt1024648',
# 'tt2125435',
# 'tt1853728',
# 'tt1707386',
# 'tt0454876',
# 'tt0443272',
# 'tt1045658',
# 'tt1790885',
# 'tt1800241',
# 'tt1535109',
# 'tt0790636',
# 'tt1454468',
# 'tt1798709',
# 'tt1821549',
# 'tt2431286',
# 'tt2024544',
# 'tt0993846',
# 'tt2179136',
# 'tt2562232',
# 'tt1065073',
# 'tt2278388',
# 'tt2084970',
# 'tt1020072',
# 'tt2980516',
# 'tt2582802',
# 'tt1596363',
# 'tt3682448',
# 'tt2381111',
# 'tt1392190',
# 'tt3659388',
# 'tt1663202',
# 'tt3170832',
# 'tt1895587',
# 'tt2543164',
# 'tt2671706',
# 'tt2119532',
# 'tt2582782',
# 'tt4846340',
# 'tt3783958',
# 'tt3741834',
# 'tt4034228',
# 'tt4975722',
# 'tt5726616',
# 'tt4555426',
# 'tt5013056',
# 'tt5052448',
# 'tt4925292',
# 'tt5776858',
# 'tt6294822',
# 'tt5580390',
# 'tt5027774',
# 'tt1825683',
# 'tt7349662',
# 'tt1727824',
# 'tt5083738',
# 'tt6966692',
# 'tt6155172',
# 'tt1517451',
# 'tt6266538',
# 'tt1950186',
# 'tt1302006',
# 'tt2584384',
# 'tt7286456',
# 'tt3281548',
# 'tt7653254',
# 'tt8579674',
# 'tt7131622',
# 'tt6751668',
# 'tt10272386',
# 'tt9784798',
# 'tt10618286',
# 'tt10633456',
# 'tt9770150',
# 'tt9620292',
# 'tt5363618',
# 'tt1070874',
# 'tt12789558',
# 'tt10366460',
# 'tt11286314',
# 'tt14039582',
# 'tt1160419',
# 'tt9620288',
# 'tt11271038',
# 'tt7740496',
# 'tt10293406',
# 'tt3581652',
# 'tt1016150',
# 'tt1630029',
# 'tt11813216',
# 'tt11813216',
# 'tt6710474',
# 'tt14208870',
# 'tt14444726',
# 'tt1745960',
# 'tt7322224',
# 'tt13669038',
# ]
#         # for i in IMDb:
#         URL_IMDb = 'https://search.douban.com/movie/subject_search?search_text='+ 'tt0056172' +'&cat=1002'
#         request = req.Request(URL_IMDb, headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
#         })
#         with req.urlopen(request) as response:
#             data_IMDb = response.read().decode('utf-8')
#         root_IMDb = bs(data_IMDb, 'html.parser')
#         # print(data_IMDb)
#         tem_MID = (root_IMDb.find('span', {'class': 'rec'})['id']).text
#         self.MID += (tem_MID)
#         print(self.MID)

class MovieReview:
    def __init__(self):
        self.review_id = ''
        self.review_vote = ''
        self.review_star = ''
        self.review_time = ''
        self.review_content = ''
        

    def get_info(self):
        '''get info from the web'''
        count = 0
        try:
            for each_review in root.find_all('div', {'class':'comment-item'}):
                self.review_id = each_review['data-cid']
                self.review_vote = each_review.find('span', {"class": "votes vote-count"}).text
                self.review_time = each_review.find('span', {"class": "comment-time"}).text
                self.review_content = each_review.find('span', {"class": "short"}).text

                # print('-'*40)
                # print('review id: ',self.review_id)
                # print('review time: ',self.review_time, '\n')
                # print('review content: ',self.review_content, '\n')
                # print('review vote: ',self.review_vote, '\n')

                star = ''
                classification = ''
                TS = ''
                Sstring = each_review.find_all('span')
                for i in Sstring:
                    TS += str(i)
                if 'star50' in TS:
                    star = '5'
                    classification = '非常正面'
                    self.review_star = star +' '+ classification
                    # print('review star: ',self.review_star, '\n')
                if 'star40' in TS:
                    star = '4'
                    classification = '正面'
                    self.review_star = star +' '+ classification
                    # print('review star: ',self.review_star, '\n')
                if 'star30' in TS:
                    star = '3'
                    classification = '中立'
                    self.review_star = star +' '+ classification
                    # print('review star: ',self.review_star, '\n')
                if 'star20' in TS:
                    star = '2'
                    classification = '負面'
                    self.review_star = star +' '+ classification
                    # print('review star: ',self.review_star, '\n')
                if 'star10' in TS:
                    star = '1'
                    classification = '非常負面'
                    self.review_star = star +' '+ classification
                    # print('review star: ',self.review_star, '\n')

                RCtrad = cc.convert(self.review_content)
                RCseg_list = pseg_.cut(self.review_content)
                # print('review content Trad: ',RCtrad)
                # print('review [word|tag]: ',RCseg_list)
                RCtag = ''
                for word, flag in RCseg_list:
                    trad_word = cc.convert(word)
                    RCtag += f'[{trad_word}|{flag}]'
                # print(RCtag)

            
                query = f"INSERT INTO review_ (id, vote, star, time_, content_, RCtrad, RCtag, MID) VALUES ({self.review_id},  {self.review_vote}, N'{self.review_star}', trim('{self.review_time}'), N'{self.review_content}', N'{RCtrad}', N'{RCtag}', N'{mid}')"
                # print(query)
                MakeSQL(query)
                # count += 1
                # print('count: ', count)
                # print("="*50)
        except Exception as e:
            print(e)
            continue
        return count
    
    # def StoreData(self):
    #     query = f"INSERT INTO review_ (id, vote, star, time_, content_) VALUES ({self.review_id},  {self.review_vote}, '{self.review_star}','{self.review_time}','{self.review_content}')"
    #     print(query)
    #     MakeSQL(query)

class LinkGrabber:
    def __init__(self):
        self.link_pool = {} #a set of links grabbed from the website
    
    def grabber(self):
        pass

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

def timeLag():
    time_lag = rd.randint(3,10)
    print('time_lag: ',time_lag)
    time.sleep(time_lag)

MID = ['1292349',
'1293626',
'1296180',
'1292862',
'1297991',
'1469159',
'1292550',
'1296467',
'1294920',
'1292591',
'1947729',
'1322848',
'1292658',
'1297965',
'1417676',
'1437774',
'1389949',
'1293228',
'1294408',
'1297205',
'1483944',
'1296260',
'1292566',
'1298812',
'1295137',
'1294584',
'27000981',
'1292271',
'1293688',
'1295480',
'1300891',
'1293104',
'1293219',
'1293413',
'1295467',
'1298762',
'1297602',
'1293094',
'1297628',
'1299026',
'1293348',
'1298192',
'1294768',
'1292766',
'1298308',
'1292233',
'1298517',
'3013046',
'1298026',
'1295425',
'1296282',
'1293561',
'1295184',
'1291841',
'1293307',
'1300106',
'1296147',
'1293755',
'1292269',
'1292941',
'1293889',
'1296908',
'1299131',
'1294087',
'1298056',
'1292472',
'1293374',
'1294941',
'1293037',
'1292224',
'1293715',
'1293194',
'1297531',
'1295742',
'1292222',
'1296987',
'1293505',
'3110825',
'1293838',
'1292563',
'1295688',
'1292403',
'1293809',
'1296827',
'1293163',
'1299330',
'1292260',
'1292932',
'1300685',
'1294986',
'1295805',
'1293200',
'1294925',
'1293155',
'1291872',
'1294508',
'1300487',
'1293767',
'1296717',
'1292891',
'1294638',
'1292238',
'1292927',
'1297737',
'1300725',
'1293796',
'1295692',
'1293371',
'1300520',
'1293341',
'1293399',
'1296617',
'1291834',
'1292667',
'1294327',
'1294503',
'1299879',
'1291840',
'1293804',
'1293229',
'1300422',
'1292764',
'1294620',
'1293396',
'1293926',
'1292511',
'1294587',
'1294245',
'1293172',
'1292869',
'1293736',
'1295713',
'1300365',
'1291870',
'1294849',
'1292874',
'1291548',
'1293204',
'1294070',
'1294000',
'1296805',
'1293764',
'1293203',
'1294240',
'1292268',
'1297995',
'1292452',
'1292230',
'1297398',
'1293544',
'1298370',
'1295260',
'1293706',
'1298624',
'1293566',
'1297229',
'1297009',
'1293818',
'1293004',
'1295124',
'1292720',
'1294950',
'1291832',
'1292759',
'1292052',
'1293785',
'1292765',
'1294639',
'1298468',
'1299193',
'1291853',
'1292067',
'1293158',
'1294477',
'1292225',
'1293917',
'1292541',
'1292656',
'1292348',
'1292722',
'1296223',
'1292063',
'1292849',
'1300220',
'1292781',
'1292062',
'1296821',
'1300374',
'1292660',
'1297630',
'1301890',
'1301168',
'1293050',
'1293530',
'1299235',
'1306029',
'1306860',
'1306604',
'1291571',
'1304641',
'1307697',
'1301061',
'1305666',
'1291572',
'1296736',
'1291552',
'1291835',
'1307749',
'1307748',
'1307535',
'1309070',
'1308831',
'1309016',
'1309085',
'1291833',
'1418834',
'1422957',
'1388216',
'1431617',
'35240917',
'1498818',
'1315316',
'1917171',
'1777612',
'1866264',
'1950148',
'2132495',
'1905790',
'1857099',
'1945780',
'1485260',
'2062678',
'2336737',
'2213597',
'2209573',
'1652587',
'3552028',
'3006772',
'3011093',
'2028645',
'1438652',
'3011072',
'3135483',
'2129039',
'3077791',
'1978709',
'2056093',
'3541415',
'3569969',
'4023638',
'4164444',
'3205624',
'1858711',
'3626372',
'3610676',
'6097775',
'3071509',
'3078514',
'3792848',
'2028677',
'4319218',
'3023164',
'2336735',
'4206436',
'4798707',
'6549903',
'7015714',
'6307447',
'6860160',
'1929463',
'1889242',
'3094909',
'6430835',
'6873657',
'4116480',
'1793929',
'3793783',
'6722879',
'6538833',
'19973780',
'6879185',
'2997076',
'21263666',
'20438962',
'2209575',
'11525673',
'10463953',
'3089638',
'24815950',
'25773932',
'26303622',
'25908051',
'10741220',
'3592854',
'25864085',
'5327268',
'25724855',
'25954475',
'21324900',
'21339682',
'26325320',
'26389148',
'26615208',
'25934014',
'26220650',
'25980443',
'26648249',
'26799731',
'26761416',
'26607693',
'26688480',
'26588314',
'26809592',
'26990609',
'26752852',
'26611804',
'6390825',
'27133913',
'5300054',
'26628282',
'27060077',
'1950330',
'4058933',
'26920842',
'6538866',
'6981153',
'30170546',
'27119724',
'26348103',
'27202818',
'30252495',
'27087724',
'27010768',
'33432655',
'30464264',
'34461705',
'34463995',
'30458949',
'30450313',
'26716348',
'2609258',
'35299584',
'35048413',
'34884712',
'35235502',
'3001114',
'30481476',
'34888057',
'27605105',
'33437152',
'26820621',
'3042261',
'4811774',
'34969348',
'26305582',
'30314848',
'35390098',
'35430833',
'6893932',
'27066152',
'35290372',
]

start = ['0', '200', '400', '600']
# MID = ['1292349','1293626','1296180','1292862','1297991','1469159',]
# start = '200'
# limit = 
# status = 
# url = 'https://movie.douban.com/subject/"26752852"/comments?start="0"&limit=200&status=P&sort=new_score'
round = 0
recorded_movie = 0
where_to_start = 226
for mid in MID[where_to_start:]:
    for page in start:
        try:
            url = 'https://movie.douban.com/subject/'+ mid +'/comments?start='+ page +'&limit=200&status=P&sort=new_score'
            request = req.Request(url, headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
            })
            with req.urlopen(request) as response:
                data = response.read().decode('utf-8')
        except Exception as e:
            print(e)
            continue
        print(url)


    #解析原始碼，取得每篇文章的標題

        root = bs(data, 'html.parser')
        # print(root.prettify())
        movie_review = MovieReview()
        movie_review.get_info()
        round += 1
        print('total count: ', round*movie_review.get_info(), '; MID: ',mid, '; page: ', page)
        print('recorded movies: ',recorded_movie + where_to_start,"/",len(MID))
        timeLag()
    recorded_movie += 1
    print('recorded movies: ',recorded_movie + where_to_start,"/",len(MID))




# movieinfo = MovieInfo()
# movieinfo.getMID()