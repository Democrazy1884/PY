# -*- coding:utf-8 -*-
from core.adb import attack, boost, card, click, graze, skill


def extra(s):
    """残血操作"""
    # print('extra:%d' % s)
    if isinstance(s, int):
        if s == 1:
            """全集中"""
            attack(2)
            attack(2)
            attack(2)
        elif s == 2:
            """全分散"""
            attack(1)
            attack(1)
            attack(1)
        elif s == 3:
            """一半集中一半分散"""
            attack(1)
            attack(2)
            attack(1)
        elif s == 4:
            """有什么符卡放什么"""
            graze(1)
            boost(1)
            card(4)
            card(3)
            card(2)
            card(1)
            click(79, 593)
            attack(2)
        return s
    else:
        return s()


wave3 = "wave3"
boss = "boss"
default = "default"


class fightmod:
    """战斗操作类"""

    def __init__(self, mode, stage, fight, before):
        self.mode = mode
        self.stage = stage
        self.fight = fight
        self.before = before

    @classmethod
    def mode1(cls):
        """模式1 """
        pass

    @classmethod
    def mode2(cls):
        """模式2 妖梦推土机"""
        mode = wave3
        stage = default

        def before_fight():
            pass

        def fight1():
            skill(1.2)
            graze(1)
            boost(1)
            card(2)
            return 1

        def fight2():
            graze(1)
            boost(1)
            card(4)
            return 1

        def fight3():
            skill(1.1)
            graze(1)
            boost(1)
            card(5)
            return 1

        fight = (fight1, fight2, fight3)
        return cls(mode, stage, fight, before_fight)

    @classmethod
    def mode3(cls):
        """模式3 蓝打2.4"""
        mode = wave3
        stage = default

        def before_fight():
            pass

        def fight1():
            skill(1.2)
            graze(1)
            boost(1)
            card(1)
            return ex1

        def ex1():
            boost(1)
            card(2)
            return 1

        def fight2():
            graze(1)
            boost(2)
            card(3)
            return ex2

        def ex2():
            boost(1)
            card(4)
            return 1

        def fight3():
            skill(1.1)
            graze(1)
            boost(3)
            card(5)
            return 1

        fight = (fight1, fight2, fight3)
        return cls(mode, stage, fight, before_fight)

    @classmethod
    def mode4(cls):
        """模式4 L紫妈 梅蒂欣加铃仙"""
        mode = boss
        stage = default

        def before_fight():
            pass

        def fight1():
            skill([1.1, 1.2, 2.1, 2.2, 2.3])
            boost(1)
            graze(1)
            card(1)

            boost(1)
            graze(1)
            card(3)

        def fight2():
            boost(1)
            graze(1)
            card(3)

            boost(1)
            graze(1)
            card(1)

        def fight3():
            boost(1)
            graze(1)
            card(2)

            boost(1)
            graze(1)
            card(2)
            return 1

        fight = (fight1, fight2, fight3)
        return cls(mode, stage, fight, before_fight)

    @classmethod
    def mode5(cls):
        """模式5 L华扇"""
        mode = boss
        stage = default

        def before_fight():
            pass

        def fight1():
            graze(1)
            card(1)

        def fight2():
            boost(1)
            graze(1)
            card(3)

        def fight3():
            skill([1.1, 1.2, 1.3])
            boost(3)
            graze(1)
            card(5)
            return extra

        def extra():
            graze(1)
            boost(1)
            attack(2)
            return extra

        fight = (fight1, fight2, fight3)
        return cls(mode, stage, fight, before_fight)

    @classmethod
    def mode6(cls):
        """模式6 L紫妈 莉莉白加帕秋莉 """
        mode = boss
        stage = default

        def before_fight():
            pass

        def fight1():
            skill([1.1, 1.2, 2.1, 2.2, 2.3])
            boost(1)
            graze(1)

            card(1)
            boost(1)
            graze(1)
            card(1)

        def fight2():
            boost(1)
            graze(1)
            card(3)
            boost(1)
            graze(1)
            card(3)

        def fight3():
            boost(1)
            graze(1)
            attack(2)

            boost(1)
            graze(1)
            card(2)
            return 1

        fight = (fight1, fight2, fight3)
        return cls(mode, stage, fight, before_fight)

    @classmethod
    def mode7(cls):
        """模式7 妖梦刷麻将"""
        mode = wave3
        stage = default

        def before_fight():
            pass

        def fight1():
            boost(1)
            skill(1.2)
            graze(1)
            card(1)
            return 1

        def fight2():
            boost(1)
            skill(1.1)
            graze(1)
            card(2)
            return 1

        def fight3():
            boost(3)
            graze(1)
            card(3)
            return 1

        fight = (fight1, fight2, fight3)
        return cls(mode, stage, fight, before_fight)

    @classmethod
    def mode8(cls):
        """模式8 活动刷华扇和灵梦两回合"""
        mode = boss
        stage = default

        def before_fight():
            pass

        def fight1():
            boost(1)
            skill([1.1, 1.2, 1.3])
            graze(1)
            card(1)
            return 1

        def fight2():
            boost(3)
            graze(1)
            card(5)
            return 1

        def fight3():
            boost(3)
            graze(1)
            attack(2)
            return fight3

        fight = (fight1, fight2, fight3)
        return cls(mode, stage, fight, before_fight)

    @classmethod
    def mode9(cls):
        """模式9 活动刷华扇和灵梦"""
        mode = boss
        stage = default

        def before_fight():
            pass

        def fight1():
            boost(1)
            skill([1.1, 1.2, 1.3])
            graze(1)
            card(5)
            return 1

        def fight2():
            boost(1)
            skill(1.1)
            graze(1)
            card(2)
            return 1

        def fight3():
            boost(3)
            graze(1)
            card(3)
            return 1

        fight = (fight1, fight2, fight3)
        return cls(mode, stage, fight, before_fight)


fightmod_dict = {
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

if __name__ == "__main__":
    x = fightmod.get_mode(1)
    print(x)
