# -*- coding:utf-8 -*-
import cv2
import pyperclip


global img
global point1, point2


def on_mouse(event, x, y, flags, param):
    global img, point1, point2
    img2 = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:  # 左键点击
        point1 = (x, y)
        cv2.circle(img2, point1, 10, (0, 255, 0), 2)
        cv2.imshow("cut", img2)
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):  # 按住左键拖曳
        cv2.rectangle(img2, point1, (x, y), (255, 0, 0), 2)
        cv2.imshow("cut", img2)
    elif event == cv2.EVENT_LBUTTONUP:  # 左键释放
        point2 = (x, y)
        cv2.rectangle(img2, point1, point2, (0, 0, 255), 2)
        cv2.imshow("cut", img2)
        min_x = min(point1[0], point2[0])
        min_y = min(point1[1], point2[1])
        width = abs(point1[0] - point2[0])
        height = abs(point1[1] - point2[1])
        y0 = min_y
        y1 = min_y + height
        x0 = min_x
        x1 = min_x + width
        cut_img = img[y0:y1, x0:x1]
        string = "cut_image(%d, %d, %d, %d, get_img())" % (y0, y1, x0, x1)
        pyperclip.copy(string)
        print(string)
        cv2.imwrite("1.jpg", cut_img)


def main():
    global img
    img = cv2.imread("x.jpg")
    cv2.namedWindow("cut", 0)
    cv2.setMouseCallback("cut", on_mouse)
    cv2.imshow("cut", img)
    cv2.resizeWindow("cut", 800, 450)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
