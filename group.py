# -*- coding:utf-8 -*-
from adb import attack, graze, boost, skill, card, click


def extra(s):
    '''残血操作'''
    # print('extra')
    if s == 1:
        '''全集中'''
        attack(2)
        attack(2)
        attack(2)
    if s == 2:
        '''全分散'''
        attack(1)
        attack(1)
        attack(1)
    if s == 3:
        '''一半集中一半分散'''
        attack(1)
        attack(2)
        attack(1)
    if s == 4:
        '''有什么符卡放什么'''
        unexpected()


def unexpected():
    '''小概率情况'''
    graze(1)
    boost(1)
    card(4)
    card(3)
    card(2)
    card(1)
    click(79, 593)
    attack(2)


class fightmod:
    '''战斗操作组'''
    class mod1:
        '''模式1 妖梦刷L15'''
        def fight1():
            skill([1.2])
            boost(1)
            card(2)

        def fight2():
            boost(1)
            card(4)

        def fight3():
            boost(1)
            skill([1.1])
            card(5)

    class mod2:
        '''模式2 妖梦刷文文'''
        def fight1():
            skill([1.2, 1.1])
            graze(1)
            boost(1)
            card(5)

        def fight2():
            boost(1)
            attack(2)

        def fight3():
            boost(1)
            attack(2)

    class mod3:
        '''模式3 魔理沙单刷铃仙'''
        def fight1():
            skill([1.2, 1.1])
            graze(1)
            card(2)

        def fight2():
            boost(1)
            graze(1)
            card(1)

        def fight3():
            boost(1)
            graze(1)
            card(3)

    class mod4:
        '''模式4 妖梦单刷铃仙'''
        def fight1():
            skill([1.2])
            graze(1)
            boost(1)
            card(1)

        def fight2():
            skill([1.1])
            graze(1)
            boost(1)
            card(3)

        def fight3():
            graze(1)
            boost(1)
            card(2)

    class mod5:
        '''模式5 HARD一回合 卡2'''
        def fight1():
            boost(1)
            card(2)

        def fight2():
            boost(1)
            card(1)

        def fight3():
            boost(1)
            attack(2)

    class mod6:
        '''模式6 HARD一回合 卡1'''
        def fight1():
            boost(1)
            card(1)

        def fight2():
            boost(1)
            card(2)

        def fight3():
            boost(1)
            attack(2)

    class mod7:
        def fight1():
            pass

        def fight2():
            pass

        def fight3():
            pass

    class mod8:
        def fight1():
            pass

        def fight2():
            pass

        def fight3():
            pass

    class mod9:
        def fight1():
            pass

        def fight2():
            pass

        def fight3():
            pass
