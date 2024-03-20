
# import requests
# from bs4 import BeautifulSoup

# r = requests.get('https://movie.douban.com/subject/26752852/')
# print(r.text)


import urllib.request as req


url = 'https://movie.douban.com/subject/26752852/comments?start=0&limit=200&status=P&sort=new_score'
request = req.Request(url, headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
})
with req.urlopen(request) as response:
    data = response.read().decode('utf-8')

#解析原始碼，取得每篇文章的標題
import bs4
root = bs4.BeautifulSoup(data, 'html.parser')

data = []

# for X in root.find_all("div", {"class":"comment-item"}):
#     print("B================================")
#     for Y in X.find_all("span"):
#       print(Y.contents)
#     print("S================================")

for X in root.find_all("div", {"class":"comment-item"}):
    print("B================================")
    for Y in X.find_all("span"):
    #   print(Y.contents)
      print(Y.find('span')['href'])
    print("S================================")



# import csv
# f = open('comments.csv', 'w', encoding = 'utf-8')
# csv_write = csv.writer(f)
# csv_write.writerow(['movie name', 'id', 'rating', 'date posted', 'like #', 'content'])

# for data in :
# csv_write.writerow([data['movie name'], data['starring'], data])