# -*- coding:utf-8 -*-
from fight import action, selection, endfind
from image import cut_image, screenshot, mathc_img
import cv2
import time


if 0:
    img = screenshot()
    cv2.imwrite('1.jpg', img)
if 1:
    img = cv2.imread('1.jpg')
if 1:
    img = cut_image(708, 731, 1324, 1348, img)
    cv2.imwrite('z.jpg', img)
