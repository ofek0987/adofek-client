from adofek_client.user_status import UserStatus
from adofek_client.users.user import IUser


class MyUser(IUser):
    """The user that is used by the local user."""

    def update_status(self, status: UserStatus):
        self.status = status
