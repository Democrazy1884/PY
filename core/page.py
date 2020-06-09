# -*- coding:utf-8 -*-
from core.universe import search
from core.adb import click
from time import sleep
import core.plan as plan


class Page(object):
    "界面"
    __slots__ = ("_find_function", "_action_function", "next_page")

    def find(self):
        "界面判断"
        return self._find_function()

    def action(self):
        "界面操作"
        return self._action_function()

    def nextfind(self):
        "下一个界面判断"
        return self.next_page()

    def run(self):
        "界面总操作"
        while 1:
            if self.find():
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
            self.order = plan.get_job("Main")
            return None

        def next_page(self):
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
                    return Fight
                self.order.remove(order)

        self._action_function = action
        self._find_function = find
        self.next_page = next_page


class March(Page):
    def __init__(self):
        def find():
            return search(696, 737, 1424, 1521, "MAIN", 0.8)


class Structure(Page):
    pass


class Fight(Page):
    pass
