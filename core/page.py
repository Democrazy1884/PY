# -*- coding:utf-8 -*-
from time import sleep

import core.plan as Plan
from core.adb import click, click_s
from core.universe import search


class Page(object):
    "界面"
    __slots__ = ("name", "_find_function", "_action_function", "next_page")

    def __repr__(self):
        return self.name

    def find(self):
        "界面判断"
        return self._find_function()

    def nextfind(self):
        "下一个界面选择"
        return self.next_page()

    def run(self):
        "界面总操作"
        while 1:
            if self.find():
                break
        self.action()
        return self.nextfind()
        sleep(1)


class First(Page):
    "初始界面"

    def __init__(self):
        def find():
            return search(839, 884, 12, 774, "FIRST", 0.5)

        def action():
            click(500, 500)

        def next_page():
            return Main

        self._action_function = action
        self._find_function = find
        self.next_page = next_page


class Main(Page):
    "主界面"

    def __init__(self):
        def find():
            return search(696, 737, 1424, 1521, "MAIN", 0.8)

        def action():
            self.order = Plan.get("Main")

        def next_page():
            for order in self.order:
                # 远征
                if "march" == order:
                    click(1390, 536)
                    return March
                # 设施
                if "skill" == order:
                    click(798, 786)
                    return Structure
                # 战斗
                if "fight" == order:
                    click(1456, 722)
                    return Select

        self.name = "main"
        self._action_function = action
        self._find_function = find
        self.next_page = next_page


class March(Page):
    "远征界面"

    def __init__(self):
        def find():
            return search(13, 48, 89, 231, "MARCHPAGE", 0.8)

        def action():
            pass

        def next_page():
            click_s(1559, 35)
            return Main

        self.name = "march"
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

        self.name = "structure"
        self._action_function = action
        self._find_function = find
        self.next_page = next_page


class Select(Page):
    "选关界面"
    pass
