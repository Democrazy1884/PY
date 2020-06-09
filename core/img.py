import os
import cv2

dirname = os.path.split(os.path.abspath(__file__))[0]
img_dict = {
    # 选关界面判断
    "FIGHT": cv2.imread(dirname + "\\IMG\\fight.jpg"),
    "FIGHT1": cv2.imread(dirname + "\\IMG\\fight.jpg"),
    # 出发界面判断
    "GO": cv2.imread(dirname + "\\IMG\\go.jpg"),
    # 战斗判断用 boost
    "BOOST": cv2.imread(dirname + "\\IMG\\boost.jpg"),
    # 战斗结束判断
    "END": cv2.imread(dirname + "\\IMG\\end.jpg"),
    # 满血判断
    "FULL": cv2.imread(dirname + "\\IMG\\full.jpg"),
    # 再打一次判断
    "NEXT": cv2.imread(dirname + "\\IMG\\next.jpg"),
    "AGAIN": cv2.imread(dirname + "\\IMG\\again.jpg"),
    # 出水判断
    "WATER": cv2.imread(dirname + "\\IMG\\water.jpg", 0),
    # 断网判断
    "OFFLINE": cv2.imread(dirname + "\\IMG\\offline.jpg"),
    # 耗油判断
    "POWERFIND": (
        cv2.imread(dirname + "\\IMG\\power\\5.jpg"),
        cv2.imread(dirname + "\\IMG\\power\\6.jpg"),
        cv2.imread(dirname + "\\IMG\\power\\7.jpg"),
        cv2.imread(dirname + "\\IMG\\power\\8.jpg"),
        cv2.imread(dirname + "\\IMG\\power\\8.jpg"),
        cv2.imread(dirname + "\\IMG\\power\\10.jpg"),
        cv2.imread(dirname + "\\IMG\\power\\11.jpg"),
        cv2.imread(dirname + "\\IMG\\power\\12.jpg"),
        cv2.imread(dirname + "\\IMG\\power\\13.jpg"),
        cv2.imread(dirname + "\\IMG\\power\\14.jpg"),
        cv2.imread(dirname + "\\IMG\\power\\15.jpg"),
        cv2.imread(dirname + "\\IMG\\power\\16.jpg"),
        cv2.imread(dirname + "\\IMG\\power\\17.jpg"),
        cv2.imread(dirname + "\\IMG\\power\\18.jpg"),
        cv2.imread(dirname + "\\IMG\\power\\19.jpg"),
        cv2.imread(dirname + "\\IMG\\power\\20.jpg"),
    ),
    # 队伍判断
    "TEAMFIND": (
        cv2.imread(dirname + "\\IMG\\1.jpg"),
        cv2.imread(dirname + "\\IMG\\2.jpg"),
        cv2.imread(dirname + "\\IMG\\3.jpg"),
        cv2.imread(dirname + "\\IMG\\4.jpg"),
        cv2.imread(dirname + "\\IMG\\5.jpg"),
    ),
    # 难度hard的图
    "HARD": cv2.imread(dirname + "\\IMG\\hard.jpg"),
    # 难度lunatic的图
    "LUNATIC": cv2.imread(dirname + "\\IMG\\lunatic.jpg"),
    # 难度normal的图
    "NORMAL": cv2.imread(dirname + "\\IMG\\normal.jpg"),
    # boost数字判断
    "BOOSTNUMBER": (
        cv2.imread(dirname + "\\IMG\\zero.jpg"),
        cv2.imread(dirname + "\\IMG\\one.jpg"),
        cv2.imread(dirname + "\\IMG\\two.jpg"),
        cv2.imread(dirname + "\\IMG\\three.jpg"),
    ),
    # 远征切小图基准点判断
    "LV": cv2.imread(dirname + "\\IMG\\lv.jpg", 0),
    # 远征界面判断
    "MARCHPAGE": cv2.imread(dirname + "\\IMG\\marchpage.jpg"),
    # 远征完成
    "DONE": cv2.imread(dirname + "\\IMG\\done.jpg", 0),
    # 远征中
    "WORKING": cv2.imread(dirname + "\\IMG\\working.jpg", 0),
    # 远征出发按钮
    "YES": cv2.imread(dirname + "\\IMG\\yes.jpg", 0),
    # 远征加人物
    "ADDGIRL": cv2.imread(dirname + "\\IMG\\addgirl.jpg", 0),
    # 技能书判断
    "BOOK": cv2.imread(dirname + "\\IMG\\l1.jpg", 0),
    # 普通结晶
    "GOLD1": cv2.imread(dirname + "\\IMG\\l2.jpg", 0),
    # 麻将
    "CARD": cv2.imread(dirname + "\\IMG\\l3.jpg", 0),
    # 灵力
    "POWER": cv2.imread(dirname + "\\IMG\\l4.jpg", 0),
    # 特殊结晶
    "GOLD2": cv2.imread(dirname + "\\IMG\\l5.jpg", 0),
    # 收远征时远征判断
    "MARCHDONE": cv2.imread(dirname + "\\IMG\\marchdone.jpg", 0),
    # 开始界面
    "FIRST": cv2.imread(dirname + "\\IMG\\first.jpg"),
    # 远征红点
    "MARCH": cv2.imread(dirname + "\\IMG\\march.jpg"),
    # 主界面
    "MAIN": cv2.imread(dirname + "\\IMG\\main.jpg"),
    # 设施红点判断
    "BUILDING": cv2.imread(dirname + "\\IMG\\building.jpg"),
    # 道场红点判断
    "SKILLROOM": cv2.imread(dirname + "\\IMG\\skillpoint.jpg"),
    # 道场确定
    "SKILLPOINT": cv2.imread(dirname + "\\IMG\\skillyes.jpg", 0),
    # 三个远征满了判断
    "M3": cv2.imread(dirname + "\\IMG\\3m.jpg"),
    # 道场技能150
    "EXP": cv2.imread(dirname + "\\IMG\\150exp.jpg", 0),
    # 四个特殊远征判断
    "TEAM4": cv2.imread(dirname + "\\IMG\\4team.jpg"),
    # 五个特殊远征判断
    "TEAM5": cv2.imread(dirname + "\\IMG\\5team.jpg"),
}
