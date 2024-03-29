import urllib.request as req
from bs4 import BeautifulSoup as bs
import pyodbc

#=============================================================
Server = 'tcp:140.136.155.46,1433'
DBName = 'msdb'
ID = 'sa'
PWD = 'qazwsx'
Driver = '{ODBC Driver 18 for SQL Server}'
#=============================================================

class MovieInfo():
    def __init__(self) -> None:
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
        for each_review in root.find_all('div', {'class':'comment-item'}):
            self.review_id = each_review['data-cid']
            self.review_vote = each_review.find('span', {"class": "votes vote-count"}).text
            self.review_time = each_review.find('span', {"class": "comment-time"}).text
            self.review_content = each_review.find('span', {"class": "short"}).text

            print('-'*40)
            print(self.review_id)
            print(self.review_time, '\n')
            print(self.review_content, '\n')
            print(self.review_vote, '\n')

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
                print(self.review_star, '\n')
            if 'star40' in TS:
                star = '4'
                classification = '正面'
                self.review_star = star +' '+ classification
                print(self.review_star, '\n')
            if 'star30' in TS:
                star = '3'
                classification = '中立'
                self.review_star = star +' '+ classification
                print(self.review_star, '\n')
            if 'star20' in TS:
                star = '2'
                classification = '負面'
                self.review_star = star +' '+ classification
                print(self.review_star, '\n')
            if 'star10' in TS:
                star = '1'
                classification = '非常負面'
                self.review_star = star +' '+ classification
                print(self.review_star, '\n')
            print("="*50)
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

def StoreData():
    for item in movie_review.get_info:
    # Assuming the table name is 'your_table_name' and you have columns 'column1', 'column2', and 'column3'
        query = f"INSERT INTO your_table_name (column1, column2, column3) VALUES (?, ?, ?)"
        cursor.execute(query, item['value1'], item['value2'], item['value3'])
    connection.commit()
    connection.close()

MID = 
start = 
limit = 
status = 
url = 'https://movie.douban.com/subject/26752852/comments?start=0&limit=200&status=P&sort=new_score'
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



