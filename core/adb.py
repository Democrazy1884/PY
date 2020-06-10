# -*- coding:utf-8 -*-
"""adb调用"""
import random
import subprocess
from functools import wraps
from time import sleep

import cv2

import core.points as p
from core.sub import get_img
from core.universe import search


def order(orders):
    """adb调用"""
    return subprocess.Popen(orders, shell=True)


def screencap(string):
    """截图"""
    order("adb shell screencap -p /storage/emulated/0/Pictures/" + string)
    sleep(1)
    order("adb pull /storage/emulated/0/Pictures/" + string)
    return cv2.imread(string)


def typeassert(func):
    "click 输入检查"

    @wraps(func)
    def wrapper(*args, **kwargs):
        tim = 0.5
        point = [0, 0]
        if len(args) == 1 and isinstance(args[0], (tuple, list)):
            point = args[0]
        elif len(args) == 2:
            if isinstance(args[0], (tuple, list)) and isinstance(args[1], int):
                point = args[0]
                tim = args[1]
            elif isinstance(args[0], int) and isinstance(args[1], int):
                point[0] = args[0]
                point[1] = args[1]
            else:
                raise TypeError
        elif len(args) == 3:
            if (
                isinstance(args[0], int)
                and isinstance(args[1], int)
                and isinstance(args[1], int)
            ):
                point[0] = args[0]
                point[1] = args[1]
                tim = args[2]
            else:
                raise TypeError
        else:
            raise TypeError
        return func(point, tim)

    return wrapper


@typeassert
def click(point, tim):
    """点击"""
    order(
        "adb shell input tap %d %d"
        % (point[0] + random.randint(-20, 20), point[1] + random.randint(-20, 20))
    )
    sleep(tim)


@typeassert
def click_s(point, tim):
    """精确点击"""
    order("adb shell input tap %d %d" % (point[0], point[1]))
    sleep(tim)


def swipe(x1, y1, x2, y2, tim):
    order("adb shell input touchscreen swipe %d %d %d %d %d" % (x1, y1, x2, y2, tim))


def attack(value):
    if value == 1:
        click(p.attack_1[0], p.attack_1[1])  # 普通攻击1
    elif value == 2:
        click(p.attack_2[0], p.attack_2[1])  # 普通攻击2


def card(value):
    click(p.card_c, 1)
    if value == 1:
        click(p.card_1)  # 符卡1
    elif value == 2:
        click(p.card_2)  # 符卡2
    elif value == 3:
        click(p.card_3)  # 符卡3
    elif value == 4:
        click(p.card_4)  # 符卡4
    elif value == 5:
        click(p.card_5)
    sleep(1.4)


def graze(value):
    if value >= 1:
        click(p.graze)  # 结界1
    if value >= 2:
        click(p.graze)  # 结界2
    if value >= 3:
        click(p.graze)  # 结界3


def boost(value, img=get_img):
    sleep(0.5)
    boost_you_have = search(708, 731, 1324, 1348, "BOOSTNUMBER", 0.8)
    if boost_you_have is False:
        search(708, 731, 1324, 1348, "BOOSTNUMBER", 0.8)
    # 判断
    if boost_you_have == 0:
        return
    elif value > boost_you_have:
        value = boost_you_have
    # 输出
    if value >= 1:
        click(p.boost)  # boost1
    if value >= 2:
        click(p.boost)  # boost2
    if value >= 3:
        click(p.boost)  # boost3


def skill(value):
    if isinstance(value, float):
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
        click(604, 614)
        sleep(1)
        click(976, 720)
        sleep(1)
