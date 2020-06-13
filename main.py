# -*- coding:utf-8 -*-
from time import sleep
from core.scripts import scripts_dict, page_goto
from core.sub import Sub


Youmu_test = scripts_dict.get("Youmu_test")
ykl = scripts_dict.get("Yukari_L")
March = scripts_dict.get("March_default")


def main(sel):
    Sub.start()
    if sel == 0:
        March()
        Sub.stop()
        sleep(5 * 60)
    elif sel == 3:
        for i in ykl:
            i.set_mode("time", 30)
        for i in ykl:
            March()
            i.run()

    Sub.stop()


if __name__ == "__main__":
    Sub.start()
    while 1:
        main(0)
    # page_goto("MAIN")
