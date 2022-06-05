from users.user import IUser
from user_status import UserStatus


class MyUser(IUser):
    """The user that is used by the local user."""

    def update_status(self, status: UserStatus):
        pass
