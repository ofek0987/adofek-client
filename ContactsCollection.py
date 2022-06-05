import OtherUser
import DB

class ContactsCollection:
    contacts: dict[str,OtherUser]
    db: DB

    def add_contact(self,user):
        pass

    def get_all_contacts(self) -> list:
        pass

    def get_contacts_by_username(self,username) -> OtherUser:
        pass
