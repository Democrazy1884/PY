# -*- coding:utf-8 -*-
import os
import sys
from time import sleep, time
import core.game_log as game_log
from core.adb import click  # , swipe
from core.gameerror import OvertimeError, Watererror
from core.group import extra, fightmod, fightmod_dict
from core.image import mathc_img
from core.sub import get_img
from core.universe import search
from retrying import retry
import numpy as np

STEP = 0.5
# # # # # # # # # # # # # # # # # # # # #  判断函数  # # # # # # # # # # # # # # # # # # #


def startfind(img=get_img):
    """选关界面判断"""
    return search("FIGHT") or search("FIGHT1")


def gofind(img=get_img):
    """选关开始界面判断"""
    return search("GO")


def boostfind(img=get_img):
    """找boost"""
    return search("BOOST")


def endfind(img=get_img):
    """战斗结束判断"""
    return search("END")


def fullfind(img=get_img):
    """残血判定"""
    return search("FULL")


def nextfind(img=get_img):
    "结束返回判定"
    return search("NEXT")


def againfind(img=get_img):
    """结束再开判定"""
    return search("AGAIN")


def waterfind():
    "出水判定"
    point = mathc_img(get_img(), "WATER", 0.9)
    if point:
        return True
    else:
        return False


def offlinefind(flag=0):
    """断网判定"""
    if search("OFFLINE"):
        game_log.warning("offline")
        click(963, 632)  # 断网重连操作
        sleep(10)
        offlinefind()
        # if flag == 1:
        #   end("next")
        return True
    else:
        return False


def powerfind(img=get_img):
    "油耗判定"
    ret = search("POWERFIND")
    if isinstance(ret, int):
        return ret


# # # # # # # # # # # # # # # # # # # # #  初级操作函数  # # # # # # # # # # # # # # # # # # #


def go(team):
    """队伍选择"""
    # 判断当前队伍 计算距目标的距离
    start = time()
    while 1:
        if time() - start > 60:
            raise OvertimeError("go")
        value = search("TEAMFIND")
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
def adjust(sel):
    """调整难度

    :sel: 1:normal 2:hard 3:lunatic

    """
    while True:
        if search("LUNATIC"):
            now = 3
        elif search("HARD"):
            now = 2
        elif search("NORMAL"):
            now = 1
        if now == sel:
            break
        else:
            click(541, 808)


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


# # # # # # # # # # # # # # # # # # # # #  主函数  # # # # # # # # # # # # # # # # # # #


class Fight:
    """
    战斗类

    stage(关卡选择)

    team(队伍选择)

    group(战斗模式选择)

    mode(战斗模式)

    num(模式赋值)

    """

    def __init__(
        self,
        stage: (int, np.ndarray),
        team: int,
        group: (int, fightmod),
        mode="time",
        num="30",
    ):
        if isinstance(group, int):
            group = fightmod_dict[group]()  # 初始化战斗组对象
        elif isinstance(group, fightmod):
            pass
        self.stage = stage  # 选关
        self.team = team  # 选队伍
        self.group = group  # 选战斗模式
        # 中断重启所需信息
        self.info = None
        # 错误中断后启动赋值方法
        self.mode_start = None
        # 模式结束方法
        self.mode_end = None
        # 总用时
        self.all_time_use = 0
        # 中断模式
        # 模式结束判断所用数值
        self.set_mode(mode, num)

    def reinitialize(self):
        "重新初始化"
        self.all_time_use = 0

    def restart_game(self):
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
            elif againfind():
                click(1412, 812)
            click(500, 500)
            sleep(5)
        # self.select_stage(self.stage)
        # select_team(self.team)

    def select_stage(self, number):
        """选关"""

        def selection(stage):
            if isinstance(stage, int):
                if stage == 1:
                    click(1105, 231)  # 选关1
                elif stage == 2:
                    click(1105, 426)  # 选关2
                elif stage == 3:
                    click(1105, 612)  # 选关3
            else:
                point = mathc_img(get_img(), stage, 0.9)
                if point:
                    click(point[0])
                else:
                    self.before_fight()
                    self.select_stage(self, number)

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

    def set_mode(self, mode, value):
        "设置模式"
        if mode == "time":
            self.mode = self.run_time_mode
        if mode == "number":
            self.mode = self.run_number_mode
        if mode == "power":
            self.mode = self.run_power_mode
        if mode == "time and power":
            self.mode = self.run_time_and_power_mode
        self.mode_number = value

    def run(self):
        "启动"
        return self.mode(self.mode_number)

    def run_time_mode(self, tim: int):
        "时间控制"

        def mode_start():
            self.begintime = self.info

        def mode_end():
            self.info = self.begintime
            if int(time()) - self.begintime > 60 * self.mode_number:
                self.info = None
                return True

        self.mode = self.run_time_mode
        self.mode_number = tim
        self.mode_start = mode_start
        self.mode_end = mode_end
        tim = self.action()
        return tim

    def run_number_mode(self, num: int):
        "次数控制"

        def mode_start():
            self.n = self.info

        def mode_end():
            self.info = self.n
            if self.n >= self.mode_number:
                self.info = None
                return True

        self.mode = self.run_number_mode
        self.mode_number = num
        self.mode_start = mode_start
        self.mode_end = mode_end
        tim = self.action()
        return tim

    def run_power_mode(self, power: int):
        "油耗控制"

        def mode_start():
            self.power_use = self.info

        def mode_end():
            self.info = self.power_use * self.n
            if self.power_use * self.n >= self.mode_number:
                self.info = None
                return True

        self.mode = self.run_power_mode
        self.mode_number = power
        self.mode_start = mode_start
        self.mode_end = mode_end
        tim = self.action()
        return tim

    def run_time_and_power_mode(self, number, time, power):
        "油耗时间共同控制"

        def mode_start():
            self.begintime = self.info[0]
            self.power_use = self.info[1]

        def mode_end():
            self.info = (self.begintime, self.power_use * self.n)
            if (
                int(time()) - self.begintime > 60 * self.mode_number[0]
                or self.power_use * self.n >= self.mode_number[1]
            ):
                self.info = None
                return True

        self.mode = self.run_time_and_power_mode
        self.mode_number = (time, power)
        self.mode_start = mode_start
        self.mode_end = mode_end
        tim = self.action()
        return tim

    def set_start(self):
        "开始阶段赋初值"
        info = self.info
        stage = self.group.stage
        self.begintime = int(time())
        self.power_use = 0
        self.n = 0
        if info is not None:
            self.mode_start()
        if stage != "default":
            self.stage = stage

    def action_sub(self):
        "战斗函数，单次运行"
        group = self.group
        fightway = group.mode
        if fightway == "boss":
            fightway = boss
        elif fightway == "wave3":
            fightway = wave3
        fightway(group)  # 战斗

    def set_end(self):
        """循环结束判断"""
        if self.mode_end():
            return True
        else:
            # 循环未能结束
            end("again")
            return False

    def water(f):
        """出水错误检查"""

        def inner(*args, **kwargs):
            try:
                ret = f(*args, **kwargs)
                return ret
            except Watererror as e:
                game_log.error(e.type)
                args[0].all_time_use = 0
                sleep(5)
                return

        return inner

    @retry
    def overtime(f):
        """ 超时错误检查"""

        def inner(*args, **kwargs):
            try:
                ret = f(*args, **kwargs)
                return ret
            except OvertimeError as e:
                game_log.error(e.type)
                args[0].restart_game()
                args[0].action()
                sleep(5)

        return inner

    @overtime
    @water
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
        self.select_stage(stage)
        # 选队伍
        self.power_use = select_team(team)
        while 1:
            # 每轮开始计时
            starttime = int(time())
            # 战斗
            self.action_sub()
            self.n += 1
            # 结束判断
            if self.set_end():
                break
            elif self.mode_number != 1:
                game_log.info("time use:" + str(int(time()) - starttime) + "s")
            self.all_time_use = int(time()) - begintime
        end("next")
        game_log.info("all time use:" + str(int(time()) - begintime) + "s")
        self.all_time_use = 0
        sleep(5)

    def before_fight(self):
        "战前选择"
        return self.group.before()


if __name__ == "__main__":
    pass
