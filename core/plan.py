# -*- coding:utf-8 -*-
import threading
import queue

march_job = queue.PriorityQueue()
fight_job = queue.PriorityQueue()
main_job = queue.PriorityQueue()


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

    def start():
        pass

    def stop():
        pass

    def add():
        pass

    def done():
        pass

    def get(page):
        if page == "Main":
            return main_job.get()
        if page == "March":
            return march_job.get()
        if page == "Fight":
            return fight_job.get()
        else:
            return 0


def march_plan():
    pass


main_job.put("march")
march_job.put([1, 1])

if __name__ == "__main__":
    Event.remove.set()

    Event.remove.wait()
    print("yes")
