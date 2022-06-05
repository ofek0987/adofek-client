from users.other_user import OtherUser
from messages.message import IMessage
from users.user import IUser
from contacts_collection import ContactsCollection


class DB:
    """Database management for client."""
    def get_contacts(self) -> ContactsCollection:
        pass

    def get_messages_history_by_user(self, user: IUser) -> list[IMessage]:
        """
        Return message history filtered by a given user.
        :param user: The user to filter the messages by.
        """
        pass

    def add_contact(self, user: OtherUser):
        pass

    def add_message(self, message: IMessage):
        pass
