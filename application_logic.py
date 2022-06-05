from users.user import IUser
from contacts_collection import ContactsCollection


class ApplicationLogic:
    """Handle events from gui class."""

    def __init__(self, my_user: IUser, contacts: ContactsCollection):
        self.my_user = my_user
        self.contacts = contacts
