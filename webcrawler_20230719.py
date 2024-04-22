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

class MovieReview:
    def __init__(self):
        self.review_id = ''
        self.review_vote = ''
        self.review_star = ''
        self.review_time = ''
        self.review_content = ''
        

    def get_info(self):
        '''get info from the web'''
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

            
                query = f"INSERT INTO review_ (id, vote, star, time_, content_, RCtrad, RCtag, MID) VALUES ({self.review_id},  {self.review_vote}, N'{self.review_star}', trim('{self.review_time}'), N'{self.review_content}', N'{RCtrad}', N'{RCtag}', N'{newMID}')"
                # print(query)
                MakeSQL(query)
        except Exception as e:
            # print('Exception: ',e)
            pass
        return
    

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


start = ['0', '200', '400', '600']

# 這個MCT是目前還沒有做完的MID的數量, 當這個MCT大於0的話，就再去抓下一個
MCT = int(OneSQL("SELECT count(*) FROM dbo.MID WHERE haddone = 0"))
# a = OneSQL("SELECT count(*) FROM dbo.MID WHERE haddone = 0")
# print(MCT)
while (MCT > 0):
    print('unprocessed: ', MCT, '/361')
    #取得一個沒完成的MID
    newMID = OneSQL("select top 1 mid from dbo.mid where haddone = 0 order by newid()")
    newMID = str(newMID).rstrip()
    print('MID: ',newMID)
    for page in start:
        try:
            url = 'https://movie.douban.com/subject/'+ newMID +'/comments?start='+ page +'&limit=200&status=P&sort=new_score'
            request = req.Request(url, headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
            })
            with req.urlopen(request) as response:
                data = response.read().decode('utf-8')
            #解析原始碼，取得每篇文章的標題
            root = bs(data, 'html.parser')
                
            # print(root.prettify())
            movie_review = MovieReview()
            movie_review.get_info()
            print('page: ', page)
            timeLag()
        except Exception as e:
            # print('Exception: ',e)
            continue
    # 先進行這次抓了的電影的更新, 把haddone改成1
    uSQL = f"Update dbo.MID SET haddone = 1 WHERE MID = '{newMID}'; "
    MakeSQL(uSQL)
    MCT = int(OneSQL("SELECT count(*) FROM dbo.MID WHERE haddone = 0"))



