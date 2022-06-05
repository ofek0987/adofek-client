from dataclasses import dataclass

from user_status import UserStatus


@dataclass
class IUser:
    Status: UserStatus
    Username: str
