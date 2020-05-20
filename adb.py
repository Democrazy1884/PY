# -*- coding:utf-8 -*-
from points import x, y


# adb调用
def order(order):
    import subprocess
    adb_return = subprocess.Popen(order)
    return adb_return


def click(x, y):
    '''adb点击'''
    import random
    import time
    x = x + random.randint(-40, 40)
    y = y + random.randint(-20, 20)
    adb_return = order('adb shell input tap %d %d' % (x, y))
    time.sleep(0.6)
    return adb_return


def attack(value):
    #
    #
    #
    import time
    if value == 1:
        adb_return = click(x.attack1, y.attack1)  # 普通攻击1
    else:
        adb_return = click(x.attack2, y.attack2)  # 普通攻击2
    time.sleep(0.5)
    return adb_return


def card(value):
    #
    #
    #
    import time
    adb_return = click(79, 593)
    time.sleep(0.6)
    if value == 1:
        adb_return = click(280, 491)  # 符卡1
    elif value == 2:
        adb_return = click(523, 382)  # 符卡2
    elif value == 3:
        adb_return = click(751, 287)  # 符卡3
    elif value == 4:
        adb_return = click(1011, 242)
    else:
        pass
    time.sleep(1.4)
    return adb_return


def graze(value):
    # 当前结界数量
    #
    #
    #
    if value >= 1:
        adb_return = click(1435, 504)  # 结界1
    elif value >= 2:
        adb_return = click(1435, 504)  # 结界2
    elif value >= 3:
        adb_return = click(1435, 504)  # 结界3
    else:
        pass
    return adb_return


def boost(value):
    # 当前p点
    #
    #
    #
    if value >= 1:
        adb_return = click(x.boost, y.boost)  # boost1
    if value >= 2:
        adb_return = click(x.boost, y.boost)  # boost2
    if value >= 3:
        adb_return = click(x.boost, y.boost)  # boost3
    else:
        pass
    return adb_return


def skill(value):
    #
    #
    #
    adb_return = click(1524, 671)
    for i in range(0, len(value)):
        if value[i] == 1.1:
            adb_return = click(242, 741)
        elif value[i] == 1.2:
            adb_return = click(368, 741)
        elif value[i] == 1.3:
            adb_return = click(748, 741)
        elif value[i] == 2.1:
            adb_return = click(687, 741)
        elif value[i] == 2.2:
            adb_return = click(807, 741)
        elif value[i] == 2.3:
            adb_return = click(933, 741)
        elif value[i] == 3.1:
            adb_return = click(1124, 741)
        elif value[i] == 3.2:
            adb_return = click(1232, 741)
        elif value[i] == 3.3:
            adb_return = click(1359, 741)
        else:
            pass
        adb_return = click(967, 701)
    adb_return = click(1524, 671)
    return adb_return
