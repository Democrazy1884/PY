# -*- coding:utf-8 -*-
from fight import action, selection, endfind
from image import cut_image, screenshot, mathc_img
import cv2
import time


if 1:
    img = screenshot()
    cv2.imwrite('1.jpg', img)
if 0:
    img = cv2.imread('1.jpg')
if 1:
    img1 = cut_image(13, 48, 89, 231, img)
    cv2.imwrite('z.jpg', img1)
