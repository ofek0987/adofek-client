from dataclasses import dataclass

from adofek_client.db import DB
from adofek_client.messages.message import IMessage
from adofek_client.users.user import IUser


@dataclass
class OtherUser(IUser):
    """A user that is not the user that is used by the local user."""
    db: DB

    def get_messages_history(self) -> list[IMessage]:
        """Returns all the messages history stored in the database,
         sorted by their's timestamp in descending order."""
        pass


