from core.universe import search
from core.adb import click, click_s
from time import sleep, time
import core.game_log as game_log
from core.gameerror import OvertimeError


def exit_to_main():
    """返回主界面"""
    click_s(1559, 35)
    start = time()
    while 1:
        if time() - start > 60:
            raise OvertimeError("exit")
        offlinefind()
        if search("MAIN"):
            break
        if time() - start > 10:
            click_s(1559, 35)
            sleep(5)
        sleep(1)


def offlinefind():
    """断网判定"""
    if search("OFFLINE"):
        click(963, 632)  # 断网重连操作
        game_log.warning("offline")
        sleep(10)
        return True
    else:
        return False


def MAIN_way(target):
    "从 主页 出发"
    if target == "FIGHT":
        click(1478, 712)
        return "FIGHT"
    elif target == "MARCH":
        click(1380, 534)
        return "MARCH"


def FIGHT_way(target):
    "从 选关 出发"
    exit_to_main()
    return "MAIN"


def GO_way(target):
    "从 选队伍 出发"
    exit_to_main()
    return "MAIN"


def BOOST_way(target):
    "从 战斗 出发"
    click(858, 34, 3)  # 强行中断战斗
    click(1408, 808)
    click(992, 628)
    return "FIGHT"


def END_way(target):
    "从 结束 出发"
    click(500, 500)
    return "NEXT"


def NEXT_way(target):
    "从 结束1 出发"
    click(1415, 813)
    return "FIGHT"


def MARCHPAGE_way(target):
    "从 远征 出发"
    exit_to_main()
    return "MAIN"


def FIRST_way(target):
    "从 初始 出发"
    exit_to_main()
    return "MAIN"


def OFFLINE_way(target):
    "从 断网 出发"
    offlinefind()
    return 0


page_dict = {
    # 主页
    "MAIN": MAIN_way,
    # 战斗选关
    "FIGHT": FIGHT_way,
    # 战斗出发
    "GO": GO_way,
    # 战斗中
    "BOOST": BOOST_way,
    # 结束1
    "END": END_way,
    # 结束2
    "NEXT": NEXT_way,
    # 远征
    "MARCHPAGE": MARCHPAGE_way,
    # 初始界面
    "FIRST": FIRST_way,
    # 断网
    "OFFLINE": OFFLINE_way,
}


def get_now():
    for page in page_dict.keys():
        if search(page):
            return page


def page_goto(target, now=None):
    # 未定义当前页面则需要查找一下
    if not now:
        now = get_now()
    print("{} to {}".format(now, target))
    # 不需要进行跳转
    if now == target:
        return
    # 查找当前页面到目标页面的方法
    func = page_dict.get(now)
    now = func(target)
    if now == target:
        return
    else:
        page_goto(target, now)
