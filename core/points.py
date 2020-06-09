# -*- coding:utf-8 -*-
def transform(p, screen):
    if isinstance(p, float):
        return int(p * screen)
    elif isinstance(p, int):
        return float(format(p / screen, ".6f"))


def xtransform(x, screen=1600):
    """x坐标转换"""
    return transform(x, screen)


def ytransform(y, screen=900):
    """y坐标转换"""
    return transform(y, screen)


# adb.py需要的坐标
boost = (1335, 725)
attack_1 = (391, 724)
attack_2 = (932, 724)
card_c = (79, 593)
card_1 = (280, 491)
card_2 = (523, 382)
card_3 = (751, 287)
card_4 = (1011, 242)
card_5 = (1264, 243)
graze = (1435, 504)
skill_c = (1524, 671)
skill_11 = (242, 741)
skill_12 = (368, 741)
skill_13 = (748, 741)
skill_21 = (687, 741)
skill_22 = (807, 741)
skill_23 = (933, 741)
skill_31 = (1124, 741)
skill_32 = (1232, 741)
skill_33 = (1359, 741)
skill_y = (967, 701)
