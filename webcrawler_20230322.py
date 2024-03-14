
# import requests
# from bs4 import BeautifulSoup

# r = requests.get('https://movie.douban.com/subject/26752852/')
# print(r.text)


import urllib.request as req
url = 'https://movie.douban.com/subject/26752852/comments?status=P'
request = req.Request(url, headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
})
with req.urlopen(request) as response:
    data = response.read().decode('utf-8')

#解析原始碼，取得每篇文章的標題
import bs4
root = bs4.BeautifulSoup(data, 'html.parser')
titles = root.find_all('p', class_='comment-content') #尋找所有class = 'title'的span標籤
print(titles.span.string)