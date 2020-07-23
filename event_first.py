# -*- coding:utf-8 -*-
# 新图推图机
from core.scripts import scripts_dict
from core.sub import Sub

march = scripts_dict.get("March_default")
Youmu_test = scripts_dict.get("Youmu_test")
# 队伍设置
Youmu_test.team = 2

Sub.start()
while True:
    Youmu_test.run()
    march.start()
