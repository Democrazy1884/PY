# -*- coding:utf-8 -*-
from image import cut_image, mathc_img
import cv2
import time
from sub import Sub, get_img

Sub.start()
if 0:
    img = get_img()
    cv2.imwrite("1.jpg", img)
if 1:
    img = cv2.imread("x.jpg")
if 1:

    img = cut_image(694, 738, 1422, 1524, get_img())
    cv2.imwrite("2.jpg", img)
Sub.stop()
