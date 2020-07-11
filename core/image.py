# -*- coding:utf-8 -*-
import time
from PyQt5.QtWidgets import QApplication
import cv2
import numpy as np
import win32gui
import sys
from core.img import img_dict
from skimage.metrics import structural_similarity as ssim


def clock(func):
    def clocked(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return clocked


def mathc_img(image: np.ndarray, target, value=0.8):
    """图像匹配"""

    # 加载原始RGB图像
    if isinstance(image, str):
        img_rgb = cv2.imread(image)
    else:
        img_rgb = image
    # 创建一个原始图像的灰度版本，所有操作在灰度版本中处理，然后在RGB图像中使用相同坐标还原
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    # 加载将要搜索的图像模板
    if isinstance(target, str):
        template = img_dict.get(target)
    else:
        template = target
    # template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    # 记录图像模板的尺寸
    w, h = template.shape[::-1]
    # 使用matchTemplate对原始灰度图像和图像模板进行匹配
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    # 设定阈值
    threshold = value
    loc = np.where(res >= threshold)
    x = loc[1] + (w // 2)
    y = loc[0] + (h // 2)
    point = []
    for num in range(0, len(x)):
        point.append((x[num], y[num]))
    return point


def cut_image(y0, y1, x0, x1, path_image1):
    """图像裁剪"""

    if isinstance(path_image1, str):
        img = cv2.imwrite(path_image1)
    img = path_image1
    cropped = img[y0:y1, x0:x1]  # 裁剪坐标为[y0:y1, x0:x1]
    return cropped


def compare_image(imageA, imageB):
    """图片比较"""
    if isinstance(imageA, str):
        imageA = cv2.imwrite(imageA)
    if isinstance(imageB, str):
        imageB = cv2.imwrite(imageB)
    # cv2.imwrite("1.jpg", imageA)
    # cv2.imwrite("2.jpg", imageB)
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    (score, diff) = ssim(grayA, grayB, full=True, multichannel=True)
    # print("SSIM: {}".format(score))
    return score


app = QApplication(sys.argv)


# @clock
def screenshot(app=app):
    """截图"""
    hwnd = win32gui.FindWindow(None, "雷电模拟器")
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(hwnd).toImage()
    img = img.copy(1, 34, 1600, 900)
    img = convertQImageToMat(img)
    cv2.imwrite("1.jpg", img)
    return img


def convertQImageToMat(incomingImage):
    """  Converts a QImage into an opencv MAT format  """
    incomingImage = incomingImage.convertToFormat(4)

    width = incomingImage.width()
    height = incomingImage.height()

    ptr = incomingImage.bits()
    ptr.setsize(incomingImage.byteCount())
    arr = np.array(ptr).reshape(height, width, 4)  # Copies the data
    return arr


if __name__ == "__main__":
    pass
