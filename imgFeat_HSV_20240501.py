import cv2
from PIL import Image

# convert BGR to HSV
# image = cv2.imread(r'C:\Users\85270\Downloads\images.jpg')
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# # cv2.imshow('Input', image)
# # cv2.imshow('Result', hsv)
# # cv2.waitKey(0)
# hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
# print(hsv[0])


# import required libraries
import numpy as np
import cv2

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
    # # compute the lower and upper limits
    # lowerLimit = hsvGreen[0][0][0] - 10, 100, 100
    # upperLimit = hsvGreen[0][0][0] + 10, 255, 255

    # # display the lower and upper limits
    # print("Lower Limit:",lowerLimit)
    # print("Upper Limit", upperLimit)

print(rgb2hsv([174, 26, 1]))