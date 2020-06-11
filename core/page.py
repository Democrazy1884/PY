# -*- coding:utf-8 -*-
from time import sleep

from core.plan import Plan
from core.adb import click, click_s
from core.universe import search
import core.march
import core.game_log as game_log

STEP = 0.5


class Page(object):
    "界面"
    __slots__ = ("name", "_find_function", "_action_function", "next_page", "order")

    def __repr__(self):
        return self.name

    def find(self):
        "界面判断"
        return self._find_function()

    def action(self):
        "界面任务"
        return self._action_function()

    def nextfind(self):
        "下一个界面选择"
        return self.next_page()

    def run(self):
        "界面总操作"
        while 1:
            if search("OFFLINE"):
                game_log.warning("offline")
                click(963, 632)
            if self.find():
                break
            sleep(STEP)
        self.action()
        return self.nextfind()


class First(Page):
    "初始界面"

    def __init__(self):
        def find():
            return search(839, 884, 12, 774, "FIRST", 0.5)

        def action():
            click(500, 500)

        self.name = "First"
        self._action_function = action
        self._find_function = find
        self.next_page = Main


class Main(Page):
    "主界面"

    def __init__(self):
        def find():
            return search("MAIN")

        def action():
            if search("MARCH"):
                Plan.add(self.name, 5, "March")
            if search("BUILDING"):
                Plan.add(self.name, 5, "Structure")

        def next_page():
            order = self.order
            # 远征
            if "March" == order:
                click(1390, 536)
                return March
            # 设施
            if "Structure" == order:
                click(798, 786)
                return Structure
            # 战斗
            if "Fight" == order:
                click(1456, 722)
                return Fight

        self.name = "Main"
        self._action_function = action
        self._find_function = find
        self.next_page = next_page


class March(Page):
    "远征界面"

    def __init__(self):
        def find():
            return search("MARCHPAGE")

        def action():
            "收"
            if self.order[0]:
                core.march.March.receive()
            "发"
            if self.order[1]:
                march_list = core.march.March.initialize()
                modelist = ["gold2", "gold1", "power", "card", "book", "nothing"]
                core.march.March.send(march_list, modelist)

        def next_page():
            click_s(1559, 35)
            return Main

        self.name = "March"
        self._action_function = action
        self._find_function = find
        self.next_page = next_page


class Structure(Page):
    "设施界面"

    def __init__(self):
        def find():
            pass

        def action():
            pass

        def next_page():
            return Main

        self.name = "Structure"
        self._action_function = action
        self._find_function = find
        self.next_page = next_page


class Skillroom(Page):
    "道场"

    def __init__(self):
        def find():
            pass

        def action():
            pass

        def next_page():
            return Main

        self.name = "Skillroom"
        self._action_function = action
        self._find_function = find
        self.next_page = Main


class Fight(Page):
    "战斗界面"
    def __init__(self):
        def find():
            return search("FIGHT") or search("FIGHT1")

        def action():
            pass

        def next_page():
            return

        self.name = "Fight"
        self._action_function = action
        self._find_function = find
        self.next_page = next_page


def start():
    pass
