import threading
from image import screenshot
from time import sleep
STEP = 0.4

img = 0


class event():
    stop = threading.Event()  # 子程序结束事件
    done = threading.Event()


def backstage():  # 子线程
    event.stop.clear()
    global img
    img = screenshot()
    event.done.set()
    while True:  # 子线程
        img = screenshot()
        sleep(STEP * 2)
        # print('sub working')
        if event.stop.is_set():
            break


def substart():
    # print('sub start')
    back_stage = threading.Thread(target=backstage, args=())
    back_stage.setDaemon(True)
    back_stage.start()


def get_img():
    event.done.wait()
    return img


def substop():
    # print('sub stop')
    event.stop.set()


if __name__ == "__main__":
    pass
