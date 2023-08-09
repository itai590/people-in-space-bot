from src.utilities import Utilities as Util
from src.user import User


def add_user(user, dict):
    dict.update({user.chat_id(): user.__dict__})


def remove_user(user, dict):
    try:
        dict.pop(user.chat_id())
    except KeyError:
        pass  # user not found


if __name__ == "__main__":

    # python -m tests.test_subscription

    my_user = User("Itai", None, "TuxoIC", 123231425)

    users = {}
    print("users before=", users)

    print(my_user.chat_id in users)

    users.update({my_user.chat_id: my_user.__dict__})
    print(my_user.chat_id in users)
    users.update({my_user.chat_id: my_user.__dict__})
    users.update({my_user.chat_id: my_user.__dict__})
    print(my_user.chat_id in users)

    print("users after=", users)

    users.pop(my_user.chat_id)
    print(my_user.chat_id in users)

    print("users after=", users)

    for k in users:
        print(k, users[k])

    # users.update({"123231425": {
    #     "_first_name": "Itai",
    #     "_last_name": None,
    #     "_user_name": "TuxoIC",
    #     "_chat_id": 123231425,
    #     "_member_since": "01.08.2023"
    # }})

    # users.update({"12323425": {
    #     "_first_name": "Itai",
    #     "_last_name": None,
    #     "_user_name": "TuxoIC",
    #     "_chat_id": 123231425,
    #     "_member_since": "01.08.2023"
    # }})

    # print("users after=", users)

    # my_dict = {'a':1,'b':2,'c':3,'d':4}
    # print(my_dict)
    # my_dict.update({'a':1})
    # my_dict.update({'a':1})
    # my_dict.update({'a':1})
    # my_dict.update({'a':1})
    # my_dict.update({'tt':1})
    # print(my_dict)

    # my_dict.pop('a')
    # my_dict.update({'a':1})
