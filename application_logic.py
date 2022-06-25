from db import DB
from users.my_user import MyUser


class ApplicationLogic:
    """Handle events from gui class."""

    def __init__(self, my_user: MyUser, db: DB):
        """
        :param my_user: Representing the actual user is logged in to.
        :param contacts: Representing the contacts of the user.
        """
        self.my_user = my_user
        self.db = db
