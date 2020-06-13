# -*- coding:utf-8 -*-
"计划控制"
import queue

job_queue = queue.PriorityQueue()

"""job 优先级

    1:错误情况
    2:特殊情况
    3:特殊输入
    4:正常输入
    5:程序输入
    6:自动继续
    7:任务完成
    结构:
    (优先级,(页面,任务类型,任务赋值))
    页面:Fight,Main,March
"""


class Plan:
    "计划"

    def add(level, page, mode, data):
        """添加任务 优先级 页面 任务类型 任务赋值

        :level: 1错误情况 2特殊情况 3特殊输入 4正常输入 5程序输入 6自动继续

        :page: Fight Main March

        """
        job_queue.put((level, (page, mode, data)))

    def get():
        "取得任务"
        try:
            return job_queue.get_nowait()
        except queue.Empty:
            return (None, None)

    def done():
        "完成任务"
        job_queue.task_done()


def fight_initialize(data):
    "战斗初始化"
    Plan.add(3, "Fight", "initialize", data)


def fight_control(data):
    "战斗控制"
    Plan.add(4, "Fight", "control", data)


def march_initialize(data):
    "远征初始化"
    Plan.add(3, "March", "initialize", data)


if __name__ == "__main__":
    pass
