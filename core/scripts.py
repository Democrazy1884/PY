# -*- coding:utf-8 -*-
"""任务库"""


from core.fight import Fight
from core.march import March_action
from core.group import fightmod
from core.adb import attack, boost, card, graze, skill

wave3 = "wave3"
boss = "boss"
default = "default"


def last_word():
    """模式2 一回合"""
    mode = boss
    stage = default

    def before_fight():
        pass

    def fight1():
        skill([1.1, 1.2, 1.3])
        boost(1)
        card(5)
        return 2

    def fight2():
        boost(1)
        graze(1)
        attack(2)
        return 2

    def fight3():
        boost(3)
        graze(1)
        attack(2)
        return 2

    fight = (fight1, fight2, fight3)
    return fightmod(mode, stage, fight, before_fight)


def card_boost():
    """模式2 大量扔符卡"""
    mode = boss
    stage = default

    def before_fight():
        pass

    def fight1():
        skill([1.1, 1.2, 1.3])
        boost(2)
        graze(1)
        card(1)
        return 2

    def fight2():
        boost(2)
        graze(1)
        card(3)
        return 2

    def fight3():
        boost(1)
        graze(1)
        attack(2)
        return fight3

    fight = (fight1, fight2, fight3)
    return fightmod(mode, stage, fight, before_fight)


def card_boost_lastword():
    """模式2 3波打BOSS"""
    mode = boss
    stage = default

    def before_fight():
        pass

    def fight1():
        skill([1.1, 1.2, 1.3])
        card(2)
        return 2

    def fight2():
        boost(3)
        card(5)
        return 2

    def fight3():

        boost(3)
        card(5)
        return 2

    fight = (fight1, fight2, fight3)
    return fightmod(mode, stage, fight, before_fight)


def daily1():
    "日常1 资源战斗"
    mode = boss
    stage = default

    def beforefight():
        pass

    def fight1():
        boost(1)
        card(5)
        attack(2)
        attack(2)
        return 1

    def fight2():
        attack(2)
        attack(2)
        attack(2)
        return 1

    def fight3():
        attack(2)
        attack(2)
        attack(2)
        return 1

    fight = (fight1, fight2, fight3)
    return fightmod(mode, stage, fight, beforefight)


#       选关  队伍 战斗组
# Fight(int1,int2,int3)
scripts_dict = {
    # 默认远征模式
    "March_default": March_action(1, 1, 1),
    # 刷L华扇
    "Kasen_L": Fight(1, 5, 5),
    # 妖梦推图机 使用队伍4
    "Youmu_test": Fight(1, 4, 2, "number", 1),
    # 刷L紫妈
    "Yukari_L": Fight(1, 1, 4),
    "Youmu_ma": Fight(3, 4, 7),
    # 一回合 last word
    "last_word": Fight(1, 1, last_word()),
    "card_boost": Fight(1, 1, card_boost()),
    "card_boost_lastword": Fight(1, 1, card_boost_lastword()),
}
