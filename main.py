# -*- coding:utf-8 -*-
from fight import action, substart, substop, boss  # ,wave3

substart()
sel = 1
if sel == 1:
    while True:
        # 选关 队伍 模式 战斗 残血 时间
        action(1, 4, boss, 5, 4)  # hard 琪露诺
        action(1, 5, boss, 5, 4)  # hard 梅蒂欣
        action(1, 1, boss, 6, 4)  # hard 灵梦
        action(1, 2, boss, 5, 4)  # hard 帕秋莉
if sel == 2:
    while True:
        action(1, 3, boss, 2, 4)  # 妖梦刷L文文
substop()
