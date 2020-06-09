# -*- coding:utf-8 -*-
import sys
import threading
from time import sleep

from PyQt5.QtWidgets import QApplication

from core.image import screenshot

STEP = 0.3

img = 0

app = QApplication(sys.argv)


class event:
    stop = threading.Event()  # 子程序结束事件
    done = threading.Event()


def backstage(app):  # 子线程
    event.stop.clear()
    global img
    img = screenshot(app)
    event.done.set()
    while 1:  # 子线程
        img = screenshot(app)
        sleep(STEP * 2)
        # print("sub working")
        if event.stop.is_set():
            break


def get_img():
    """读取图像"""
    event.done.wait()
    return img


class Sub:
    def stop():
        "停止"
        # print("sub stop")
        event.stop.set()

    def start():
        "启动"
        # print("sub start")
        back_stage = threading.Thread(target=backstage, args=(app,))
        back_stage.setDaemon(True)
        back_stage.start()
        return back_stage


if __name__ == "__main__":
    x = Sub.substart()
    x.join()
