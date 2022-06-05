import other_user
import db

class ContactsCollection:
    contacts: dict[str, other_user]
    db: db

    def add_contact(self,user):
        pass

    def get_all_contacts(self) -> list:
        pass

    def get_contacts_by_username(self,username) -> other_user:
        pass
