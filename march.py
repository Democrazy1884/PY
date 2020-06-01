# -*- coding:utf-8 -*-
import sys
from time import sleep, time

import cv2
from adb import click, swipe, click_s
from image import compare_image, cut_image, mathc_img
from sub import get_img
from gameerror import OvertimeError
LV = cv2.imread(sys.path[0] + '\\IMG\\lv.jpg', 0)  # 远征检测
MARCHPAGE = cv2.imread(sys.path[0] + '\\IMG\\marchpage.jpg')
DONE = cv2.imread(sys.path[0] + '\\IMG\\done.jpg', 0)  # 远征完成
WORKING = cv2.imread(sys.path[0] + '\\IMG\\working.jpg', 0)  # 远征中
YES = cv2.imread(sys.path[0] + '\\IMG\\yes.jpg', 0)  # 决定
ADD = cv2.imread(sys.path[0] + '\\IMG\\add.jpg', 0)  # 远征加人物

BOOK = cv2.imread(sys.path[0] + '\\IMG\\l1.jpg', 0)
GOLD1 = cv2.imread(sys.path[0] + '\\IMG\\l2.jpg', 0)
CARD = cv2.imread(sys.path[0] + '\\IMG\\l3.jpg', 0)
POWER = cv2.imread(sys.path[0] + '\\IMG\\l4.jpg', 0)
GOLD2 = cv2.imread(sys.path[0] + '\\IMG\\l5.jpg', 0)

ADDGIRL = cv2.imread(sys.path[0] + '\\IMG\\addgirl.jpg', 0)
M3 = cv2.imread(sys.path[0] + '\\IMG\\3m.jpg')
MARCHDONE = cv2.imread(sys.path[0] + '\\IMG\\marchdone.jpg', 0)
STEP = 0.2

OFFLINE = cv2.imread(sys.path[0] + '\\IMG\\offline.jpg')


def offlinefind(get_img=get_img):
    '''断网判定'''
    # y0   y1   x0   x1
    # 390, 485, 626, 960
    #
    img = cut_image(390, 485, 626, 960, get_img())
    x = compare_image(img, OFFLINE)
    if x >= 0.9:
        click(963, 632)  # 断网重连操作
        print('offline')
        sleep(10)
        return True
    return False


FIRST = cv2.imread(sys.path[0] + '\\IMG\\first.jpg')  # 开始界面


def firstpagefind(get_img=get_img):
    '''初始界面判断'''
    img = cut_image(839, 884, 12, 774, get_img())
    x = compare_image(img, FIRST)
    if x > 0.5:
        return True
    else:
        return False


def marchfind(get_img=get_img):
    '''远征界面判断'''
    img = cut_image(13, 48, 89, 231, get_img())  # 远征判断
    x = compare_image(img, MARCHPAGE)
    if x > 0.8:
        return True
    else:
        return False


MARCH = cv2.imread(sys.path[0] + '\\IMG\\march.jpg')  # 远征红点


def mainpage_marchfind(get_img=get_img):
    '''主界面远征判断'''
    img = cut_image(480, 502, 1415, 1445, get_img())  # 远征判断
    x = compare_image(img, MARCH)
    if x > 0.8:
        return True
    else:
        return False


MAIN = cv2.imread(sys.path[0] + '\\IMG\\main.jpg')  # 主界面


def mainpagefind(get_img=get_img):
    '''主界面判断'''
    img = cut_image(696, 737, 1424, 1521, get_img())
    x = compare_image(img, MAIN)
    if x > 0.8:
        return True
    else:
        return False


class March():
    '''远征类'''

    def __init__(self, img, number):
        '''初始化远征

        :img:远征的小图
        :number:远征编号
        :mode: 模式 材料、灵力、钱、两种结晶
        :name: 远征名字，选择合适队员用
        :situation: 情况 进行中 结束 可用
        '''
        # cv2.imwrite('march%d.jpg' % number, img)
        self.img = img
        self.number = number
        self.mode = March.get_mode(img)
        self.name = March.get_name(img)
        self.situation = self.get_situation(img)
        # print(number, self.mode, self.situation)

    def remove_same(x: list, y: list):
        '''删除坐标list中的相似值'''
        new_x = []
        new_y = []
        for num in range(0, len(x)):
            if num != 0:
                if abs(x[num] - x[num - 1]) > 20 or abs(y[num] - y[num - 1]) > 20:
                    new_x.append(x[num])
                    new_y.append(y[num])
            else:
                new_x.append(x[num])
                new_y.append(y[num])
        return new_x, new_y

    def get_mode(img):
        '''获取类别'''
        x, y = mathc_img(img, BOOK, 0.8)
        x, y = March.remove_same(x, y)
        # print(x)
        string = 'nothing'
        if x:
            string = 'book'  # 指南书
        x, y = mathc_img(img, GOLD1, 0.9)
        x, y = March.remove_same(x, y)
        # print(x)
        if x:
            string = 'gold1'  # 封结晶
        x, y = mathc_img(img, GOLD2, 0.9)
        x, y = March.remove_same(x, y)
        # print(x)
        if x:
            string = 'gold2'  # 神结晶
        x, y = mathc_img(img, CARD, 0.8)
        x, y = March.remove_same(x, y)
        # print(x)
        if x:
            string = 'card'  # 绘扎
        x, y = mathc_img(img, POWER, 0.8)
        x, y = March.remove_same(x, y)
        # print(x)
        if x:
            string = 'power'  # 灵力
        return string

    def get_name(img):
        '''获取名字'''
        return 1

    def get_situation(self, img):
        '''获取状态'''
        x1, y1 = mathc_img(img, DONE, 0.9)
        x2, y2 = mathc_img(img, WORKING, 0.9)
        if x1:
            return 'done'  # 状态为完成
        elif x2:
            return 'doing'  # 状态为进行中
        else:
            return 'available'  # 状态为可选

    def cut(img):
        '''切出每个远征的小图'''
        # 找到所以基准点
        x, y = mathc_img(img, LV, 0.7)
        x, y = March.remove_same(x, y)
        # 图片切片
        piclist = []
        for num in range(0, len(x)):
            y0 = y[num] - 34
            y1 = y[num] + 186
            x0 = x[num] - 296
            x1 = x[num] + 907
            piclist.append(cut_image(y0, y1, x0, x1, img))
        return piclist

    def down_swipe():
        '''下滑'''
        swipe(1557, 261, 1560, 615, 200)
        sleep(1)

    def up_swipe():
        '''上滑'''
        swipe(1560, 615, 1557, 261, 200)
        sleep(1)

    @classmethod
    def initialize(cls, get_img=get_img):
        '''初始化

        需要处在远征界面
        '''
        # 普通远征
        click(73, 179)
        March.up_swipe()
        sleep(1)
        piclist = March.cut(get_img())
        piclist.pop()
        March.down_swipe()

        sleep(1)
        pic2list = March.cut(get_img())
        pic2list.pop(0)
        piclist = piclist + pic2list
        sleep(1)
        march_list = []
        for number in range(0, 5):
            march_list.append(cls(piclist[number], number))
        # 特殊远征
        click(73, 329)
        sleep(1)
        March.up_swipe()
        sleep(1)
        piclist = March.cut(get_img())
        if piclist:
            if len(piclist) <= 3:
                for number in range(0, len(piclist)):
                    march_list.append(cls(piclist[number], number + 5))
            else:
                piclist = piclist[:3]
                March.down_swipe()

                sleep(1)
                pic2list = March.cut(get_img())
                piclist = piclist + pic2list
                for number in range(0, len(piclist)):
                    march_list.append(cls(piclist[number], number + 8))
        return march_list

    def receive_done_sub(get_img=get_img):
        '''收远征完成'''
        sleep(1)
        for num in range(0, 3):
            # 找完成的远征
            x, y = mathc_img(get_img(), DONE, 0.9)
            x, y = March.remove_same(x, y)
            # 找到可以收的远征
            if x:
                click(x[0], y[0])
                x = []
                y = []
                sleep(1)
                # 找MARCHDONE
                start = time()
                while True:
                    if time() - start > 60:
                        raise OvertimeError('receive1')
                    x, y = mathc_img(get_img(), MARCHDONE, 0.9)
                    if x:
                        x = []
                        y = []
                        break
                    sleep(STEP * 2)
                # 在回到远征界面前一直点
                start = time()
                while True:
                    if time() - start > 60:
                        raise OvertimeError('receive2')
                    if marchfind():
                        break
                    click(792, 818)
                    sleep(2)
            else:
                # 没远征可收
                print('Nope')
                return

    def receive_done_main():
        '''收远征'''
        sleep(5)
        March.receive_done_sub()
        March.down_swipe()
        March.receive_done_sub()
        click(73, 329)
        March.receive_done_sub()
        March.down_swipe()
        March.receive_done_sub()

    def go():
        '''进入远征界面'''
        click(1387, 543)
        sleep(3)
        start = time()
        while True:
            if time() - start > 60:
                raise OvertimeError('go')
            marchfind()
            offlinefind()
            if marchfind():
                break
            sleep(STEP * 2)

    def exit():
        '''返回主界面'''
        click_s(1559, 35)
        start = time()
        while True:
            if time() - start > 60:
                raise OvertimeError('exit')
            offlinefind()
            if mainpagefind():
                break
            if time() - start > 20:
                click_s(1559, 35)
                start = time()
            sleep(STEP * 2)

    def select_player():
        # 选人
        start = time()
        while True:
            if time() - start > 60:
                raise OvertimeError('select_player1')
            x, y = mathc_img(get_img(), ADDGIRL, 0.8)
            x, y = March.remove_same(x, y)
            if x:
                click(x[0], y[0])
                break
        # 确定
        start = time()
        while True:
            if time() - start > 60:
                raise OvertimeError('select_player2')
            x, y = mathc_img(get_img(), YES, 0.8)
            x, y = March.remove_same(x, y)
            if x:
                click(x[0], y[0])
                break
        sleep(2)
        click(75, 186)
        March.up_swipe()

    def send_done(march):
        '''做远征'''
        num = march.number+1
        click(75, 186)
        March.up_swipe()
        if num == 1:
            click(576, 207)
        elif num == 2:
            click(560, 440)
        elif num == 3:
            click(599, 666)
        elif num == 4:
            March.down_swipe()
            click(846, 520)
        elif num == 5:
            March.down_swipe()
            click(866, 762)
        elif num == 6:
            click(72, 336)
            click(576, 207)
        elif num == 7:
            click(72, 336)
            click(560, 440)
        elif num == 8:
            click(72, 336)
            click(599, 666)
        elif num == 9:
            click(72, 336)
            March.down_swipe()
            click(846, 520)
        elif num == 10:
            click(72, 336)
            March.down_swipe()
            click(866, 762)
        March.select_player()

    def fullfind():
        '''三个远征满了判断'''
        img = cut_image(815, 853, 113, 197, get_img())
        x = compare_image(img, M3)
        # print(x)
        if x > 0.8:
            return True
        else:
            return False

    def send(available_list, modelist):
        '''发远征'''
        # 反转list
        available_list.reverse()
        # 按模式list的顺序发远征
        for string in modelist:
            # 按先限时后普通的顺序选择远征
            for march in available_list:
                # 三个远征满了就返回
                if March.fullfind():
                    return
                # march 必须为可用 且为当前选择的mode
                if march.situation == 'available' and string in march.mode:
                    March.send_done(march)
                    march.situation = 'doing'
                sleep(1)

    def receive():
        March.exit()
        March.go()
        March.receive_done_main()

    def start():
        '''远征全家桶'''
        try:
            print('march start')
            March.exit()
            # 收远征
            March.receive()
            # 初始化
            march_list = March.initialize()
            # 远征优先级
            modelist = ['gold2', 'gold1', 'power', 'card', 'book', 'nothing']
            # 做远征
            March.send(march_list, modelist)
            print('march done')
            March.exit()

            click(1472, 717)
            sleep(3)
        except OvertimeError as err:
            print(err.type)
            March.start()
