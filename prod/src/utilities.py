

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
