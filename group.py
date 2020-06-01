# -*- coding:utf-8 -*-
from adb import attack, graze, boost, skill, card, click


def extra(s):
    '''残血操作'''
    # print('extra:%d' % s)
    if isinstance(s, int):
        if s == 1:
            '''全集中'''
            attack(2)
            attack(2)
            attack(2)
        elif s == 2:
            '''全分散'''
            attack(1)
            attack(1)
            attack(1)
        elif s == 3:
            '''一半集中一半分散'''
            attack(1)
            attack(2)
            attack(1)
        elif s == 4:
            '''有什么符卡放什么'''
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


class fightmod:
    '''战斗操作组'''
    class mod1:
        '''模式1 妖梦刷L15'''
        def mode():
            return 'wave3'

        def fight1():
            skill([1.2])
            boost(1)
            card(2)
            return 4

        def fight2():
            boost(1)
            card(4)
            return 4

        def fight3():
            boost(1)
            skill([1.1])
            card(5)
            return 4

    class mod2:
        '''模式2 八云蓝打L魔理沙'''
        def mode():
            return 'boss'

        def fight1():
            card(2)
            return fightmod.mod2.extra

        def fight2():
            skill([1.2])
            graze(1)
            card(4)
            return fightmod.mod2.extra

        def fight3():
            boost(2)
            graze(1)
            skill([1.1])
            card(1)
            return fightmod.mod2.fight4

        def fight4():
            boost(3)
            graze(1)
            card(3)
            return fightmod.mod2.extra

        def extra():
            graze(1)
            boost(1)
            attack(2)
            return fightmod.mod2.extra

    class mod3:
        '''模式3 八云蓝打L铃仙'''
        def mode():
            return 'boss'

        def fight1():
            skill([1.2])
            card(2)
            return fightmod.mod3.extra

        def fight2():
            skill([1.1])
            boost(2)
            card(1)
            return fightmod.mod3.extra

        def fight3():
            boost(2)
            graze(1)
            card(3)
            return fightmod.mod3.fight4

        def fight4():
            boost(1)
            card(4)
            return fightmod.mod3.extra

        def extra():
            boost(1)
            attack(2)
            return fightmod.mod3.extra

    class mod4:
        '''模式4 '''
        def mode():
            return ''

        def fight1():
            pass

        def fight2():
            pass

        def fight3():
            pass

    class mod5:
        '''模式5 '''
        def mode():
            return 'boss'

        def fight1():
            pass

        def fight2():
            pass

        def fight3():
            pass

    class mod6:
        '''模式6 '''
        def mode():
            return 'boss'

        def fight1():
            pass

        def fight2():
            pass

        def fight3():
            pass

    class mod7:
        '''魔理沙打L15'''
        def mode():
            return 'wave3'

        def fight1():
            skill([1.2])
            boost(1)
            card(1)
            return 1

        def fight2():
            graze(1)
            boost(1)
            card(2)
            return fightmod.mod7.fight2_extra

        def fight3():
            boost(3)
            graze(1)
            skill([1.1])
            card(3)
            return 1

        def fight2_extra():
            graze(1)
            card(4)
            return 2

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
