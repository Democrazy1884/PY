# -*- coding:utf-8 -*-
# 日常刷远征
from time import sleep, time
from core.scripts import scripts_dict
from core.sub import Sub

March = scripts_dict.get("March_default")
Yukari_H = scripts_dict.get("Yukari_H")
Yukari_H.set_mode("power", 56)

Sub.start()
while True:
    timeUse = Yukari_H.run()
    March()
    marchTime = time()
    while True:
        sleeped_time = time() - marchTime
        if sleeped_time >= 600:
            March()
        sleep(30)
        if time() - marchTime > 60 * 40 - timeUse:
            break
