class OvertimeError(RuntimeError):
    '''while超时'''

    def __init__(self, errortype='undefined'):
        super().__init__(self)
        errortype = errortype+' ERROR:OVERTIME'
        self.type = errortype

    def __str__(self):
        return self.type


class Gameerror(RuntimeError):
    '''超时错误处理超时'''

    def __init__(self, errortype='undefined'):
        super().__init__(self)
        errortype = errortype + ' ERROR:OVERTIME again'
        self.type = errortype

    def __str__(self):
        return self.type
