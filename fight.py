# -*- coding:utf-8 -*-
import os
import sys
from time import sleep, time
import cv2
from universe import search
import game_log
from adb import click  # , swipe
from gameerror import OvertimeError, Watererror
from group import extra, fightmod
from image import mathc_img
from sub import get_img

STEP = 0.5
# # # # # # # # # # # # # # # # # # # # #  判断函数  # # # # # # # # # # # # # # # # # # #

FIGHT = cv2.imread(sys.path[0] + "\\IMG\\fight.jpg")
FIGHT1 = cv2.imread(sys.path[0] + "\\IMG\\fight1.jpg")


def startfind(img=get_img):
    """选关界面判断"""
    if search(14, 50, 88, 161, img, FIGHT, 0.8) or search(
        14, 50, 88, 161, img, FIGHT1, 0.8
    ):
        return True
    else:
        return False


GO = cv2.imread(sys.path[0] + "\\IMG\\go.jpg")


def gofind(img=get_img):
    """选关开始界面判断"""
    return search(754, 830, 1220, 1465, img, GO, 0.8)


BOOST = cv2.imread(sys.path[0] + "\\IMG\\boost.jpg")  # 战斗判断用 boost


def boostfind(img=get_img):
    """找boost"""
    return search(753, 790, 1259, 1410, img, BOOST, 0.7)


END = cv2.imread(sys.path[0] + "\\IMG\\end.jpg")  # 战斗结束


def endfind(img=get_img):
    """战斗结束判断"""
    return search(158, 216, 690, 907, img, END, 0.4)


FULL = cv2.imread(sys.path[0] + "\\IMG\\full.jpg")


def fullfind(img=get_img):
    """残血判定"""
    return search(140, 150, 529, 534, img, FULL, 0.8)


NEXT = cv2.imread(sys.path[0] + "\\IMG\\next.jpg")


def nextfind(img=get_img):
    "结束返回判定"
    return search(795, 831, 1388, 1465, img, NEXT, 0.8)


AGAIN = cv2.imread(sys.path[0] + "\\IMG\\again.jpg")


def againfind(img=get_img):
    """结束再开判定"""
    return search(795, 831, 101, 181, img, AGAIN, 0.8)


WATER = cv2.imread(sys.path[0] + "\\IMG\\water.jpg", 0)


def waterfind():
    "出水判定"
    x, y = mathc_img(get_img(), WATER, 0.9)
    if x:
        return True
    else:
        return False


OFFLINE = cv2.imread(sys.path[0] + "\\IMG\\offline.jpg")


def offlinefind(flag=0):
    """断网判定"""
    if search(390, 485, 626, 960, get_img, OFFLINE, 0.9):
        game_log.warning("offline")
        sleep(10)
        click(963, 632)  # 断网重连操作
        sleep(10)
        if flag == 1:
            end("next")
        return True
    else:
        return False


NUM_tuple = (
    cv2.imread(sys.path[0] + "\\IMG\\power\\5.jpg"),
    cv2.imread(sys.path[0] + "\\IMG\\power\\6.jpg"),
    cv2.imread(sys.path[0] + "\\IMG\\power\\7.jpg"),
    cv2.imread(sys.path[0] + "\\IMG\\power\\8.jpg"),
    cv2.imread(sys.path[0] + "\\IMG\\power\\8.jpg"),
    cv2.imread(sys.path[0] + "\\IMG\\power\\10.jpg"),
    cv2.imread(sys.path[0] + "\\IMG\\power\\11.jpg"),
    cv2.imread(sys.path[0] + "\\IMG\\power\\12.jpg"),
    cv2.imread(sys.path[0] + "\\IMG\\power\\13.jpg"),
    cv2.imread(sys.path[0] + "\\IMG\\power\\14.jpg"),
    cv2.imread(sys.path[0] + "\\IMG\\power\\15.jpg"),
    cv2.imread(sys.path[0] + "\\IMG\\power\\16.jpg"),
    cv2.imread(sys.path[0] + "\\IMG\\power\\17.jpg"),
    cv2.imread(sys.path[0] + "\\IMG\\power\\18.jpg"),
    cv2.imread(sys.path[0] + "\\IMG\\power\\19.jpg"),
    cv2.imread(sys.path[0] + "\\IMG\\power\\20.jpg"),
)


def powerfind(img=get_img):
    "油耗判定"
    ret = search(686, 726, 1371, 1431, img, NUM_tuple, 0.5)
    if isinstance(ret, int):
        return ret


# # # # # # # # # # # # # # # # # # # # #  初级操作函数  # # # # # # # # # # # # # # # # # # #


def selection(stage):
    """选关"""
    if isinstance(stage, int):
        if stage == 1:
            click(1105, 231)  # 选关1
        elif stage == 2:
            click(1105, 426)  # 选关2
        elif stage == 3:
            click(1105, 612)  # 选关3
    else:
        x, y = mathc_img(get_img(), stage, 0.9)
        if x:
            click(x[0], y[0])
        else:  # TODO 没找到目标，去重新选择
            pass


NUM5_tuple = (
    cv2.imread(sys.path[0] + "\\IMG\\1.jpg"),
    cv2.imread(sys.path[0] + "\\IMG\\2.jpg"),
    cv2.imread(sys.path[0] + "\\IMG\\3.jpg"),
    cv2.imread(sys.path[0] + "\\IMG\\4.jpg"),
    cv2.imread(sys.path[0] + "\\IMG\\5.jpg"),
)


def go(team):
    """队伍选择"""
    # 判断当前队伍 计算距目标的距离
    start = time()
    while 1:
        if time() - start > 60:
            raise OvertimeError("go")
        value = search(790, 815, 723, 743, get_img, NUM5_tuple, 0.5)
        value = value + 1 - team
        if value == 0:
            power_use = powerfind()
            # print(power_use)
            click(1338, 796)
            return power_use
        elif value > 0:
            click(58, 534)
        else:
            click(1030, 534)
        sleep(2)


def end(sel):
    """结束处理"""
    click(500, 500)
    start = time()
    while 1:
        if time() - start > 60:
            raise OvertimeError("end")
        offlinefind()
        if againfind() or nextfind():
            break
        sleep(STEP * 3)
    if waterfind():
        print("water find")
        click(1415, 813)
        raise Watererror("end")
    elif sel == "next":
        click(1415, 813)
    elif sel == "again":
        click(181, 814)


def usegroup(fightway: fightmod, wave: int):
    """战斗"""
    extra = fightway.fight[wave - 1]()
    sleep(3)
    return extra


# # # # # # # # # # # # # # # # # # # # #  中级混合函数  # # # # # # # # # # # # # # # # # # #


def select_stage(number):
    """选关"""
    start = time()
    while 1:
        if time() - start > 60:
            raise OvertimeError("stage")
        offlinefind(1)
        if startfind():
            selection(number)
            sleep(2)
            break
        sleep(STEP * 2)


def select_team(number):
    """选队伍和点击出发"""
    start = time()
    while 1:
        if time() - start > 60:
            raise OvertimeError("team")
        offlinefind()
        if gofind():
            power_use = go(number)
            sleep(2)
            return power_use
        sleep(STEP * 2)


def select_notfull(abnormal=0):
    """残血处理"""
    next_abnormal = extra(abnormal)
    sleep(5)
    start = time()
    while 1:
        if time() - start > 30:
            raise OvertimeError("notfull")
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
                start = time()
        elif endfind():
            # 残血打完发现现在是结束
            return 1
        sleep(STEP * 2)


def select_wavefight(abnormal=0):
    """wave战斗选择"""
    start = time()
    while 1:
        if time() - start > 60:
            raise OvertimeError("wavefight")
        offlinefind()
        if boostfind():
            if fullfind():
                # 满血
                return 0
            else:
                # 残血
                return select_notfull(abnormal)
                start = time()
        elif endfind():
            # 结束
            return 1
        sleep(STEP * 3)


def select_bossfight(abnormal):
    """boss战斗选择"""
    start = time()
    while 1:
        if time() - start > 60:
            raise OvertimeError("bossfight")
        offlinefind()
        if boostfind():
            # 战斗
            return 0
        elif endfind():
            # 结束
            return 1
        sleep(STEP * 3)


def wave3(groups: fightmod):
    """三波战斗"""

    if select_wavefight():
        return
    else:
        abnormal = usegroup(groups, 1)

    if select_wavefight(abnormal):
        return
    else:
        abnormal = usegroup(groups, 2)

    if select_wavefight(abnormal):
        return
    else:
        abnormal = usegroup(groups, 3)

    if select_wavefight(abnormal):
        return
    else:
        game_log.error("wave3:no end")


def boss(groups: fightmod):
    """boss战斗"""
    if select_bossfight(1):
        return
    else:
        abnormal = usegroup(groups, 1)

    if select_bossfight(abnormal):
        return
    else:
        abnormal = usegroup(groups, 2)

    if select_bossfight(abnormal):
        return
    else:
        abnormal = usegroup(groups, 3)

    if select_wavefight(abnormal):
        return
    else:
        game_log.error("boss:no end")


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def restart_game():
    "游戏重启"
    start = time()
    while 1:
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
            end("next")
        elif gofind():
            click(48, 48)
        click(500, 500)
        sleep(5)


# # # # # # # # # # # # # # # # # # # # #  主函数  # # # # # # # # # # # # # # # # # # #


d = {
    1: fightmod.mode1,
    2: fightmod.mode2,
    3: fightmod.mode3,
    4: fightmod.mode4,
    5: fightmod.mode5,
    6: fightmod.mode6,
    7: fightmod.mode7,
    8: fightmod.mode8,
    9: fightmod.mode9,
}


class Fight:
    """
    战斗类

    stage(关卡选择)

    team(队伍选择)

    group(战斗模式选择)

    """

    def __init__(self, stage: int, team: int, group: int):
        if isinstance(group, int):
            group = d[group]()  # 初始化战斗组对象
        else:
            pass  # TODO 其它的读取方法，从json读啥的
        self.stage = stage  # 选关
        self.team = team  # 选队伍
        self.group = group  # 选战斗模式
        # 中断重启所需信息
        self.info = None
        self.mode = None
        # 总用时
        self.all_time_use = 0

    def action_sub(self):
        "战斗函数，单次运行"
        group = self.group
        fightway = group.mode
        if fightway == "boss":
            fightway = boss
        elif fightway == "wave3":
            fightway = wave3
        fightway(group)  # 战斗

    def set_start(self):
        "开始阶段赋初值"
        info = self.info
        mode = self.mode
        stage = self.group.stage
        if info is None:
            self.begintime = int(time())
            self.power_use = 0
            self.n = 0
        elif mode == "time":
            self.begintime = info
            self.power_use = 0
            self.n = 0
        elif mode == "power":
            self.begintime = int(time())
            self.power_use = info
            self.n = 0
        elif mode == "number":
            self.begintime = int(time())
            self.power_use = 0
            self.n = info
        elif mode == "time and power":
            self.begintime = info[0]
            self.power_use = info[1]
            self.n = 0
        if stage != "default":
            self.stage = stage

    def set_end(self):
        """循环结束判断"""
        mode = self.mode
        number = self.number
        begintime = self.begintime
        n = self.n
        power_use = self.power_use
        if mode == "time":
            self.info = begintime
            if int(time()) - begintime > 60 * number:
                return True
        elif mode == "number":
            self.info = n
            if n >= number:
                return True
        elif mode == "power":
            self.info = power_use * n
            if power_use * n >= number:
                return True
        elif mode == "time and power":
            self.info = (begintime, power_use * n)
            if int(time()) - begintime > 60 * number[0] or power_use * n >= number[1]:
                return True
        # 循环未能结束
        end("again")
        return False

    def action(self):
        """

        战斗主函数

        """
        # 设定初始值
        self.set_start()
        begintime = self.begintime
        stage = self.stage
        team = self.team
        # 选关
        select_stage(stage)
        # 选队伍
        power_use = select_team(team)
        self.power_use = power_use
        # 选关选队伍用时输出
        # game_log.info("select time:" + str(int(time()) - begintime) + "s")
        while 1:
            try:
                # 每轮开始计时
                starttime = int(time())
                # 战斗
                self.action_sub()
                self.n += 1
                # 结束判断
                if self.set_end():
                    break
                elif self.number != 1:
                    game_log.info("time use:" + str(int(time()) - starttime) + "s")
                self.all_time_use = int(time()) - begintime
            except OvertimeError as e:
                game_log.error(e.type)
                restart_game()
                select_stage(stage)
                select_team(team)
        end("next")
        game_log.info("all time use:" + str(int(time()) - begintime) + "s")

    def action_main(self):
        """出水检查"""
        try:
            self.action()
        except Watererror as e:
            game_log.error(e.type)
        finally:
            return self.all_time_use

    def before_fight(self):
        "战前选择"
        return self.group.before()

    def run_time_mode(self, tim: int):
        "时间控制"
        self.mode = "time"
        self.number = tim
        tim = self.action_main()
        game_log.info("break")
        return tim

    def run_number_mode(self, num: int):
        "次数控制"
        self.mode = "number"
        self.number = num
        tim = self.action_main()
        if num != 1:
            game_log.info("break")
        return tim

    def run_power_mode(self, power: int):
        "油耗控制"
        self.mode = "power"
        self.number = power
        tim = self.action_main()
        game_log.info("break")
        return tim

    def run_time_and_power_mode(self, number, time, power):
        "油耗时间共同控制"
        self.mode = "time and power"
        mode_tuple = (time, power)
        self.number = mode_tuple
        tim = self.action_main()
        game_log.info("break")
        return tim


if __name__ == "__main__":
    pass
