# -*- coding:utf-8 -*-
import time


def mathc_img(image, target, value):  # 图像匹配
    import cv2
    import numpy as np
    # 加载原始RGB图像
    img_rgb = cv2.imread(image)
    # 创建一个原始图像的灰度版本，所有操作在灰度版本中处理，然后在RGB图像中使用相同坐标还原
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    # 加载将要搜索的图像模板
    template = cv2.imread(target, 0)
    # 记录图像模板的尺寸
    w, h = template.shape[::-1]
    # 使用matchTemplate对原始灰度图像和图像模板进行匹配
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    # 设定阈值
    threshold = value
    loc = np.where(res >= threshold)
    x = loc[1][0] + (w // 2)
    y = loc[0][0] + (h // 2)
    # print(x, y)
    return x, y


# 图像裁剪cut_image("screenshot.jpg","test.jpg")
def cut_image(y0, y1, x0, x1, path_image1, path_image2):
    import cv2
    img = cv2.imread(path_image1)
    cropped = img[0:128, 0:512]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite(path_image2, cropped)


def compare_image(path_image1, path_image2):  # 图片比较
    from skimage.measure import compare_ssim as ssim
    import cv2
    import warnings

    warnings.filterwarnings("ignore")
    imageA = cv2.imread(path_image1)
    imageB = cv2.imread(path_image2)

    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    (score, diff) = ssim(grayA, grayB, full=True)
    # print("SSIM: {}".format(score))
    return score
    # compare_image = CompareImage()
    # compare_image.compare_image("1.png", "2.png")


def screenshot():  # 截图
    from PyQt5.QtWidgets import QApplication
    import win32gui
    import sys
    app = QApplication(sys.argv)
    app = app
    hwnd = win32gui.FindWindow(None, 'MI 9 SE')
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(hwnd).toImage()
    img = img.copy(0, 52, 1920, 896)
    img.save("temp.jpg")


class adb:
    def order(order):  # adb调用
        import subprocess
        adb_return = subprocess.Popen(order)
        return adb_return

    def click(x, y):
        adb_return = adb.order('adb shell input tap %d %d' % (x, y))
        time.sleep(0.5)
        return adb_return


class game:
    def attack(value):
        if value == 1:
            adb_return = adb.click()  # 普通攻击1
        else:
            adb_return = adb.click()  # 普通攻击2
        time.sleep(0.5)
        return adb_return

    def card(value):
        if value == 1:
            adb_return = adb.click()  # 符卡1
        elif value == 2:
            adb_return = adb.click()  # 符卡2
        elif value == 3:
            adb_return = adb.click()  # 符卡3
        else:
            pass
        return adb_return

    def graze(value):
        # 当前结界数量
        if value == 1:
            adb_return = adb.click()  # 结界1
        elif value == 2:
            adb_return = adb.click()  # 结界2
        elif value == 3:
            adb_return = adb.click()  # 结界3
        else:
            pass
        return adb_return

    def boost(value):
        # 当前p点
        if value == 1:
            adb_return = adb.click()  # boost1
        elif value == 2:
            adb_return = adb.click()  # boost2
        elif value == 3:
            adb_return = adb.click()  # boost3
        else:
            pass
        return adb_return

    def skill(value):
        if value == 1.1:
            adb_return = adb.click()
        elif value == 1.2:
            adb_return = adb.click()
        elif value == 1.3:
            adb_return = adb.click()
        elif value == 2.1:
            adb_return = adb.click()
        elif value == 2.2:
            adb_return = adb.click()
        elif value == 2.3:
            adb_return = adb.click()
        elif value == 3.1:
            adb_return = adb.click()
        elif value == 3.2:
            adb_return = adb.click()
        elif value == 3.3:
            adb_return = adb.click()
        else:
            pass
        return adb_return
