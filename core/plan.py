# -*- coding:utf-8 -*-
import threading
import Queue

job_list = Queue.PriorityQueue()


class Event:
    remove = threading.Event()
    add = threading.Event()


def plan():
    while 1:
        Event.remove.wait() or Event.add.wait()
        if Event.remove.isSet():
            pass
        if Event.add.isSet():
            pass


class Plan:
    def start():
        pass

    def stop():
        pass

    def add():
        pass

    def remove():
        pass

    def get():
        pass


if __name__ == "__main__":
    Event.remove.set()

    Event.remove.wait()
    print("yes")
