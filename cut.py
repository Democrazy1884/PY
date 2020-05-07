# -*- coding:utf-8 -*-
#图片裁剪
import cv2
def cut_image(y0,y1,x0,x1,path_image1, path_image2):
    img = cv2.imread(path_image1)
    cropped = img[0:128, 0:512]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite(path_image2, cropped)

cut_image("screenshot.jpg","test.jpg")
