from core.fight import Fight
from core.march import March_action

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
    "event_Kasen": [
        Fight(1, 4, 9).set_mode("time", 40),
        Fight(1, 1, 9).set_mode("time", 30),
        Fight(1, 5, 9).set_mode("time", 30),
        Fight(1, 2, 8).set_mode("time", 30),
    ],
}
