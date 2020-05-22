# -*- coding:utf-8 -*-
import sys
import threading
import time
from group import extra, fightmod

import cv2

from img import cut_image, compare_image, screenshot
from adb import click


class event:
    flag = threading.Event()  # 子程序开关
    end = threading.Event()  # 子程序结束主程序开始事件
    stop = threading.Event()  # 子程序结束事件

    class fight:  # 战斗子程序事件
        flag = threading.Event()  # 战斗类事件筛选
        end = threading.Event()  # 子程序完成事件
        boost = threading.Event()  # boost事件
        full = threading.Event()  # 满血事件

    class select:  # 选择子程序事件
        flag = threading.Event()  # 选择类事件筛选
        start = threading.Event()  # 开始界面事件
        go = threading.Event()  # 出发界面事件


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
img = None
STEP = 0.2


def startfind(img):
    '''选关界面判断'''
    # y0   y1   x0   x1
    # 14, 50, 88, 161
    img = cut_image(14, 50, 88, 161, img)
    x = compare_image(img, FIGHT)
    x1 = compare_image(img, FIGHT1)
    if x >= 0.8:
        event.select.start.set()
        return True
    elif x1 >= 0.8:
        event.select.start.set()
        return True
    else:
        event.select.start.clear()
        return False
    # print(x)


def gofind(img):
    '''开始界面判断'''
    # y0   y1   x0   x1
    # 754, 830, 1220, 1465
    #
    img = screenshot()
    img = cut_image(754, 830, 1220, 1465, img)
    x = compare_image(img, GO)
    if x >= 0.8:
        event.select.go.set()
        return True
    else:
        event.select.go.clear()
        return False
    # print(x)


def boostfind(img):
    '''找boost'''
    # y0   y1   x0   x1
    # 753, 790, 1259, 1410
    #
    img = cut_image(753, 790, 1259, 1410, img)
    x = compare_image(img, BOOST)
    if x >= 0.7:  # boost 找到了
        event.fight.boost.set()
        return True
    else:
        event.fight.boost.clear()
        return False
    # print(x)


def endfind(img):
    '''结束判断'''
    # y0   y1   x0   x1
    # 158, 216, 690, 907
    #
    img = cut_image(158, 216, 690, 907, img)
    # cv2.imwrite('x.jpg', img)
    x = compare_image(img, END)
    if x >= 0.5:
        event.fight.end.set()
        return True
    else:
        event.fight.end.clear()
        return False
    # print(x)


def fullfind(img):
    '''残血判定'''
    # y0   y1   x0   x1
    # 140, 150, 529, 534
    #
    img = cut_image(140, 150, 529, 534, img)
    x = compare_image(img, FULL)
    if x >= 0.8:
        event.fight.full.set()
        return True
    else:
        event.fight.full.clear()
        return False
    # print(x)


def offlinefind(img):
    '''断网判定'''
    # y0   y1   x0   x1
    # 390, 485, 626, 960
    #
    img = cut_image(390, 485, 626, 960, img)
    x = compare_image(img, OFFLINE)
    if x >= 0.9:
        click(963, 632)  # 断网重连操作
        time.sleep(10)
        offlinefind(img)


def backstage():  # 子线程
    event.fight.boost.clear()
    event.fight.full.clear()
    event.fight.end.clear()
    event.select.start.clear()
    event.select.go.clear()
    event.stop.clear()
    event.flag.clear()
    event.select.flag.clear()
    event.fight.flag.clear()
    time.sleep(2)
    while True:  # 子线程
        event.flag.wait()  # 等待后台允许事件
        global img
        img = screenshot()
        if event.select.flag.is_set():  # 选择类事件检测
            offlinefind(img)
            startfind(img)
            gofind(img)
        if event.fight.flag.is_set():  # 战斗类事件检测
            offlinefind(img)
            boostfind(img)
            fullfind(img)
            endfind(img)
            if event.fight.boost.is_set():
                event.end.set()
            elif event.fight.end.is_set():
                event.end.set()
            else:
                event.end.clear()
        time.sleep(0.2)
        if event.stop.is_set():
            break


def actionextra(s):
    '''战斗判断函数'''
    time.sleep(3)
    event.flag.set()  # 开始子线程
    event.end.wait(timeout=None)  # 等待后台发出开始命令
    event.end.clear()
    event.flag.clear()  # 停止子线程，开始判断
    if event.fight.boost.is_set():  # 有boost
        if event.fight.full.is_set():  # 满血返回1
            return 1
        if not event.fight.full.is_set():  # 残血
            # boss模式残血视为满血继续下一波
            if s == 'boss':
                return 1
            extra(s)
            event.fight.boost.clear()
            x = actionextra(s)
            return x
    if event.fight.end.is_set():  # 结束返回0
        return 0


def end():
    '''结束处理'''
    # print('end')
    click(500, 500)
    time.sleep(0.5)
    click(500, 500)
    time.sleep(0.5)
    click(500, 500)
    event.fight.flag.clear()  # 战斗事件结束
    event.fight.end.clear()
    event.fight.boost.clear()
    event.fight.full.clear()


def actionselect(n, team):
    '''关卡选择函数'''
    event.flag.set()  # 开始子线程
    event.select.start.wait()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    selection(n)  # 选择内容函数

    event.select.go.wait()

    # 队伍选择点出发
    go(team)

    event.flag.clear()  # 结束子线程


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
        time.sleep(2)


def substart():
    back_stage = threading.Thread(target=backstage, args=())
    back_stage.setDaemon(True)
    back_stage.start()


def substop():
    event.stop.set()


def action(n, style, s, team=0, tim=30):
    """
    战斗主函数

    n(关卡选择) = 1 2 3

    style(战斗模式选择) = 1() 2(妖梦刷文文) 3(魔理沙单刷铃仙) 4(妖梦单刷铃仙) 5(HARD符卡一回合 卡2) 6(HARD符卡一回合 卡1)

    s(残血模式选择) =  boss(跳过残血) 1(全集中) 2(全分散) 3(一半集中一半分散) 4(有什么符卡放什么)

    team(队伍选择)

    tim(运行时间min)

    """
    start = time.time()  # 开始计时
    while True:
        stop = time.time()  # 结束计时
        if stop - start > 60 * tim:
            print('break')
            break

        event.select.flag.set()  # 选择事件开始
        actionselect(n, team)  # 选择
        event.select.flag.clear()  # 选择事件结束

        event.fight.flag.set()  # 战斗事件开始
        if actionextra(s):
            fight1(style)  # 操作1
        else:
            end()
            continue
        if actionextra(s):
            fight2(style)  # 操作2
        else:
            print("WAVE 1")
            end()
            continue
        if actionextra(s):
            fight3(style)  # 操作3
        else:
            print("WAVE 2")
            end()
            continue
        if actionextra(s):
            actionextra(4)
            print('end error')
            end()
            continue
        else:
            print("WAVE 3")
            end()
            continue


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


# 战斗选择字典
d = {
    1: fightmod.mod1,
    2: fightmod.mod2,
    3: fightmod.mod3,
    4: fightmod.mod4,
    5: fightmod.mod5,
    6: fightmod.mod6,
    7: fightmod.mod7,
    8: fightmod.mod8,
    9: fightmod.mod9,
}


# 第一波战斗
def fight1(style):
    # print("WAVE 1")
    d[style].fight1()


# 第二波战斗
def fight2(style):
    # print("WAVE 2")
    d[style].fight2()


# 第三波战斗
def fight3(style):
    # print("WAVE 3")
    d[style].fight3()


if __name__ == "__main__":
    pass
