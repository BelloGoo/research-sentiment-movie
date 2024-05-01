import urllib.request as req
from bs4 import BeautifulSoup as bs
from webcrawler_20230719 import timeLag
from subtitle_check_20230808 import MID, TITLEeng_plus, corresponding, abs_, tt_MID

def download_file(url, custom_filename):
    try:
        filesub = url[url.rfind("."):]
        file_path = 'C:\\subtitle\\{}{}'.format(custom_filename,filesub)

        req.urlretrieve(url, file_path)
        return True
    except:
        return False

def showingIndex():
    indexlist = []
    for i in MID:
        for j in abs_:
            if i == j:
                indexlist.append(MID.index(i))
    return indexlist

movie_not_found = []

count = 0
for movie in showingIndex():
    # finding values using index on dictionary
    # missing_index = list(corresponding.keys()).index(movie)
    # title = TITLEeng_plus[missing_index]

    try:
        # URL of the OpenSubtitles website
        url = "https://r3sub.com/movie.php?id="+ str(tt_MID[movie])

        request2 = req.Request(url, headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    })
    #     with req.urlopen(request) as response:
    #         data = response.read().decode('utf-8')
    #     root = bs(data, 'html.parser')
    #     # Find the download link
    #     # print(bs.prettify(root), '\n =================')
        prefix = 'https://r3sub.com/'
    #     suffix = root.find_all('a', {'class': 'introtitle'})[0]['href']
    #     target_movie = prefix + str(suffix)
    #     print('target movie: ',target_movie)
    #     request2 = req.Request(target_movie, headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    # })
        with req.urlopen(request2) as response2:
            data2 = response2.read().decode('utf-8')
        #解析原始碼，取得每篇文章的標題
        root2 = bs(data2, 'html.parser')
        is_trad = root2.find_all('span', {'class': 'btn-text btn--shine'})
        for i in is_trad:
            trad = i.getText()
            # print(trad)
            if '繁' in trad:
                download_link_suffix = i.find_next_siblings('a')[0]['href']
                # print(download_link_suffix)
        download_link = prefix + str(download_link_suffix)
        print('download link: ',download_link)

    # # Save the file
        # download_file(download_link, f'{MID[movie]}')
        print('just finished: ', MID[movie], '; index in the list: ', movie)
        count+=1
        print('unprocessed: ', (90-count))
        timeLag()
    except Exception as e:
        print('===========\nException: ',e)
        movie_not_found.append(movie)
        count+=1
        print(f'movie not found: {movie}\n==================')
        if e == '<urlopen error [WinError 10054] 遠端主機已強制關閉一個現存的連線。>':
            print('||||||we got banned.')
            break
        timeLag()
        continue
    
print('all movie not found: ',movie_not_found,f' ({len(movie_not_found)})')
