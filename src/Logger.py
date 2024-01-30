from enum import Enum
import datetime as dt

class LogLevel(Enum):
    LL_Trace = 0
    LL_Info = 1
    LL_Warning = 2
    LL_Error = 3

class Logger:
    logs = []

    def __init__(self, level: LogLevel) -> None:
        self.loglevel = level

    def WriteLog(self, level: LogLevel, message: str):
        if level  < self.loglevel: 
            return

        log = {"level": level, "time": dt.datetime, "message": message}
        print(log)
        self.logs.append(log)

CurrentLogger = Logger(LogLevel.LL_Trace)