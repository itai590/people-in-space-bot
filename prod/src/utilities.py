import json


DATE_FORMAT = '%d.%m.%Y'


class Utilities():

    def read_json(filename):
        f = open(filename, 'r')
        data = json.load(f)  # dictionary
        f.close()
        return data

    def write_to_json(filename, data):
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)
            

    def add_user(user, filename):
        dict = Utilities.read_json(filename)
        dict.update({user.chat_id(): user.__dict__})
        Utilities.write_to_json(filename, dict)

    def remove_user(user, filename):
        try:
            dict = Utilities.read_json(filename)
            dict.pop(user.chat_id())
            Utilities.write_to_json(filename, dict)
        except KeyError:
            pass  # user not found

    def _get_users(filename):
        dict = Utilities.read_json(filename)
        return dict.values()
