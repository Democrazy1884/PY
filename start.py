# -*- coding:utf-8 -*-
from time import sleep

from core.adb import click, order
from core.fight import offlinefind
from core.march import firstpagefind, mainpagefind
from core.sub import Sub

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
