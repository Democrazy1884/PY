# -*- coding:utf-8 -*-
"计划控制"
import threading
import queue

job_queue = queue.PriorityQueue()

"""job 优先级

    1:错误情况
    2:特殊情况
    3:特殊输入
    4:正常输入
    5:程序输入
    结构:
    （优先级(页面，任务)）
"""


class Event:
    remove = threading.Event()
    add = threading.Event()


def sub(job_list):
    while 1:
        Event.remove.wait() or Event.add.wait()
        if Event.remove.isSet():
            pass
        if Event.add.isSet():
            pass


class Plan:
    "计划队列"

    def start(job_list):
        for job in job_list:
            pass

    def stop():
        while 1:
            x = job_queue.get()
            if x:
                pass
            else:
                break

    def add(page, level, data):
        job_queue.put((level, (page, data)))

    def get(page):
        try:
            return job_queue.get_nowait()
        except queue.Empty:
            return


if __name__ == "__main__":
    pass
