# -*- coding:utf-8 -*-
import points as p
from time import sleep
import cv2
import sys
from sub import get_img
from image import cut_image,  compare_image

# adb调用


def order(orders):
    '''adb调用'''
    import subprocess
    return subprocess.Popen(orders)


def screencap(string):
    '''截图'''
    order('adb shell screencap -p /storage/emulated/0/Pictures/' + string)
    sleep(1)
    order('adb pull /storage/emulated/0/Pictures/' + string)
    return cv2.imread(string)


def click(x, y, tim=0.5):
    '''点击'''
    import random
    x = x + random.randint(-20, 20)
    y = y + random.randint(-20, 20)
    order('adb shell input tap %d %d' % (x, y))
    sleep(tim)


def click_s(x, y, tim=0.5):
    '''精确点击'''
    order('adb shell input tap %d %d' % (x, y))
    sleep(tim)


def swipe(x1, y1, x2, y2, tim):
    order('adb shell input touchscreen swipe %d %d %d %d %d' %
          (x1, y1, x2, y2, tim))


def attack(value):
    if value == 1:
        click(p.attack_1[0], p.attack_1[1])  # 普通攻击1
    elif value == 2:
        click(p.attack_2[0], p.attack_2[1])  # 普通攻击2


def card(value):
    click(p.card_c[0], p.card_c[1], 1)
    if value == 1:
        click(p.card_1[0], p.card_1[1])  # 符卡1
    elif value == 2:
        click(p.card_2[0], p.card_2[1])  # 符卡2
    elif value == 3:
        click(p.card_3[0], p.card_3[1])  # 符卡3
    elif value == 4:
        click(p.card_4[0], p.card_4[1])  # 符卡4
    elif value == 5:
        click(p.card_5[0], p.card_5[1])
    sleep(1.4)


def graze(value):
    if value >= 1:
        click(p.graze[0], p.graze[1])  # 结界1
    if value >= 2:
        click(p.graze[0], p.graze[1])  # 结界2
    if value >= 3:
        click(p.graze[0], p.graze[1])  # 结界3


ZERO = cv2.imread(sys.path[0] + '\\IMG\\zero.jpg')
ONE = cv2.imread(sys.path[0] + '\\IMG\\one.jpg')
TWO = cv2.imread(sys.path[0] + '\\IMG\\two.jpg')
THREE = cv2.imread(sys.path[0] + '\\IMG\\three.jpg')


def boost(value, get_img=get_img):
    sleep(0.5)
    img = cut_image(708, 731, 1324, 1348, get_img())
    # 当前拥有的p点
    possibility = []
    possibility.append(compare_image(img, ZERO))
    possibility.append(compare_image(img, ONE))
    possibility.append(compare_image(img, TWO))
    possibility.append(compare_image(img, THREE))
    # 找到最接近的数字
    boost_you_have = possibility.index(max(possibility))
    # print(boost_you_have)
    # 判断
    if boost_you_have == 0:
        return
    elif value > boost_you_have:
        value = boost_you_have
    # 输出
    if value >= 1:
        click(p.boost[0], p.boost[1])  # boost1
    if value >= 2:
        click(p.boost[0], p.boost[1])  # boost2
    if value >= 3:
        click(p.boost[0], p.boost[1])  # boost3


def skill(value):
    if isinstance(value, int):
        value = [value]
    click(1524, 671)
    sleep(0.5)
    for i in range(0, len(value)):
        if value[i] == 1.1:
            click(242, 741)
        elif value[i] == 1.2:
            click(368, 741)
        elif value[i] == 1.3:
            click(748, 741)
        elif value[i] == 2.1:
            click(687, 741)
        elif value[i] == 2.2:
            click(807, 741)
        elif value[i] == 2.3:
            click(933, 741)
        elif value[i] == 3.1:
            click(1124, 741)
        elif value[i] == 3.2:
            click(1232, 741)
        elif value[i] == 3.3:
            click(1359, 741)
        else:
            return
        click(967, 701)
    click(1524, 671)


if __name__ == "__main__":
    while True:
        click(878, 590)
        click(976, 720)
