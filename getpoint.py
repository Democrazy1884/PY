import pyperclip
import cv2
from image import screenshot
import time


def getposHsv(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("HSV is", HSV[y, x])


def getposBgr(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        x = str(x * 2)
        y = str(y * 2)
        string = 'click(' + x + ',' + y + ')'

        print(string)
        pyperclip.copy(string)


while True:
    #   读 取 图 片
    img = screenshot()  # 直接读为灰度图像
    cv2.imwrite('D:\\PY\\x.jpg', img)
    #   缩小图像10倍(因为我的图片太大，所以要缩小10倍方便显示)
    height, width = img.shape[:2]
    size = (width//2, height//2)  # bgr
    img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    # BGR转化为HSV
    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 鼠标点击响应事件
    # cv2.imshow("imageHSV",HSV)
    cv2.imshow('image', img)
    cv2.setMouseCallback("image", getposBgr)
    time.sleep(0.5)
    cv2.waitKey(0)
