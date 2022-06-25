from dataclasses import dataclass

from db import DB
from messages.message import IMessage
from users.user import IUser


@dataclass
class OtherUser(IUser):
    """A user that is not the user that is used by the local user."""
    db: DB

    def get_messages_history(self) -> list[IMessage]:
        """Returns all the messages history stored in the database,
         sorted by their's timestamp in descending order."""
        pass
