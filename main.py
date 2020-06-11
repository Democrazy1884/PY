# -*- coding:utf-8 -*-
from time import sleep

from core.fight import Fight
from core.march import March_action
from core.sub import Sub


# 选关 队伍 战斗组
Youmu_test = Fight(1, 3, 2)
Lan_2 = Fight(2, 1, 3)  # 蓝打2.4
hs = (Fight(1, 4, 4), Fight(1, 3, 4), Fight(1, 2, 4))  # 刷华扇1.3.3
ykl = [
    Fight(1, 3, 5),
    Fight(1, 1, 5),
]
March = March_action()


def main(sel):
    Sub.start()
    if sel == 0:
        March.start()
        Sub.stop()
        sleep(5 * 60)
    elif sel == 1:
        Lan_2.run_time_mode(30)
        March.start()
    elif sel == 2:
        for i in range(0, 3):
            hs[i].run_time_mode(30)
            March.start()
    elif sel == 3:
        for i in ykl:
            i.set_mode("time", 30)
        for i in ykl:
            i.run()
            March.start()
    Sub.stop()


if __name__ == "__main__":
    while 1:
        main(3)
        sleep(3)
