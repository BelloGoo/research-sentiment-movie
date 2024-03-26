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
        r_id = root.find_all('div', {'class': 'comment-item'})
        self.review_vote = root.find_all('span', {"class": "votes vote-count"})
        # comment_star_pre = root.find_all('span')
        self.review_time = root.find_all('span', {"class": "comment-time"})
        self.review_content = root.find_all('span', {"class": "short"})

        # for input in comment_id_pre:
        #     temp = input.get('value')
        #     self.comment_id.append(temp)
        for i in r_id:
            self.review_id = i['data-cid']
            print(self.review_id)
        print(self.review_vote, '\n')
        # for span in comment_star_pre:
        #     # for num in f'allstar{range(10,51,10)}':
        #         temp = span.get('allstar')
        #         self.comment_star.append(temp)
        print(self.comment_star)
        print(self.review_time, '\n')
        print(self.review_content, '\n')

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
# movie_review.get_info()
star = ''
classification = ''
Bstring = ''
Sstring = root.find_all('span')
for i in Sstring:
    if 'star50' in str(i):
        star = '5'
        classification = '非常正面'
        Bstring += star +'|'+ classification
    print(type(i))
    print(i)
    # if 'star40' in i:
    #     star = '4'
    #     classification = '正面'
    #     Bstring += star, classification
    # if 'star30' in i:
    #     star = '3'
    #     classification = '中立'
    #     Bstring += star, classification
    # if 'star20' in i:
    #     star = '2'
    #     classification = '負面'
    #     Bstring += star, classification
    # if 'star10' in i:
    #     star = '1'
    #     classification = '非常負面'
    #     Bstring += star, classification
print(Bstring)


# data = []


# for X in root.find_all("div", {"class":"comment-item"}):
#     print("B================================")
#     for Y in X.find_all("span"):
#     #   print(Y.contents)
#       print(Y.find('span')['href'])
#     print("S================================")