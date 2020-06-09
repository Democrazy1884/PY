# -*- coding:utf-8 -*-
"各种通用的函数库"
from image import compare_image, cut_image
from sub import get_img
import numpy as np


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


def search(y0: int, y1: int, x0: int, x1: int, img1, img2, value: float):
    """通用图像对比

    Args:
        y0,y1,x0,x1 (int): 对比区域四角坐标
        img1 (np.ndarray/get_img): 被裁剪的图
        img2 (np.ndarray): 被对比的图
        value (float): 相似度

    Returns:
        [bool]: [符合返回真，不符合返回假]
    """
    if img1 is get_img:
        cut_img = cut_image(y0, y1, x0, x1, img1())
    else:
        cut_img = cut_image(y0, y1, x0, x1, img1)
    if isinstance(img2, np.ndarray):
        x = compare_image(cut_img, img2)
        if x >= value:
            return True
        else:
            return False
    if isinstance(img2, tuple):
        x = []
        for img in img2:
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


class Page(object):
    "界面"
    __slots__ = ("find", "action", "next_page", "ret")

    def __init__(self, find, action, next_page, ret):
        "初始化"
        self.find = find
        self.action = action
        self.next_page = next_page
        self.ret = ret


class First(Page):
    "初始界面"

    def __init__(self):
        def find():
            pass

        def action():
            pass

        def next_page():
            pass

        def ret():
            pass

        super().__init__(find, action, next_page, ret)


if __name__ == "__main__":
    from random import shuffle

    d = [
        (605, 219),
        (604, 220),
        (605, 220),
        (606, 220),
        (604, 221),
        (605, 221),
        (606, 221),
        (604, 222),
        (605, 222),
        (606, 222),
        (604, 223),
        (605, 223),
        (606, 223),
        (604, 224),
        (605, 224),
        (606, 224),
        (604, 225),
        (605, 225),
        (606, 225),
        (604, 226),
        (605, 226),
        (606, 226),
        (604, 455),
        (605, 455),
        (604, 456),
        (605, 456),
        (606, 456),
        (604, 457),
        (605, 457),
        (606, 457),
        (604, 458),
        (605, 458),
        (606, 458),
        (604, 459),
        (605, 459),
        (606, 459),
        (604, 460),
        (605, 460),
        (606, 460),
        (604, 461),
        (605, 461),
        (606, 461),
        (604, 462),
        (605, 462),
        (606, 462),
        (605, 690),
        (604, 691),
        (605, 691),
        (606, 691),
        (604, 692),
        (605, 692),
        (606, 692),
        (604, 693),
        (605, 693),
        (606, 693),
        (604, 694),
        (605, 694),
        (606, 694),
        (604, 695),
        (605, 695),
        (606, 695),
        (604, 696),
        (605, 696),
        (606, 696),
        (604, 697),
        (605, 697),
        (606, 697),
        (605, 698),
    ]
    shuffle(d)
    d2 = remove_same2(d)
    print(d2)
