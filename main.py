# -*- coding:utf-8 -*-
from adb import swipe
from fight import action
from sub import substart, substop
from time import sleep
from march import March
substart()
sel = 3
# action(2, 1, 3)  # 八云蓝刷L铃仙
# action(2, 3, 1)  # 妖梦刷L1
# action(2, 4, 7)  # 魔理沙刷L15 使用队伍4
if sel == 1:
    while True:
        # 选关 队伍 战斗组  时间
        pass
if sel == 2:
    while True:
        swipe(1516, 250, 1516, 670, 5000)
        #
        March.start()
if sel == 3:
    while True:
        action(2, 4, 7)  # 魔理沙刷L15 使用队伍4
        March.start()
        action(2, 3, 1)  # 妖梦刷L15
        March.start()
substop()
