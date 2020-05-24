from time import sleep
# import fight
from adb import order
order('D:\\leidian\\LDPlayer\\dnplayer.exe')
sleep(60)
order('adb devices')

# 开游戏
order(
    '''adb shell am start -n jp.goodsmile.touhoulostword_android/com.google.firebase.MessagingUnityPlayerActivity'''
)

sleep(1)
# 开始界面判断
# 主页判断
# 红点判断 1技能 2打工 3寺子屋 4战斗
# 滑动程序
