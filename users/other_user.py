import db
from messages import message


class OtherUser:

    db:db

    def get_messages_history(self) -> list[message]:
        pass