# -*- coding:utf-8 -*-
from adb import attack, graze, boost, skill, card


def extra(s):
    '''残血操作'''
    print('extra')
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
        card(4)
        card(3)
        card(2)
        card(1)
        card(4)
        card(3)
        card(2)
        card(1)


def unexpected():
    '''小概率情况'''
    extra(4)
    extra(3)


class fightmod:
    '''战斗操作组'''
    class mod1:
        '''模式1 单面三人boss战'''
        def fight1():
            skill([1.1, 1.2, 2.1, 2.2, 3.1, 3.2])
            graze(1)
            card(2)

            boost(1)
            graze(1)
            card(1)

            graze(1)
            card(3)

        def fight2():
            graze(1)
            boost(1)
            card(1)

            graze(1)
            card(2)

            graze(1)
            boost(2)
            card(2)

        def fight3():
            card(3)

            boost(1)
            card(3)

            boost(1)
            card(1)

    class mod2:
        '''模式2 单boss两回合秒杀'''
        def fight1():
            skill([1.2])
            graze(1)
            boost(1)
            card(2)

        def fight2():
            skill([1.1])
            boost(1)
            graze(1)
            card(3)

        def fight3():
            boost(1)
            card(1)

    class mod3:
        '''模式3'''
        def fight1():
            pass

        def fight2():
            pass

        def fight3():
            pass

    class mod4:
        '''模式4'''
        def fight1():
            pass

        def fight2():
            pass

        def fight3():
            pass
