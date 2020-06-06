# -*- coding:utf-8 -*-
import cv2
import sys
from image import cut_image, compare_image
from adb import click
from sub import get_img


HARD = cv2.imread(sys.path[0] + "\\IMG\\hard.jpg")  # 难度hard的图
LUNATIC = cv2.imread(sys.path[0] + "\\IMG\\lunatic.jpg")  # 难度lunatic的图
NORMAL = cv2.imread(sys.path[0] + "\\IMG\\normal.jpg")  # 难度normal的图


def adjust(sel):
    """调整难度

    :sel: 1:normal 2:hard 3:lunatic

    """
    while True:
        img = cut_image(797, 824, 457, 633, get_img())
        if compare_image(img, LUNATIC) > 0.8:
            now = 3
        elif compare_image(img, HARD) > 0.8:
            now = 2
        elif compare_image(img, NORMAL) > 0.8:
            now = 1
        if now == sel:
            break
        else:
            click(541, 808)
