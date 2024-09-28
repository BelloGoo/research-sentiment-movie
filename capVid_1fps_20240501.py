import os
from moviepy.editor import VideoFileClip
from PIL import Image

def imgCrop(name,Left,Upper,Right,Lower):
    # 裁切圖片
    # 依照左上右下裁切
    im = Image.open(name)
    im = im.crop((Left, Upper, Right, Lower))
    im.save(name)

VIDEO_PATH = r"C:\Users\85270\OneDrive - 輔仁大學\文件\subjective well-being\movie_tag_related\MovieTagger\Movie\T07.Everything.Everywhere.All.At.Once.2022.mp4"
IMG_PATH = r'C:\Users\85270\OneDrive - 輔仁大學\桌面\Python\study\vidFrames'
# "D:\vidFrames"


os.chdir(IMG_PATH)  # 使用 Colab 要換路徑使用
video = VideoFileClip(VIDEO_PATH)

for i in range(1, int(video.duration) +1, 1): #10 replaced by int(video.duration)
    NAME = 'T07f'
    NAME = NAME + str(i) + '.jpg'
    frame = video.save_frame(NAME, t = i)
    # print(NAME + ' saved')
    # imgCrop(NAME, 0, 134, 1080, 586) # T01
    # imgCrop(NAME, 0, 72, 1080, 648) # T02
    # imgCrop(NAME, 0, 40, 1280, 680) # T03
    # imgCrop(NAME, 0, 138, 1920, 942) # T04
    # imgCrop(NAME, 0, 140, 1920, 940) # T05 (start from 320)(start from 4137)
    # imgCrop(NAME, 0, 140, 1080, 580) # T06 
    imgCrop(NAME, 0, 69, 1080, 651) # T07



