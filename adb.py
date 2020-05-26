# -*- coding:utf-8 -*-
import points as p
from time import sleep
import cv2


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


def click(x, y):
    '''adb点击'''
    import random
    x = x + random.randint(-40, 40)
    y = y + random.randint(-20, 20)
    order('adb shell input tap %d %d' % (x, y))
    sleep(0.5)


def swipe(x1, y1, x2, y2, tim):
    order('adb shell input swipe %d %d %d %d %d' % (x1, y1, x2, y2, tim))


def attack(value):
    if value == 1:
        click(p.attack_1[0], p.attack_1[1])  # 普通攻击1
    elif value == 2:
        click(p.attack_2[0], p.attack_2[1])  # 普通攻击2


def card(value):
    click(p.card_c[0], p.card_c[1])
    sleep(0.4)
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


def boost(value):
    if value >= 1:
        click(p.boost[0], p.boost[1])  # boost1
    if value >= 2:
        click(p.boost[0], p.boost[1])  # boost2
    if value >= 3:
        click(p.boost[0], p.boost[1])  # boost3


def skill(value):
    #
    #
    #
    click(1524, 671)
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
