# -*- coding:utf-8 -*-
"""自定义的错误"""


class OvertimeError(RuntimeError):
    """超时"""

    def __init__(self, errortype="undefined"):
        super().__init__(self)
        errortype = errortype + " OVERTIME"
        self.type = errortype

    def __str__(self):
        return self.type


class Gameerror(RuntimeError):
    """超时处理超时"""

    def __init__(self, errortype="undefined"):
        super().__init__(self)
        errortype = errortype + " OVERTIME again"
        self.type = errortype

    def __str__(self):
        return self.type


class Watererror(RuntimeError):
    """出水了"""

    def __init__(self, errortype="undefined"):
        super().__init__(self)
        errortype = errortype + " FIND WATER"
        self.type = errortype

    def __str__(self):
        return self.type
