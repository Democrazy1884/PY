# -*- coding:utf-8 -*-
from time import sleep

from adb import click, order
from fight import offlinefind
from march import firstpagefind, mainpagefind
from sub import Sub

STEP = 0.5
order("D:\\leidian\\LDPlayer\\dnplayer.exe")
sleep(60)
order("adb devices")
order("adb devices")
Sub.start()
# 开游戏
order(
    """adb shell am start -n jp.goodsmile.touhoulostword_android/com.google.firebase.MessagingUnityPlayerActivity"""
)
# 开始界面判断
sleep(10)
while True:
    if firstpagefind():
        click(500, 500)
        break
    offlinefind()
    sleep(STEP)
# 主页判断
while True:
    if mainpagefind():
        break
    offlinefind()
    sleep(STEP)

# 红点判断 1技能 2打工 3寺子屋 4战斗
