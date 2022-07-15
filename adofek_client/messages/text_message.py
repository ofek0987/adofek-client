from adofek_client.messages import message
from adofek_client.users.user import IUser
from adofek_client.message_status import MessageStatus


class TextMessage(message.IMessage):
    def __init__(self, identifier: str, sender: IUser, receiver: IUser, text: str, status: MessageStatus):
        super().__init__(identifier, sender, receiver)
        self._text = text
        self._status = status

    @property
    def getText(self) -> str:
        return self._text

    def update_status(self, status: MessageStatus):
        self._status = status
