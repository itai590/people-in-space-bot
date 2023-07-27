import datetime
import utilities as util


class User:
    def __init__(self, first_name, last_name, chat_id):
        self._first_name = first_name
        self._last_name = last_name
        self._chat_id = chat_id
        now = datetime.datetime.now()
        self._member_since = now.strftime(util.DATE_FORMAT)

    def first_name(self):
        return self._first_name

    def last_name(self):
        return self._last_name

    def chat_id(self):
        return self._chat_id

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


if __name__ == "__main__":

    user = User("John", "Doe", "5555")
    print(user.member_since)
    print(user.chat_id())
    print(user.__hash__())
    print(user.__repr__())
    print(user.__str__())
    print(user.__eq__(user))
    print(user.__eq__(User("John", "Doe", "5555")))
    print(user.__eq__(User("John", "Doe", "5556")))
    print(user)