from dataclasses import dataclass

from adofek_client.user_status import UserStatus


@dataclass
class IUser:
    status: UserStatus
    username: str
    def __init__(self, username: str, status: UserStatus = UserStatus.OFFLINE):
        """

        :param username:
        :param status:
        """
        self._username = username
        self._status = status

    def __str__(self) -> str:
        return f"User: {self._username} | status {self._status}"

    def __eq__(self, other) -> bool:
        return self._username == other._username

    def __ne__(self, other) -> bool:
        return not self == other

    @property
    def getStatus(self) -> UserStatus:
        return self._status