# -*- coding:utf-8 -*-
from time import sleep, time

import core.game_log as game_log
from core.adb import click, click_s, swipe
from core.gameerror import OvertimeError
from core.image import cut_image, mathc_img
from core.sub import Sub, get_img
from core.universe import remove_same, search

STEP = 0.5


def offlinefind(img=get_img):
    """断网判定"""
    if search("OFFLINE"):
        click(963, 632)  # 断网重连操作
        game_log.warning("offline")
        sleep(10)
        return True
    else:
        return False


def firstpagefind(img=get_img):
    "初始界面判断"
    return search("FIRST")


def marchfind(img=get_img):
    """远征界面判断"""
    return search("MARCHPAGE")


def mainpage_marchfind(img=get_img):
    """主界面远征判断"""
    return search("MARCH")


def mainpagefind(img=get_img):
    """主界面判断"""
    return search("MAIN")


def mainpage_buildingfind(img=get_img):
    """设施红点判断"""
    return search("BUILDING")


def mainpage_building_skill_room_point(img=get_img):
    """道场红点判断"""
    return search("SKILLROOM")


def fullfind(img=get_img):
    """三个远征满了判断"""
    return search("M3")


def number_find(img=get_img):
    """远征个数判断"""
    if search("TEAM4"):
        return 4
    elif search("TEAM5"):
        return 5
    else:
        up_swipe()
        return number_find()


def skill_room():
    """道场续书"""
    # 设施有红点吗
    if not mainpage_buildingfind():
        return
    click(800, 800, 3)
    # 道场有红点吗
    if not mainpage_building_skill_room_point():
        click(792, 772)
        return
    click(1316, 464)
    start = time()
    num = 0
    while 1:
        sleep(5)
        if time() - start > 60:
            break
            raise OvertimeError("skill_room")
        # 道场技能150
        point = mathc_img(get_img(), "EXP", 0.8)
        point = remove_same(point)
        if point:
            for p in point:
                if p[0] > 800:
                    point.remove(p)
            # print(point)
            click(int(point[1][0]), int(point[1][1] + 50), 1)  # 银书
            click(1322, 764, 1)
            click(992, 632, 1)
            num += 1
            continue
        #  道场确定
        point = mathc_img(get_img(), "SKILLPOINT", 0.9)
        if point:
            point = remove_same(point)
            click(point[0])
            continue
        if num == 3:
            break
    exit_to_main()


def down_swipe():
    """下滑"""
    swipe(1557, 261, 1560, 615, 200)
    sleep(2)
    swipe(1557, 261, 1560, 615, 200)
    sleep(2)


def up_swipe():
    """上滑"""
    swipe(1560, 615, 1557, 261, 200)
    sleep(2)
    swipe(1560, 615, 1557, 261, 200)
    sleep(2)


def go_to_march():
    """进入远征界面"""
    click(1387, 543)
    sleep(3)
    start = time()
    while 1:
        if time() - start > 60:
            raise OvertimeError("go")
        marchfind()
        offlinefind()
        if marchfind():
            break
        sleep(STEP * 2)


def exit_to_main():
    """返回主界面"""
    click_s(1559, 35)
    start = time()
    while 1:
        if time() - start > 60:
            raise OvertimeError("exit")
        offlinefind()
        if mainpagefind():
            break
        if time() - start > 10:
            click_s(1559, 35)
            sleep(5)
        sleep(STEP * 2)


class March:
    """远征类"""

    def __init__(self, img, number):
        """初始化远征

        :img:远征的小图
        :number:远征编号
        :mode: 模式 材料、灵力、钱、两种结晶
        :name: 远征名字，选择合适队员用
        :situation: 情况 进行中 结束 可用
        """

        def get_mode(img):
            """获取类别"""
            point = mathc_img(img, "BOOK", 0.8)
            point = remove_same(point)
            # print(x)
            string = "nothing"
            if point:
                string = "book"  # 指南书
            point = mathc_img(img, "GOLD1", 0.9)
            point = remove_same(point)
            # print(x)
            if point:
                string = "gold1"  # 封结晶
            point = mathc_img(img, "GOLD2", 0.9)
            point = remove_same(point)
            # print(x)
            if point:
                string = "gold2"  # 神结晶
            point = mathc_img(img, "CARD", 0.8)
            point = remove_same(point)
            # print(x)
            if point:
                string = "card"  # 绘扎
            point = mathc_img(img, "POWER", 0.8)
            point = remove_same(point)
            # print(x)
            if point:
                string = "power"  # 灵力
            return string

        def get_name(img):
            """获取名字"""
            return 1

        def get_situation(img):
            """获取状态"""
            point1 = mathc_img(img, "DONE", 0.9)
            point2 = mathc_img(img, "WORKING", 0.9)
            if point1:
                return "done"  # 状态为完成
            elif point2:
                return "doing"  # 状态为进行中
            else:
                return "available"  # 状态为可选

        # cv2.imwrite("march%d.jpg" % number, img)
        self.img = img
        self.number = number
        self.mode = get_mode(img)
        self.name = get_name(img)
        self.situation = get_situation(img)
        # print(number, self.mode, self.situation)

    @classmethod
    def initialize(cls, get_img=get_img):
        """初始化

        需要处在远征界面
        """

        def cut(img):
            """切出每个远征的小图"""
            # 找到所以基准点
            point = mathc_img(img, "LV", 0.7)
            point = remove_same(point)
            # 图片切片
            piclist = []
            for num in range(0, len(point)):
                y0 = point[num][1] - 34
                y1 = point[num][1] + 186
                x0 = point[num][0] - 296
                x1 = point[num][0] + 907
                piclist.append(cut_image(y0, y1, x0, x1, img))
            return piclist

        # 普通远征
        click(73, 179)
        up_swipe()
        sleep(1)
        piclist = cut(get_img())
        piclist.pop()
        down_swipe()

        sleep(1)
        pic2list = cut(get_img())
        pic2list.pop(0)
        piclist = piclist + pic2list
        sleep(1)
        march_list = []
        for number in range(0, 5):
            march_list.append(cls(piclist[number], number))
        # 特殊远征
        click(73, 329)
        sleep(1)
        up_swipe()
        sleep(1)
        piclist = cut(get_img())
        if piclist:
            # 限时远征少于3个，一次搞定
            if len(piclist) <= 3:
                for number in range(0, len(piclist)):
                    march_list.append(cls(piclist[number], number + 5))
            # 限时远征多于3个
            else:
                # 限时远征个数判断
                n = number_find()
                piclist.pop()
                down_swipe()
                sleep(1)
                pic2list = cut(get_img())
                if n == 5:
                    pic2list.pop(0)
                if n == 4:
                    pic2list.pop(0)
                    pic2list.pop(0)
                piclist = piclist + pic2list
                for number in range(0, len(piclist)):
                    march_list.append(cls(piclist[number], number + 5))
        return march_list[0:9]


class March_action:
    "远征操作"

    def __init__(self, skill=True, receive=True, send=True):
        self.skill_room = skill
        self.receive_march = receive
        self.send_march = send

    @classmethod
    def only_skill(cls):
        """只续技能书"""
        return cls(1, 0, 0)

    @classmethod
    def only_receive(cls):
        """只收远征"""
        return cls(0, 1, 0)

    @classmethod
    def only_send(cls):
        """只发远征"""
        return cls(0, 0, 1)

    def send(self, available_list, modelist):
        """发远征"""

        def select_player():
            # 选人
            start = time()
            while 1:
                if time() - start > 60:
                    raise OvertimeError("select_player1")
                sleep(2)
                point = mathc_img(get_img(), "ADDGIRL", 0.8)
                point = remove_same(point)
                if point:
                    click(point[0])
                    break
            # 确定
            start = time()
            while 1:
                if time() - start > 60:
                    raise OvertimeError("select_player2")
                point = mathc_img(get_img(), "YES", 0.8)
                point = remove_same(point)
                if point:
                    click(point[0])
                    break
            sleep(2)
            click(75, 186)
            up_swipe()

        def send_done(march):
            """做远征"""
            num = march.number + 1
            # print(num)
            click(75, 186)
            up_swipe()
            # 普通远征
            if num == 1:
                click(576, 207)
                return
            elif num == 2:
                click(560, 440)
                return
            elif num == 3:
                click(599, 666)
                return
            else:
                down_swipe()
            if num == 4:
                click(846, 520)
                return
            elif num == 5:
                click(866, 762)
                return
            # 限时远征 前三个
            else:
                click(72, 336)
            if num == 6:
                click(576, 207)
                return
            elif num == 7:
                click(560, 440)
                return
            elif num == 8:
                click(599, 666)
                return
            else:
                down_swipe()
            # 限时远征 后三个
            if num == 9:
                click(570, 306)
                return
            elif num == 10:
                click(600, 540)
                return
            elif num == 11:
                click(756, 770)
                return

        # 反转list
        available_list.reverse()
        # 按模式list的顺序发远征
        for string in modelist:
            # 按先限时后普通的顺序选择远征
            for march in available_list:
                # 三个远征满了就返回
                if fullfind():
                    return
                # march 必须为可用 且为当前选择的mode
                if march.situation == "available" and string in march.mode:
                    send_done(march)
                    select_player()
                    march.situation = "doing"
                sleep(1)

    def receive(self):
        """收远征"""

        def receive_done_sub(get_img=get_img):
            """收远征完成"""
            sleep(1)
            for num in range(0, 3):
                # 找完成的远征
                point = mathc_img(get_img(), "DONE", 0.9)
                point = remove_same(point)
                # 找到可以收的远征
                if point:
                    game_log.info("RECEIVE")
                    click(point[0])
                    point = []
                    sleep(1)
                    # 找MARCHDONE
                    start = time()
                    while 1:
                        if time() - start > 60:
                            raise OvertimeError("receive1")
                        point = mathc_img(get_img(), "MARCHDONE", 0.9)
                        if point:
                            point = []
                            break
                        sleep(STEP * 2)
                    # 在回到远征界面前一直点
                    start = time()
                    while 1:
                        if time() - start > 60:
                            raise OvertimeError("receive2")
                        if marchfind():
                            break
                        click(792, 818)
                        sleep(2)
                # 没远征可收
                else:
                    return

        def receive_done_main():
            """收远征"""

            sleep(5)
            receive_done_sub()
            down_swipe()
            receive_done_sub()
            click(73, 329)
            receive_done_sub()
            down_swipe()
            receive_done_sub()

        receive_done_main()

    def start(self):
        """远征全家桶"""
        if not (self.skill_room or self.receive_march or self.send_march):
            return
        try:
            # 道场续书
            exit_to_main()
            if self.skill_room:
                skill_room()
                sleep(3)
            if not mainpage_marchfind():
                mode = (self.receive_march, self.send_march)
                # 在"收+发"和"收"模式时,如果没有远征可以收就退出远征模式
                if mode == (1, 1) or mode == (1, 0):
                    game_log.info("no march is done")
                    click(1472, 717)
                    return
            go_to_march()
            # 收远征
            if self.receive_march:
                self.receive()
            # 发远征
            if not self.send_march:
                exit_to_main()
                click(1472, 717)
                sleep(3)
                return
            # 初始化
            march_list = March.initialize()
            # 远征优先级
            modelist = ["gold2", "gold1", "power", "card", "book", "nothing"]
            # 做远征
            self.send(march_list, modelist)
            game_log.info("march done")
            exit_to_main()
            click(1472, 717)
            sleep(3)
        except OvertimeError as err:
            game_log.error(err.type)
            self.start()


if __name__ == "__main__":
    Sub.start()
    while 1:
        # 道场技能150
        point = mathc_img(get_img(), "EXP", 0.8)
        point = remove_same(point)
        if point:
            for p in point:
                if p[0] > 800:
                    point.remove(p)
            print(point)
            x = int(point[1][0])
            y = int(point[1][1] + 50)
            click(x, y, 2)  # 银书
            click(1322, 764, 1)
            click(992, 632, 1)
            sleep(3)
            continue
        #  道场确定
        point = mathc_img(get_img(), "SKILLPOINT", 0.9)
        if point:
            point = remove_same(point)
            click(point[0])
            sleep(3)
            continue
