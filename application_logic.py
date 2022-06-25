from contacts_collection import ContactsCollection
from users.user import IUser


class ApplicationLogic:
    """Handle events from gui class."""

    def __init__(self, my_user: IUser, contacts: ContactsCollection):
        self.my_user = my_user
        self.contacts = contacts
