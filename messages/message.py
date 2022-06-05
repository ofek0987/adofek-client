from abc import ABC

from users.user import IUser


class IMessage(ABC):
    """Interface representing all the messages that can be sent/received, for example a text message"""
    def __init__(self, identifier: str, sender: IUser, receiver: IUser):
        self.identifier = identifier
        self.sender = sender
        self.receiver = receiver


