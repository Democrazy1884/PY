from core.fight import Fight
from core.march import March_action, offlinefind, exit_to_main
from core.universe import search
from core.adb import click

default = "default"

#       选关  队伍 战斗组
# Fight(int1,int2,int3)
scripts_dict = {
    # 默认远征模式
    "March_default": March_action(1, 1, 1).start,
    # 只续技能书
    "March_skill": March_action.only_skill().start,
    # 只收远征
    "March_receive": March_action.only_receive().start,
    # 只发远征
    "March_send": March_action.only_send().start,
    # 刷L华扇，使用队伍1,3,5
    "Kasen_L": [Fight(1, 1, 5), Fight(1, 3, 5), Fight(1, 5, 5)],
    # 妖梦推图机 使用队伍4
    "Youmu_test": Fight(1, 4, 2),
    # 刷L紫妈
    "Yukari_L": [Fight(1, 1, 4), Fight(1, 2, 6)],
    "Youmu_ma": Fight(3, 4, 7),
    # 活动刷华扇和灵梦
    "event_Kasen": [Fight(1, 4, 9), Fight(1, 5, 9)],
    "event_Kasen_ex": Fight(1, 1, 8),
}


def MAIN_way(target):
    if target == "FIGHT":
        click(1478, 712)
        return "FIGHT"
    elif target == "MARCH":
        click(1380, 534)
        return "MARCH"


def FIGHT_way(target):
    exit_to_main()
    return "MAIN"


def GO_way(target):
    exit_to_main()
    return "MAIN"


def BOOST_way(target):
    click(858, 34, 3)  # 强行中断战斗
    click(1408, 808)
    click(992, 628)
    return "FIGHT"


def END_way(target):
    click(500, 500)
    return "NEXT"


def NEXT_way(target):
    click(1415, 813)
    return "FIGHT"


def MARCHPAGE_way(target):
    exit_to_main()
    return "MAIN"


def FIRST_way(target):
    exit_to_main()
    return "MAIN"


def OFFLINE_way(target):
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
