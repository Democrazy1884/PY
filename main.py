# -*- coding:utf-8 -*-
from fight import action, substart, substop, boss, wave3
from time import sleep
substart()
sel = 1
if sel == 1:
    while True:
        # 选关 队伍 模式 战斗 残血 时间

        action(1, 2, boss, 5, 4)  # hard 帕秋莉
        action(1, 4, boss, 5, 4)  # hard 琪露诺
        action(1, 5, boss, 5, 4)  # hard 梅蒂欣
        action(1, 1, boss, 6, 4)  # hard 八云蓝
if sel == 2:
    while True:
        action(1, 3, boss, 2, 4)  # 妖梦刷L文文
if sel == 3:
    while True:
        used_time = action(1, 3, wave3, 1, 4, 1)  # 妖梦刷L15
        sleep(150 - used_time)
substop()
