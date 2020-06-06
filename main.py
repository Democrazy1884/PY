# -*- coding:utf-8 -*-
from fight import Fight
from sub import Sub
from march import March
from time import sleep

# 选关 队伍 战斗组
Youmu_l15 = Fight(2, 3, 1)  # 妖梦刷L15
Marisa_l15 = Fight(2, 4, 7)  # 魔理沙刷L15
Youmu_test = Fight(1, 3, 2)
Lan_2 = Fight(2, 1, 3)  # 蓝打2.4
hs = (Fight(1, 4, 4), Fight(1, 3, 4), Fight(1, 2, 4))


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
        Marisa_l15.run_time_mode(30)  # 魔理沙刷L15
        March.start()
        Youmu_l15.run_time_mode(30)  # 妖梦刷L15
        March.start()


if __name__ == "__main__":
    while 1:
        main(2)
