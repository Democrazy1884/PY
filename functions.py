# -*- coding:utf-8 -*-
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
def cut_image(y0, y1, x0, x1, path_image1):
    import cv2
    if isinstance(path_image1, str):
        img = cv2.imwrite(path_image1)
    img = path_image1
    cropped = img[y0:y1, x0:x1]  # 裁剪坐标为[y0:y1, x0:x1]
    return cropped


def compare_image(path_image1, path_image2):  # 图片比较
    from skimage.measure import compare_ssim as ssim
    import cv2
    import warnings

    if isinstance(path_image1, str):
        imageA = cv2.imwrite(path_image1)
    if isinstance(path_image2, str):
        imageB = cv2.imwrite(path_image2)
    warnings.filterwarnings("ignore")
    imageA = path_image1
    imageB = path_image2

    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    (score, diff) = ssim(grayA, grayB, full=True, multichannel=True)
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
    img = convertQImageToMat(img)
    return img


def convertQImageToMat(incomingImage):
    '''  Converts a QImage into an opencv MAT format  '''
    import numpy as np
    incomingImage = incomingImage.convertToFormat(4)

    width = incomingImage.width()
    height = incomingImage.height()

    ptr = incomingImage.bits()
    ptr.setsize(incomingImage.byteCount())
    arr = np.array(ptr).reshape(height, width, 4)  # Copies the data
    return arr


class adb:
    def order(order):  # adb调用
        import subprocess
        adb_return = subprocess.Popen(order)
        return adb_return

    def click(x, y):
        import random
        import time
        x = x + random.randint(-40, 40)
        y = y + random.randint(-20, 20)
        adb_return = adb.order('adb shell input tap %d %d' % (x, y))
        time.sleep(0.7)
        return adb_return


class game:
    def attack(value):
        import time
        if value == 1:
            adb_return = adb.click(885, 878)  # 普通攻击1
        else:
            adb_return = adb.click(1485, 880)  # 普通攻击2
        time.sleep(0.5)
        return adb_return

    def card(value):
        import time
        adb_return = adb.click(461, 716)
        time.sleep(0.7)
        if value == 1:
            adb_return = adb.click(669, 591)  # 符卡1
        elif value == 2:
            adb_return = adb.click(984, 494)  # 符卡2
        elif value == 3:
            adb_return = adb.click(1241, 347)  # 符卡3
        else:
            pass
        time.sleep(1.5)
        return adb_return

    def graze(value):
        # 当前结界数量
        if value >= 1:
            adb_return = adb.click(2080, 631)  # 结界1
        elif value >= 2:
            adb_return = adb.click(2080, 631)  # 结界2
        elif value >= 3:
            adb_return = adb.click(2080, 631)  # 结界3
        else:
            pass
        return adb_return

    def boost(value):
        # 当前p点
        if value >= 1:
            adb_return = adb.click(1959, 846)  # boost1
        elif value >= 2:
            adb_return = adb.click(1959, 846)  # boost2
        elif value >= 3:
            adb_return = adb.click(1959, 846)  # boost3
        else:
            pass
        return adb_return

    def skill(value):
        adb_return = adb.click(2182, 806)
        for i in range(0, len(value)):
            if value[i] == 1.1:
                adb_return = adb.click(657, 891)
            elif value[i] == 1.2:
                adb_return = adb.click(804, 891)
            elif value[i] == 1.3:
                adb_return = adb.click(932, 890)
            elif value[i] == 2.1:
                adb_return = adb.click(1155, 886)
            elif value[i] == 2.2:
                adb_return = adb.click(1319, 895)
            elif value[i] == 2.3:
                adb_return = adb.click(1451, 900)
            elif value[i] == 3.1:
                adb_return = adb.click(1690, 895)
            elif value[i] == 3.2:
                adb_return = adb.click(1824, 893)
            elif value[i] == 3.3:
                adb_return = adb.click(1957, 885)
            else:
                pass
            adb_return = adb.click(1507, 837)
        adb_return = adb.click(2182, 806)
        return adb_return
