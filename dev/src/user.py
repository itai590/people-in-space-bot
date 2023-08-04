import datetime
import utilities


class User:
    def __init__(self, first_name, last_name, user_name, chat_id):
        self._first_name = first_name
        self._last_name = last_name
        self._user_name = user_name
        self._chat_id = chat_id
        self.set_member_since()

    def full_name(self):
        last_name = " " + self.last_name() if self.last_name() != "" else ""
        return self.first_name() + last_name

    def username(self):
        return str(self._user_name)

    def first_name(self):
        return self._first_name if self._first_name is not None else ""

    def last_name(self):
        return self._last_name if self._last_name is not None else ""

    def chat_id(self):
        return self._chat_id

    def set_member_since(self):
        now = datetime.datetime.now()
        self._member_since = now.strftime(utilities.DATE_FORMAT)

    def member_since(self):
        return self._member_since

    def __str__(self):
        return f"{self.first_name()} {self.last_name()} ({self.member_since()})"

    def __repr__(self):
        return f"<{self.chat_id()}> {self.first_name()} {self.last_name()} ({self.member_since()})"

    def __eq__(self, other):
        return self.chat_id() == other.chat_id()

    def __hash__(self):
        return hash((self.first_name(), self.last_name(), self.chat_id()))


