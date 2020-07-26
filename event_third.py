# -*- coding:utf-8 -*-
# 活动规则3
from core.scripts import scripts_dict
from core.sub import Sub

march = scripts_dict.get("March_default")
last_word = scripts_dict.get("last_word")
card_boost_lastword = scripts_dict.get("card_boost_lastword")
Sub.start()
# 选关

last_word.stage = 1
card_boost_lastword.stage = 1
card_boost_lastword.time = 40

while True:

    last_word.team = 4
    last_word.run()
    march.start()

    last_word.team = 1
    last_word.run()
    march.start()

    last_word.team = 2
    last_word.run()
    march.start()

    card_boost_lastword.team = 3
    card_boost_lastword.run()
    march.start()
