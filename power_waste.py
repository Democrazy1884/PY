# -*- coding:utf-8 -*-
# 日常消耗体力
from time import sleep
from core.scripts import scripts_dict
from core.sub import Sub

March = scripts_dict.get("March_default")
Yukari_H = scripts_dict.get("Yukari_H")
Yukari_H.set_mode("power", 56)

Sub.start()
while True:
    timeUse = Yukari_H.run()
    March()
    sleep(200)
