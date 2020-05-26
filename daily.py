from adb import swipe, click
from time import sleep
from image import compare_image, cut_image, mathc_img
import cv2
import sys
from fight import offlinefind, img, substart, substop, event

img


# # # # # # # # # # # # # # # # # # # # #  判断函数  # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # #  行动函数  # # # # # # # # # # # # # # # # # # #



substart()
event.done.wait()
cv2.imwrite('x.jpg', img)

if mainpage_marchfind(img):
    click(1390, 537)
    while True:
        offlinefind(img)
        if marchfind(img):
            m_list = March.start(img)
            break
    click(75, 184)
    swipe(1560, 615, 1557, 261, 200)
    waiting = []
    doing = []
    done = []
    for n in range(0, len(m_list)):
        if m_list[n].situation == 'waiting':
            waiting.append(n)
        elif m_list[n].situation == 'doing':
            doing.append(n)
        elif m_list[n].situation == 'done':
            done.append(n)
