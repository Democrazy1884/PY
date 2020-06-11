# -*- coding:utf-8 -*-
"各种通用的函数库"
import numpy as np
from functools import wraps
from core.image import compare_image, cut_image
from core.sub import get_img
from core.img import img_dict
from time import sleep


def manhattan_dist(p, q):
    """
    曼哈顿距离/绝对距离(L1范数)
    INPUT  -> 长度一致的向量1、向量2
    举例: p = [1,2,6]; q = [1,3,5]
    """
    p = np.mat(p)
    q = np.mat(q)
    # return np.linalg.norm(p-q, ord=1)
    return np.sum(np.abs(p - q))


def searchtypeassert(func):
    "search 输入检查"

    @wraps(func)
    def wrapper(*args, **kwargs):
        # 长度为6时
        if len(args) == 6:
            value = args[5]
            # 输入为图像
            if isinstance(args[4], np.ndarray):
                ret = func(args[0], args[1], args[2], args[3], args[4])
            # 输入为字符串
            elif isinstance(args[4], str):
                mode_img = img_dict.get(args[4])
                return wrapper(args[0], args[1], args[2], args[3], mode_img, args[5])
            # 输入为tuple时
            elif isinstance(args[4], tuple):
                ret_list = []
                for mode_img in args[4]:
                    ret_list.append(func(args[0], args[1], args[2], args[3], mode_img))
                ret = max(ret_list)
                if ret < value:
                    sleep(1)
                    return False
                else:
                    return ret_list.index(ret)
            else:
                raise TypeError()
        # 单个输入时
        elif len(args) == 1 and isinstance(args[0], str):
            i = search_dict.get(args[0])
            return wrapper(i[0], i[1], i[2], i[3], img_dict.get(i[4]), i[5])
        else:
            raise TypeError()
        # 单次运算返回真假
        if ret > value:
            return True
        else:
            return False

    return wrapper


@searchtypeassert
def search(y0, y1, x0, x1, mode_img: np.ndarray):
    """通用图像对比

    Args:
        y0,y1,x0,x1 (int): 对比区域四角坐标
        mode_img(np.ndarray): 图像
        value (float): 相似度

    Returns:
        [float]: [符合返回真，不符合返回假]
    """
    cut_img = cut_image(y0, y1, x0, x1, get_img())
    return compare_image(cut_img, mode_img)


def remove_same2(point: list):
    """删除坐标list中的相似值"""
    # print(point)
    for num1 in range(0, len(point)):
        for num2 in range(num1 + 1, len(point)):
            if (
                abs(point[num1][0] - point[num2][0]) < 20
                and abs(point[num1][1] - point[num2][1]) < 20
            ):
                point[num2] = (0, 0)

    point = list(filter(lambda n: n[0], point))
    # print(point)
    return point


def remove_same(point: list):
    """删除坐标list中的相似值"""
    for p in point:
        n = point.index(p) + 1
        for q in point[n::]:
            if manhattan_dist(p, q) < 20:
                point.remove(q)
    return point


search_dict = {
    # 断网
    "OFFLINE": (390, 485, 626, 960, "OFFLINE", 0.9),
    # 选关界面判断
    "FIGHT": (14, 50, 88, 161, "FIGHT", 0.8),
    "FIGHT1": (14, 50, 88, 161, "FIGHT1", 0.8),
    # 找队伍
    "TEAMFIND": (790, 815, 723, 743, "TEAMFIND", 0.5),
    # 油耗探测
    "POWERFIND": (686, 726, 1371, 1431, "POWERFIND", 0.5),
    # 出发界面判断
    "GO": (754, 830, 1220, 1465, "GO", 0.8),
    # 战斗判断用 boost
    "BOOST": (753, 790, 1259, 1410, "BOOST", 0.7),
    # 战斗结束判断
    "END": (158, 216, 690, 907, "END", 0.4),
    # 满血判断
    "FULL": (140, 150, 529, 534, "FULL", 0.8),
    # 再打一次判断
    "NEXT": (795, 831, 1388, 1465, "NEXT", 0.8),
    "AGAIN": (795, 831, 101, 181, "AGAIN", 0.8),
    # 难度hard的图
    "HARD": (797, 824, 457, 633, "HARD", 0.8),
    # 难度lunatic的图
    "LUNATIC": (797, 824, 457, 633, "LUNATIC", 0.8),
    # 难度normal的图
    "NORMAL": (797, 824, 457, 633, "NORMAL", 0.8),
    # 远征界面判断
    "MARCHPAGE": (13, 48, 89, 231, "MARCHPAGE", 0.8),
    # 开始界面
    "FIRST": (839, 884, 12, 774, "FIRST", 0.5),
    # 远征红点
    "MARCH": (480, 502, 1415, 1445, "MARCH", 0.8),
    # 主界面
    "MAIN": (696, 737, 1424, 1521, "MAIN", 0.8),
    # 设施红点判断
    "BUILDING": (754, 770, 880, 900, "BUILDING", 0.8),
    # 道场红点判断
    "SKILLROOM": (238, 260, 1418, 1430, "SKILLROOM", 0.8),
    # 三个远征满了判断
    "M3": (812, 854, 122, 146, "M3", 0.75),
}
