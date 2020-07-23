# -*- coding:utf-8 -*-
# 活动规则
from core.scripts import scripts_dict
from core.sub import Sub

march = scripts_dict.get("March_default")
last_word = scripts_dict.get("last_word")
Sub.start()

while True:
    last_word.team = 1
    last_word.run()
    march.start()
    last_word.team = 2
    last_word.run()
    march.start()
    last_word.team = 3
    last_word.run()
    march.start()
