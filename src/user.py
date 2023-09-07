import datetime

DATE_FORMAT = '%d.%m.%Y'


class User:
    def __init__(self, first_name, last_name, user_name, chat_id, member_since=None):
        self._first_name = first_name
        self._last_name = last_name
        self._user_name = user_name
        self._chat_id = chat_id
        if member_since is not None:
            self.member_since = member_since
        else:
            self.member_since = "trigger setter"


    def full_name(self):
        last_name = " " + self.last_name if self.last_name != "" else ""
        return self.first_name + last_name

    @property
    def username(self):
        return str(self._user_name)

    @property
    def first_name(self):
        return self._first_name if self._first_name is not None else ""

    @property
    def last_name(self):
        return self._last_name if self._last_name is not None else ""

    @property
    def chat_id(self):
        return self._chat_id
    
    
    @property
    def member_since(self):
        return self._member_since

    @member_since.setter
    def member_since(self, value):
        value = datetime.datetime.now()
        self._member_since = value.strftime(DATE_FORMAT)


    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.member_since})"

    def __repr__(self):
        return f"<{self.chat_id}> {self.first_name} {self.last_name} ({self.member_since})"

    def __eq__(self, other):
        return self.chat_id == other.chat_id()

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.chat_id))

if __name__ == "__main__":
    
    my_user = User("Itai", None, "TuxoIC", 123231425)

    users = {}
    print("users before=", users)

    print(my_user.chat_id in users)

    users.update({my_user.chat_id: my_user.__dict__})
    print(my_user.chat_id in users)
    users.update({my_user.chat_id: my_user.__dict__})
    users.update({my_user.chat_id: my_user.__dict__})
    print(my_user.chat_id in users)
    print(my_user.member_since)
