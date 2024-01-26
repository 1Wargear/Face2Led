from enum import Enum
import datetime as dt

class LogLevel(Enum):
    Trace = 0
    Info = 1
    Warning = 2
    Error = 3

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