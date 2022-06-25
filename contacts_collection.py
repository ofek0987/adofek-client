from db import DB
from users.other_user import OtherUser


class ContactsCollection:
    """Stores all the contacts and manage them."""

    def __init__(self, db: DB):
        """
        :param db: The local database that stores all the needed information.
        """
        self.db = db

    def add_contact(self, user: OtherUser):
        pass

    def get_all_contacts(self) -> list[OtherUser]:
        pass

    def get_contacts_by_username(self, username: str) -> OtherUser:
        pass
