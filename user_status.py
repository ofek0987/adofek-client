from enum import auto
from enum import Enum


class UserStatus(Enum):
    """Enum representing a user's availability status."""
    OFFLINE = auto()
    ONLINE = auto()
    DO_NOT_DISTURB = auto()
