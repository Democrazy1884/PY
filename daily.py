from img import compare_image, cut_image
import cv2
import sys
from fight import img

img
FIRST = cv2.imread(sys.path[0] + '\\IMG\\first.jpg')
MAIN = cv2.imread(sys.path[0] + '\\IMG\\main.jpg')


# # # # # # # # # # # # # # # # # # # # #  判断函数  # # # # # # # # # # # # # # # # # # #


def firstpagefind(img):
    '''初始界面判断'''
    x = compare_image(img, FIRST)
    if x > 0.8:
        return True
    else:
        return False


def mainpagefind(img):
    '''主界面判断'''
    x = compare_image(img, MAIN)
    if x > 0.8:
        return True
    else:
        return False


def spotfind(img):
    '''主界面红点判断'''
    img = cut_image()

# # # # # # # # # # # # # # # # # # # # #  行动函数  # # # # # # # # # # # # # # # # # # #
