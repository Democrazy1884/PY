class OvertimeError(RuntimeError):
    def __init__(self, errortype='undefined'):
        super().__init__(self)
        errortype = errortype+' ERROR:OVERTIME'
        self.type = errortype

    def __str__(self):
        return self.type
