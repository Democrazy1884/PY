# -*- coding:utf-8 -*-
"各种通用的函数库"
import numpy as np

from core.image import compare_image, cut_image
from core.sub import get_img
from core.img import img_dict


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


def search(y0: int, y1: int, x0: int, x1: int, mode: str, value: float):
    """通用图像对比

    Args:
        y0,y1,x0,x1 (int): 对比区域四角坐标
        img1 (np.ndarray/get_img): 被裁剪的图
        mode_img (np.ndarray): 被对比的图
        value (float): 相似度

    Returns:
        [bool]: [符合返回真，不符合返回假]
    """
    mode_img = img_dict.get(mode)
    cut_img = cut_image(y0, y1, x0, x1, get_img())
    if isinstance(mode_img, np.ndarray):
        x = compare_image(cut_img, mode_img)
        if x >= value:
            return True
        else:
            return False
    if isinstance(mode_img, tuple):
        x = []
        for img in mode_img:
            x.append(compare_image(cut_img, img))
        if max(x) >= value:
            return x.index(max(x))
        else:
            return False


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
