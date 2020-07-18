from core.fight import Fight
from core.march import March_action
from core.group import fightmod
from core.adb import attack, boost, card, click, graze, skill

wave3 = "wave3"
boss = "boss"
default = "default"


def Yukari_H():
    """模式2 H紫妈一回合"""
    mode = wave3
    stage = default

    def before_fight():
        pass

    def fight1():
        skill([1.1, 1.2, 1.3])
        boost(1)
        graze(1)
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
    "March_default": March_action(1, 1, 1).start,
    # 只续技能书
    "March_skill": March_action.only_skill().start,
    # 只收远征
    "March_receive": March_action.only_receive().start,
    # 只发远征
    "March_send": March_action.only_send().start,
    # 刷L华扇，使用队伍1,3,5
    "Kasen_L": [Fight(1, 1, 5), Fight(1, 3, 5), Fight(1, 5, 5)],
    # 妖梦推图机 使用队伍4
    "Youmu_test": Fight(1, 4, 2),
    # 刷L紫妈
    "Yukari_L": [Fight(1, 1, 4), Fight(1, 2, 6)],
    "Youmu_ma": Fight(3, 4, 7),
    # 日常之刷H紫妈
    "Yukari_H": Fight(1, 5, Yukari_H()),
}
