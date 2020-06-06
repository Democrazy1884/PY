# -*- coding:utf-8 -*-
from fight import action, selection, endfind
from image import cut_image, mathc_img
import cv2
import time
from sub import Sub, get_img

Sub.start()
if 1:
    img = get_img()
    cv2.imwrite("1.jpg", img)
if 0:
    img = cv2.imread("1.jpg")
if 1:

    img = cut_image(795, 831, 1388, 1465, img)
    cv2.imwrite("z.jpg", img)
Sub.stop()
