import functions
import time


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

def fight():
    
fight()
