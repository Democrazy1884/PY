# -*- coding:utf-8 -*-
import os
import sys

from time import localtime, sleep, strftime, time
from gameerror import OvertimeError
import cv2
from sub import get_img
from adb import click  # , swipe
from group import extra, fightmod
from image import compare_image, cut_image, mathc_img
BOOST = cv2.imread(sys.path[0] + '\\IMG\\boost.jpg')  # 战斗判断用 boost
END = cv2.imread(sys.path[0] + '\\IMG\\end.jpg')  # 战斗结束
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
STEP = 0.2
d1 = {
    1: {
        0: fightmod.mod1,
        1: fightmod.mod1.fight1,
        2: fightmod.mod1.fight2,
        3: fightmod.mod1.fight3,
    },
    2: {
        0: fightmod.mod2,
        1: fightmod.mod2.fight1,
        2: fightmod.mod2.fight2,
        3: fightmod.mod2.fight3,
    },
    3: {
        0: fightmod.mod3,
        1: fightmod.mod3.fight1,
        2: fightmod.mod3.fight2,
        3: fightmod.mod3.fight3,
    },
    4: {
        0: fightmod.mod4,
        1: fightmod.mod4.fight1,
        2: fightmod.mod4.fight2,
        3: fightmod.mod4.fight3,
    },
    5: {
        0: fightmod.mod5,
        1: fightmod.mod5.fight1,
        2: fightmod.mod5.fight2,
        3: fightmod.mod5.fight3,
    },
    6: {
        0: fightmod.mod6,
        1: fightmod.mod6.fight1,
        2: fightmod.mod6.fight2,
        3: fightmod.mod6.fight3,
    },
    7: {
        0: fightmod.mod7,
        1: fightmod.mod7.fight1,
        2: fightmod.mod7.fight2,
        3: fightmod.mod7.fight3,
    },
    8: {
        0: fightmod.mod8,
        1: fightmod.mod8.fight1,
        2: fightmod.mod8.fight2,
        3: fightmod.mod8.fight3,
    },
    9: {
        0: fightmod.mod9,
        1: fightmod.mod9.fight1,
        2: fightmod.mod9.fight2,
        3: fightmod.mod9.fight3,
    },
}


# # # # # # # # # # # # # # # # # # # # #  判断函数  # # # # # # # # # # # # # # # # # # #


def startfind():
    '''选关界面判断'''
    # y0   y1   x0   x1
    # 14, 50, 88, 161
    img = cut_image(14, 50, 88, 161, get_img())
    x = compare_image(img, FIGHT)
    x1 = compare_image(img, FIGHT1)
    if x >= 0.8:
        return True
    elif x1 >= 0.8:
        return True
    else:
        return False


def gofind():
    '''选关开始界面判断'''
    # y0   y1   x0   x1
    # 754, 830, 1220, 1465
    #
    img = cut_image(754, 830, 1220, 1465, get_img())
    x = compare_image(img, GO)
    if x >= 0.8:
        return True
    else:
        return False
    # print(x)


def boostfind():
    '''找boost'''
    # y0   y1   x0   x1
    # 753, 790, 1259, 1410
    #
    img = cut_image(753, 790, 1259, 1410, get_img())
    x = compare_image(img, BOOST)
    if x >= 0.7:  # boost 找到了
        return True
    else:
        return False


def endfind():
    '''战斗结束判断'''
    # y0   y1   x0   x1
    # 158, 216, 690, 907
    #
    img = cut_image(158, 216, 690, 907, get_img())
    x = compare_image(img, END)
    # print(x)
    if x >= 0.4:
        return True
    else:
        return False
    # print(x)


def fullfind():
    '''残血判定'''
    # y0   y1   x0   x1
    # 140, 150, 529, 534
    #
    img = cut_image(140, 150, 529, 534, get_img())
    x = compare_image(img, FULL)
    if x >= 0.8:
        return True
    else:
        return False
    # print(x)


def offlinefind(flag=0):
    '''断网判定'''
    # y0   y1   x0   x1
    # 390, 485, 626, 960
    #
    img = cut_image(390, 485, 626, 960, get_img())
    x = compare_image(img, OFFLINE)
    if x >= 0.9:
        print('offline')
        sleep(10)
        click(963, 632)  # 断网重连操作
        sleep(10)
        if flag == 1:
            end()
        return True
    else:
        return False


# # # # # # # # # # # # # # # # # # # # #  初级操作函数  # # # # # # # # # # # # # # # # # # #


def selection(n):
    '''选关'''
    #
    #
    #
    if isinstance(n, int):
        if n == 1:
            click(1105, 231)  # 选关1
        elif n == 2:
            click(1105, 426)  # 选关2
        elif n == 3:
            click(1105, 612)  # 选关3
    else:
        x, y = mathc_img(get_img(), n, 0.9)
        if x:
            click(x[0], y[0])
        else:  # 没找到目标，去重新选择
            pass


def go(team):
    '''队伍选择'''
    # 判断当前队伍 计算距目标的距离
    start = time()
    while True:
        if time() - start > 60:
            raise OvertimeError('go')
        pic = cut_image(790, 815, 723, 743, get_img())
        x = []
        x.append(compare_image(pic, NUMBER1))
        x.append(compare_image(pic, NUMBER2))
        x.append(compare_image(pic, NUMBER3))
        x.append(compare_image(pic, NUMBER4))
        x.append(compare_image(pic, NUMBER5))
        value = x.index(max(x)) + 1 - team
        if value == 0:
            click(1338, 796)
            return
        elif value > 0:
            click(58, 534)
        else:
            click(1030, 534)
        sleep(2)


def end():
    '''结束处理'''
    click(500, 500)
    sleep(0.5)
    click(500, 500)
    sleep(0.5)
    click(500, 500)


def usegroup(fightway, wave):
    '''战斗'''
    extra_way = d1[fightway][wave]()
    sleep(3)
    return extra_way


# # # # # # # # # # # # # # # # # # # # #  中级混合函数  # # # # # # # # # # # # # # # # # # #


def select_stage(number):
    '''选关'''
    start = time()
    while True:
        if time() - start > 60:
            raise OvertimeError('stage')
        offlinefind(1)
        sleep(STEP*2)
        if startfind():
            selection(number)
            sleep(2)
            break


def select_team(number):
    '''选队伍和点击出发'''
    start = time()
    while True:
        if time() - start > 60:
            raise OvertimeError('team')
        offlinefind()
        sleep(STEP*2)
        if gofind():
            go(number)
            sleep(2)
            break


def select_notfull(abnormal=0):
    '''残血处理'''
    next_abnormal = extra(abnormal)
    sleep(5)
    start = time()
    while True:
        if time() - start > 30:
            raise OvertimeError('notfull')
        if boostfind():
            if fullfind():
                # 残血打完发现现在是满血
                return 0
            else:
                # 残血打完发现现在是残血
                if next_abnormal:
                    select_notfull(next_abnormal)
                else:
                    select_notfull(abnormal)
        elif endfind():
            # 残血打完发现现在是结束
            return 1
        sleep(STEP * 2)


def select_wavefight(abnormal=0):
    '''wave战斗选择'''
    start = time()
    while True:
        if time() - start > 60:
            raise OvertimeError('wavefight')
        sleep(STEP * 2)
        offlinefind()
        if boostfind():
            if fullfind():
                # 满血
                return 0
            else:
                # 残血
                return select_notfull(abnormal)
        elif endfind():
            # 结束
            return 1


def select_bossfight(abnormal):
    '''boss战斗选择'''
    start = time()
    while True:
        if time() - start > 60:
            raise OvertimeError('bossfight')
        sleep(STEP * 2)
        offlinefind()
        if boostfind():
            # 战斗
            return 0
        elif endfind():
            # 结束
            return 1


def wave3(normal):
    '''三波战斗'''

    if select_wavefight():
        return
    else:
        abnormal = usegroup(normal, 1)

    if select_wavefight(abnormal):
        return
    else:
        abnormal = usegroup(normal, 2)

    if select_wavefight(abnormal):
        return
    else:
        abnormal = usegroup(normal, 3)

    if select_wavefight(abnormal):
        return
    else:
        print('error')


def boss(normal):
    '''boss战斗'''
    if select_bossfight(1):
        return
    else:
        abnormal = usegroup(normal, 1)

    if select_bossfight(abnormal):
        return
    else:
        abnormal = usegroup(normal, 2)

    if select_bossfight(abnormal):
        return
    else:
        abnormal = usegroup(normal, 3)

    if select_wavefight(abnormal):
        return
    else:
        print('error')


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def restart_game():
    start = time()
    while True:
        if time() - start > 120:
            restart_program()
        if startfind():
            break
        elif offlinefind():
            pass
        elif boostfind():
            click(858, 34)  # 强行中断战斗
            sleep(2)
            click(1408, 808)
            click(992, 628)
        elif endfind():
            end()
        elif gofind():
            click(48, 48)
        click(500, 500)
        sleep(5)
# # # # # # # # # # # # # # # # # # # # #  主函数  # # # # # # # # # # # # # # # # # # #


def action(stage, team, normal, tim=30):
    """
    战斗主函数

    stage(关卡选择) 1 2 3

    team(队伍选择) 1 2 3 4 5

    fightway boss wave3

    normal(战斗模式选择)

    abnormal(残血模式选择)


    tim(运行时间min)

    """
    sleep(3)
    start = int(time())  # 开始计时
    fightway = d1[normal][0].mode()
    if fightway == 'boss':
        fightway = boss
    if fightway == 'wave3':
        fightway = wave3
    print(fightway)
    while True:
        stop = int(time())  # 结束计时
        if stop - start > 60 * tim:
            print('break at ' + strftime("%H:%M:%S", localtime()))
            sleep(3)
            return stop - start
        try:
            print('start at ' + strftime("%H:%M:%S", localtime()))
            # print(strftime("%H:%M:%S", localtime()))
            select_stage(stage)  # 选关
            # print('team')
            select_team(team)  # 选队伍
            # print('fight')
            fightway(normal)  # 战斗
            # print('end')
            end()  # 结束

            endtime = int(time())
            print('time use:'+str(endtime - stop)+'s')

        except OvertimeError as err:
            print(err.type)
            restart_game()
            # 返回起点


class Fight():
    def __init__(self):
        self.time

    def run(self: int, stage: int, team: int, fightway, normal: int, tim=30):
        action(stage, team, fightway, normal, tim)


if __name__ == "__main__":
    pass
