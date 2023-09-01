import json
from user import User


class Utilities():

    def read_json(filename):
        try:
            f = open(filename, 'r')
            data = json.load(f)  # dictionary
            f.close()
        except FileNotFoundError:
            data = {}
        return data

    def write_to_json(filename, data):
        with open(filename, 'w') as outfile:
            outfile.seek(0)
            json.dump(data, outfile)

    def add_user(user, filename):
        dict = Utilities.read_json(filename)
        if str(user.chat_id) not in dict:
            dict.update({user.chat_id: user.__dict__})
            Utilities.write_to_json(filename, dict)

    def remove_user(user, filename):
        try:
            dict = Utilities.read_json(filename)
            dict.pop(str(user.chat_id))
            Utilities.write_to_json(filename, dict)
        except KeyError:
            pass  # user not found

    def _get_users(filename, json=False):
        ans = ""
        dict = Utilities.read_json(filename)
        if json:
            return dict
        for key in dict:
            u = User(dict[key]["_first_name"], dict[key]["_last_name"], dict[key]["_user_name"], dict[key]["_chat_id"])
            ans += u.__str__() + "\n"
        return ans
