import time

# import fight
import functions

functions.adb.order('adb devices')
# 解锁
functions.adb.order('adb shell input keyevent 26')
time.sleep(1)
functions.adb.click(300, 300)
time.sleep(1)
# 上滑
functions.adb.order('adb shell input swipe 500 1000 500 20 500')
time.sleep(1)
# 输密码
functions.adb.order('adb shell input text  "132659"')
time.sleep(1)
# 开游戏
functions.adb.order(
    '''adb shell am start -n jp.goodsmile.touhoulostword_android/com.google.firebase.MessagingUnityPlayerActivity'''
)
time.sleep(1)
# 界面判断
while 1:
    functions.screenshot()
    score = functions.compare_image("temp.jpg", "begin.jpg")
    if score >= 0.8:
        print("start")
        functions.adb.click(300, 300)
        break

#
# x, y = functions.mathc_img('1.jpg', "2.jpg", 0.8)#图像匹配
# functions.cut_image()#裁剪
# functions.screenshot()#截图
