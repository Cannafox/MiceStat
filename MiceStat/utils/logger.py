import datetime
from enum import Enum


class MessageType(Enum):
    INFO = "[I]"
    WARNING = "[W]"
    ERROR = "[I]"
    DEFAULT = "[ ]"


# class MessageSymbol(Enum):
#     INFO = "[I]"
#     WARNING = "[W]"
#     ERROR = "[I]"
#     DEFAULT = "[ ]"


class Logger:
    class Message:
        separator = " "

        def __init__(self, id, severity, timestamp, message):
            self.id = id
            self.severity = severity
            self.timestamp = timestamp
            self.message = message

        def __str__(self):
            representation = f"" \
                            f"{self.severity.value}{self.separator}" \
                            f"{self.timestamp}{self.separator}" \
                            f"{self.id}{self.separator}" \
                            f": {self.message}"

            return representation

    def __init__(self, id):
        self.id = id
        self.history = []

    def log_message(self, message, severity, display):
        timestamp = datetime.datetime.now()
        message = self.Message(self.id, severity, timestamp, message)
        self.history.append(message)
        if display:
            print(message)
        return message

    def info(self, message, display=True):
        return self.log_message(message, MessageType.INFO, display=display)

    def warning(self, message, display=True):
        return self.log_message(message, MessageType.WARNING, display=display)

    def error(self, message, display=True):
        return self.log_message(message, MessageType.ERROR, display=display)


class LoggerFactory:
    _loggers = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(LoggerFactory, cls).__new__(cls)
        return cls.instance

    @classmethod
    def create_logger(cls, obj):
        class_name = obj.__class__.__name__
        logger = Logger(class_name)
        assert class_name not in cls._loggers.keys()
        cls._loggers[class_name] = logger

        return logger
