

def add_user(user, dict):
    dict.update({user.chat_id(): user.__dict__})


def remove_user(user, dict):
    try:
        dict.pop(user.chat_id())
    except KeyError:
        pass  # user not found


if __name__ == "__main__":
    users = {"a": {
        "_first_name": "Itai",
        "_last_name": None,
        "_user_name": "TuxoIC",
        "_chat_id": 123231425,
        "_member_since": "01.06.2019"
    }
    }
    print("users before=", users)  
    users.update({"a": {
        "_first_name": "Itai",
        "_last_name": None,
        "_user_name": "TuxoIC",
        "_chat_id": 123231425,
        "_member_since": "01.08.2023"
    }})
    print("users after=", users)

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
