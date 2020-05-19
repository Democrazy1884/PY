# -*- coding:utf-8 -*-
from easy import attack, graze, boost, skill, card


def extra(s):
    '''残血任务'''
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


class fightmod:
    '''战斗操作组'''
    class mod1:
        '''模式1 单面boss战'''
        def fight1():
            skill([1.1, 1.2])
            boost(1)
            card(3)
            card(3)

        def fight2():
            card(1)
            card(1)

        def fight3():
            attack(1)
            boost(2)
            card(2)

    class mod2:
        '''模式2 秒杀模式'''
        def fight1():
            skill([1.1, 1.2])
            boost(1)
            card(3)

        def fight2():
            card(1)

        def fight3():
            pass

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
