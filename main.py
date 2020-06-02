# -*- coding:utf-8 -*-
from fight import action
from sub import substart, substop
from march import March

substart()
sel = 3
# action(2, 1, 3)  # 八云蓝刷L铃仙
# action(2, 3, 1)  # 妖梦刷L1
# action(2, 4, 7)  # 魔理沙刷L15 使用队伍4
# 选关 队伍 战斗组  时间
if sel == 3:
    while True:

        action(2, 4, 7)  # 魔理沙刷L15 使用队伍4
        March.start()
        action(2, 3, 1)  # 妖梦刷L15
        March.start()
substop()
