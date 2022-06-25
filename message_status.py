from enum import auto
from enum import Enum


class MessageStatus(Enum):
    RECEIVED = auto()
    PENDING = auto()
    SENT = auto()
    FAILED = auto()
