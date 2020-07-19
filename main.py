# -*- coding:utf-8 -*-
# 出活动时用
from time import sleep
from core.scripts import scripts_dict
from core.sub import Sub


Youmu_test = scripts_dict.get("Youmu_test")
ykl = scripts_dict.get("Yukari_L")
March = scripts_dict.get("March_default")
ma = scripts_dict.get("Youmu_ma")
Youmu_test.set_mode("number", 1)
Yukari_H = scripts_dict.get("Yukari_H")


def main(sel):
    Sub.start()
    if sel == 0:
        March()
        Sub.stop()
        sleep(5 * 60)
    elif sel == 1:
        pass
    if sel == 2:
        ma.run()
        March()
    elif sel == 3:
        for i in ykl[::-1]:
            i.run()
            March()
    Sub.stop()


if __name__ == "__main__":
    Sub.start()
    while 1:
        main(1)
