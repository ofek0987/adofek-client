from abc import ABC
from abc import abstractmethod
from adofek_client.users.user import IUser
from adofek_client.message_status import MessageStatus


class IMessage(ABC):
    """Interface representing all the messages that can
    be sent/received, for example a text message"""

    def __init__(self, identifier: str, sender: IUser, receiver: IUser):
        self.identifier = identifier
        self.sender = sender
        self.receiver = receiver

    @abstractmethod
    def update_status(self, status: MessageStatus):
        pass


