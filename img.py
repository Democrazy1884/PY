# -*- coding:utf-8 -*-


def mathc_img(image, target, value):
    '''图像匹配'''
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


def cut_image(y0, y1, x0, x1, path_image1):
    '''图像裁剪'''
    import cv2
    if isinstance(path_image1, str):
        img = cv2.imwrite(path_image1)
    img = path_image1
    cropped = img[y0:y1, x0:x1]  # 裁剪坐标为[y0:y1, x0:x1]
    return cropped


def compare_image(path_image1, path_image2):
    '''图片比较'''
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


def screenshot():
    '''截图'''
    from PyQt5.QtWidgets import QApplication
    import win32gui
    import sys
    app = QApplication(sys.argv)
    app = app
    hwnd = win32gui.FindWindow(None, '雷电模拟器')
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(hwnd).toImage()
    img = img.copy(1, 34, 1600, 900)
    img = convertQImageToMat(img)
    return img


def convertQImageToMat(incomingImage):
    '''图像坐标匹配'''
    '''  Converts a QImage into an opencv MAT format  '''
    import numpy as np
    incomingImage = incomingImage.convertToFormat(4)

    width = incomingImage.width()
    height = incomingImage.height()

    ptr = incomingImage.bits()
    ptr.setsize(incomingImage.byteCount())
    arr = np.array(ptr).reshape(height, width, 4)  # Copies the data
    return arr