# -*- coding:utf-8 -*-
import sys
import threading
from time import localtime, sleep, strftime, time

import cv2

from adb import click
from group import extra, fightmod
from img import compare_image, cut_image, screenshot

BOOST = cv2.imread(sys.path[0] + '\\IMG\\boost.jpg')
END = cv2.imread(sys.path[0] + '\\IMG\\end.jpg')
FIGHT = cv2.imread(sys.path[0] + '\\IMG\\fight.jpg')
FIGHT1 = cv2.imread(sys.path[0] + '\\IMG\\fight1.jpg')
GO = cv2.imread(sys.path[0] + '\\IMG\\go.jpg')
OFFLINE = cv2.imread(sys.path[0] + '\\IMG\\offline.jpg')
FULL = cv2.imread(sys.path[0] + '\\IMG\\full.jpg')
NUMBER1 = cv2.imread(sys.path[0] + '\\IMG\\1.jpg')
NUMBER2 = cv2.imread(sys.path[0] + '\\IMG\\2.jpg')
NUMBER3 = cv2.imread(sys.path[0] + '\\IMG\\3.jpg')
NUMBER4 = cv2.imread(sys.path[0] + '\\IMG\\4.jpg')
NUMBER5 = cv2.imread(sys.path[0] + '\\IMG\\5.jpg')
img = cv2.imread(sys.path[0] + '\\IMG\\5.jpg')
STEP = 0.5

d1 = {
    1: {
        1: fightmod.mod1.fight1,
        2: fightmod.mod1.fight2,
        3: fightmod.mod1.fight3
    },
    2: {
        1: fightmod.mod2.fight1,
        2: fightmod.mod2.fight2,
        3: fightmod.mod2.fight3
    },
    3: {
        1: fightmod.mod3.fight1,
        2: fightmod.mod3.fight2,
        3: fightmod.mod3.fight3
    },
    4: {
        1: fightmod.mod4.fight1,
        2: fightmod.mod4.fight2,
        3: fightmod.mod4.fight3
    },
    5: {
        1: fightmod.mod5.fight1,
        2: fightmod.mod5.fight2,
        3: fightmod.mod5.fight3
    },
    6: {
        1: fightmod.mod6.fight1,
        2: fightmod.mod6.fight2,
        3: fightmod.mod6.fight3
    },
    7: {
        1: fightmod.mod7.fight1,
        2: fightmod.mod7.fight2,
        3: fightmod.mod7.fight3
    },
    8: {
        1: fightmod.mod8.fight1,
        2: fightmod.mod8.fight2,
        3: fightmod.mod8.fight3
    },
    9: {
        1: fightmod.mod9.fight1,
        2: fightmod.mod9.fight2,
        3: fightmod.mod9.fight3
    },
}

# # # # # # # # # # # # # # # # # # # # #  判断函数  # # # # # # # # # # # # # # # # # # #


def startfind(img=img):
    '''选关界面判断'''
    # y0   y1   x0   x1
    # 14, 50, 88, 161
    img = cut_image(14, 50, 88, 161, img)
    x = compare_image(img, FIGHT)
    x1 = compare_image(img, FIGHT1)
    if x >= 0.8:
        return True
    elif x1 >= 0.8:
        return True
    else:
        return False


def gofind(img=img):
    '''开始界面判断'''
    # y0   y1   x0   x1
    # 754, 830, 1220, 1465
    #
    img = cut_image(754, 830, 1220, 1465, img)
    x = compare_image(img, GO)
    if x >= 0.8:
        return True
    else:
        return False
    # print(x)


def boostfind(img=img):
    '''找boost'''
    # y0   y1   x0   x1
    # 753, 790, 1259, 1410
    #
    img = cut_image(753, 790, 1259, 1410, img)
    x = compare_image(img, BOOST)
    if x >= 0.7:  # boost 找到了
        return True
    else:
        return False


def endfind(img=img):
    '''结束判断'''
    # y0   y1   x0   x1
    # 158, 216, 690, 907
    #
    img1 = cut_image(158, 216, 690, 907, img)
    x = compare_image(img1, END)
    if x >= 0.5:
        return True
    else:
        return False
    # print(x)


def fullfind(img=img):
    '''残血判定'''
    # y0   y1   x0   x1
    # 140, 150, 529, 534
    #
    img = cut_image(140, 150, 529, 534, img)
    x = compare_image(img, FULL)
    if x >= 0.8:
        return True
    else:
        return False
    # print(x)


def offlinefind(img=img, flag=0):
    '''断网判定'''
    # y0   y1   x0   x1
    # 390, 485, 626, 960
    #
    img = cut_image(390, 485, 626, 960, img)
    x = compare_image(img, OFFLINE)
    if x >= 0.9:
        click(963, 632)  # 断网重连操作
        sleep(10)
        if flag == 1:
            end()


# # # # # # # # # # # # # # # # # # # # #  初级操作函数  # # # # # # # # # # # # # # # # # # #


def selection(n):
    '''选关'''
    #
    #
    #
    if n == 1:
        click(1105, 231)  # 选关1
    elif n == 2:
        click(1105, 426)  # 选关2
    elif n == 3:
        click(1105, 612)  # 选关3


def go(team):
    '''队伍选择'''
    # 判断当前队伍 计算距目标的距离
    while True:
        pic = cut_image(790, 815, 723, 743, img)
        value = None
        x = compare_image(pic, NUMBER1)
        if x > 0.8:
            value = 1 - team
        x = compare_image(pic, NUMBER2)
        if x > 0.8:
            value = 2 - team
        x = compare_image(pic, NUMBER3)
        if x > 0.93:
            value = 3 - team
        x = compare_image(pic, NUMBER4)
        if x > 0.8:
            value = 4 - team
        x = compare_image(pic, NUMBER5)
        if x > 0.8:
            value = 5 - team
        if not isinstance(value, int):
            continue
        if value == 0:
            click(1338, 796)
            return
        if value > 0:
            click(58, 534)
        else:
            click(1030, 534)


def end():
    '''结束处理'''
    click(500, 500)
    sleep(0.5)
    click(500, 500)
    sleep(0.5)
    click(500, 500)


def usegroup(fightway, wave):
    '''战斗'''
    d1[fightway][wave]()
    sleep(3)


# # # # # # # # # # # # # # # # # # # # #  中级混合函数  # # # # # # # # # # # # # # # # # # #


def select_stage(number):
    '''选关'''
    while True:
        offlinefind(img, 1)
        sleep(STEP*2)
        if startfind(img):
            selection(number)
            sleep(2)
            break


def select_team(number):
    '''选队伍和点击出发'''
    while True:
        offlinefind(img)
        sleep(STEP*2)
        if gofind(img):
            go(number)
            sleep(2)
            break


def select_notfull(abnormal):
    '''残血处理'''
    extra(abnormal)
    sleep(5)
    while True:
        if boostfind(img):
            if fullfind(img):
                # 残血打完发现现在是满血
                return 0
            else:
                # 残血打完发现现在是残血
                select_notfull(abnormal)
        elif endfind(img):
            # 残血打完发现现在是结束
            return 1
        sleep(STEP * 2)


def select_wavefight(abnormal):
    '''wave战斗选择'''
    while True:
        sleep(STEP * 3)
        offlinefind(img)
        if boostfind(img):
            if fullfind(img):
                # 满血
                return 0
            else:
                # 残血
                return select_notfull(abnormal)
        elif endfind(img):
            # 结束
            return 1


def select_bossfight(abnormal):
    '''boss战斗选择'''
    while True:
        sleep(STEP * 3)
        offlinefind(img)
        if boostfind(img):
            # 战斗
            return 0
        elif endfind(img):
            # 结束
            return 1


def wave3(normal, abnormal):
    '''三波战斗'''

    if select_wavefight(abnormal):
        return
    else:
        usegroup(normal, 1)

    if select_wavefight(abnormal):
        return
    else:
        usegroup(normal, 2)

    if select_wavefight(abnormal):
        return
    else:
        usegroup(normal, 3)

    if select_wavefight(abnormal):
        return
    else:
        print('error')


def boss(normal, abnormal):
    '''boss战斗'''
    if select_bossfight(abnormal):
        return
    else:
        usegroup(normal, 1)

    if select_bossfight(abnormal):
        return
    else:
        usegroup(normal, 2)

    if select_bossfight(abnormal):
        return
    else:
        usegroup(normal, 3)

    if select_wavefight(abnormal):
        return
    else:
        print('error')


# # # # # # # # # # # # # # # # # # # # #  子线程函数  # # # # # # # # # # # # # # # # # # # # #


class event:
    stop = threading.Event()  # 子程序结束事件


def backstage():  # 子线程
    event.stop.clear()
    sleep(2)
    while True:  # 子线程
        global img
        img = screenshot()
        sleep(STEP / 2)
        if event.stop.is_set():
            break


def substart():
    back_stage = threading.Thread(target=backstage, args=())
    back_stage.setDaemon(True)
    back_stage.start()


def substop():
    event.stop.set()


# # # # # # # # # # # # # # # # # # # # #  主函数  # # # # # # # # # # # # # # # # # # #


def action(stage, team, fightway, normal, abnormal, tim=30):
    """
    战斗主函数

    stage(关卡选择) 1 2 3

    team(队伍选择) 1 2 3 4 5

    fightway boss wave3

    normal(战斗模式选择) 1() 2(妖梦刷文文) 3(魔理沙单刷铃仙) 4(妖梦单刷铃仙) 5(HARD符卡一回合 卡2) 6(HARD符卡一回合 卡1)

    abnormal(残血模式选择) boss(跳过残血) 1(全集中) 2(全分散) 3(一半集中一半分散) 4(有什么符卡放什么)


    tim(运行时间min)

    """
    sleep(3)
    start = int(time())  # 开始计时
    while True:
        print(strftime("%H:%M:%S", localtime()))
        stop = int(time())  # 结束计时
        if stop - start > 60 * tim:
            print('break')
            break

        select_stage(stage)  # 选关
        select_team(team)  # 选队伍
        fightway(normal, abnormal)  # 战斗
        end()  # 结束

        endtime = int(time())
        print(endtime - stop, 's')


if __name__ == "__main__":
    pass
