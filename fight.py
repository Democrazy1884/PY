import functions
import time
import cv2
import sys


def firstfight():
    # 点战斗
    functions.adb.click(2121, 869)
    # 选故事
    time.sleep(2)
    functions.adb.click(1372, 972)
    # 选关
    functions.adb.click(1669, 274)
    time.sleep(2)
    # 难度hard
    functions.adb.click(1000, 981)
    # 开始
    functions.adb.click(1669, 274)
    functions.adb.click(1684, 494)


def startjudge():  # 选关界面判断
    while True:
        time.sleep(1)
        img = functions.screenshot()
        offlinejudge(img)
        img = functions.cut_image(781, 830, 1006, 1248, img)
        x = functions.compare_image(img, FIGHT)
        if x >= 0.8:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            time.sleep(1)
            functions.adb.click(1669, 274)  # 选关操作
            # 选关程序待写
            # functions.adb.order('adb shell input swipe 1432 730  1428 256 500')
            # time.sleep(1)
            break


def gojudge():  # 开始界面判断
    while True:
        time.sleep(1)
        img = functions.screenshot()
        offlinejudge(img)
        img = functions.cut_image(742, 831, 1473, 1747, img)
        x = functions.compare_image(img, GO)
        if x >= 0.8:
            time.sleep(1)
            functions.adb.click(1892, 940)  # 出发操作
            break


def boostjudge(img):  # 找boost
    img = functions.cut_image(687, 780, 1525, 1674, img)
    x = functions.compare_image(img, BOOST)
    if x >= 0.8:  # boost 找到了
        return True
    else:  # boost 没找到
        return False


def endjudge(img):  # 结束判断
    img = functions.cut_image(160, 216, 878, 1102, img)
    x = functions.compare_image(img, END)
    if x >= 0.8:
        return True
    else:
        return False


def fulljudge(img):
    img = functions.cut_image(143, 154, 640, 646, img)
    x = functions.compare_image(img, FULL)
    if x >= 0.8:
        return True
    else:
        return False


def offlinejudge(img):  # 断网判定
    img = functions.cut_image(394, 675, 629, 1329, img)
    x = functions.compare_image(img, OFFLINE)
    if x >= 0.9:
        functions.adb.click(1424, 765)  # 断网重连操作


def judge():  # 中场判断
    time.sleep(5)
    while (1):
        img = functions.screenshot()
        boostvalue = boostjudge(img)
        endvalue = endjudge(img)
        fullvalue = fulljudge(img)
        offlinejudge(img)
        if boostvalue is True and fullvalue is True:  # 残血
            return 'not full'
            break
        if boostvalue is True and fullvalue is False:
            return 'full'
            break
        if endvalue is True:  # 找到end
            return 'end'
            break
        time.sleep(1)


def action():
    while True:
        startjudge()
        gojudge()

        word = judge()
        if word == 'full':
            print("WAVE 1")
            functions.game.skill([1.2, 2.1, 3.1])
            functions.game.graze(1)
            functions.game.card(2)
            functions.game.graze(1)
            functions.game.card(2)
            functions.game.graze(1)
            functions.game.card(1)
        word = judge()
        if word == 'not full':
            print("WAVE 2")
            functions.game.skill([1.1])
            functions.game.graze(1)
            functions.game.card(1)
            functions.game.graze(1)
            functions.game.card(1)
            functions.game.graze(1)
            functions.game.boost(1)
            functions.game.card(2)

        word = judge()
        if word == 'not full':
            print("WAVE 3")
            functions.game.boost(1)
            functions.game.graze(1)
            functions.game.card(3)
            functions.game.graze(1)
            functions.game.card(3)
            functions.game.graze(1)
            functions.game.attack(2)

        word = judge()
        if word == 'end':
            functions.adb.click(500, 500)
            functions.adb.click(500, 500)
            functions.adb.click(500, 500)


BEGIN = cv2.imread(sys.path[0] + '\\IMG\\begin.jpg')
BOOST = cv2.imread(sys.path[0] + '\\IMG\\boost.jpg')
END = cv2.imread(sys.path[0] + '\\IMG\\end.jpg')
FIGHT = cv2.imread(sys.path[0] + '\\IMG\\fight.jpg')
GO = cv2.imread(sys.path[0] + '\\IMG\\go.jpg')
OFFLINE = cv2.imread(sys.path[0] + '\\IMG\\offline.jpg')
START = cv2.imread(sys.path[0] + '\\IMG\\start.jpg')
FULL = cv2.imread(sys.path[0] + '\\IMG\\full.jpg')
action()
