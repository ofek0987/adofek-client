from users.user import IUser
from db import DB


class ContactsCollection:
    """Stores all the contacts and manage them."""
    def __init__(self, db: DB):
        """
        :param db: The local database that stores all the needed information.
        """
        self.db = db
        self._contacts = []

    def add_contact(self, user: IUser):
        pass

    def get_all_contacts(self) -> list[IUser]:
        pass

    def get_contacts_by_username(self, username: str) -> IUser:
        pass
