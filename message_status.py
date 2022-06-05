from enum import Enum, auto


class MessageStatus(Enum):
    RECEIVED = auto()
    PENDING = auto()
    SENT = auto()
    FAILED = auto()