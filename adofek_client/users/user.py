from dataclasses import dataclass

from user_status import UserStatus


@dataclass
class IUser:
    status: UserStatus
    username: str
