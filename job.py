# -*- coding:utf-8 -*-
from core.fight import Fight
from core.march import March_action as March


class mode:
    "脚本计划"

    def __init__(self):
        pass

    # TODO 从文件读计划
    @classmethod
    def get_mode(cls):
        pass


def mod1():
    mod = mode()
    mod.march = March()
    mod.fight = Fight(1, 4, 4)
    mod.fight.mode = mod.fight.run_time_mode
    mod.fight.number = 30
    print(mod.march)
    return mod


if __name__ == "__main__":
    mod = mod1()
    mod.fight
