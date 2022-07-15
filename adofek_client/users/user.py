from dataclasses import dataclass

from adofek_client.user_status import UserStatus


@dataclass
class IUser:
    username: str
    status: UserStatus

    @property
    def getStatus(self) -> UserStatus:
        return self.status

    @property
    def getUsername(self) -> str:
        return self.username

    @getStatus.setter
    def getStatus(self, status: UserStatus):
        self.status = status
