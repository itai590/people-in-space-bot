###### wrapperapiopennotify ######
import json

import requests

SETTINGS_JSON = "settings.json"
FLAGS_FILE = "src/flags.json"
json_file_key = "jsonFile"


def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


def search_flag(flags_dict, country_name):
    country_name = country_name.lower()
    for key in flags_dict:
        if country_name in key.lower():
            return flags_dict.get(key)
    return ''


def scrape(number_only=False):
    flags = read_json(FLAGS_FILE)  # dictionary

    # Fetch data from the API
    response = requests.get('http://api.open-notify.org/astros.json')
    data = response.json()

    people_in_space = data['number']
    astronauts = data['people']

    output = "🚀   🪐  🌍     " + str(people_in_space) + "   🧑‍🚀🧑‍🚀\n"
    for idx, person in enumerate(astronauts, 1):
        name = person['name']
        craft = person['craft']

        # Example mapping of craft to countries (you may need to adjust this)
        craft_country_mapping = {
            'ISS': 'International',
            'Tiangong': 'China',
            # Add more mappings if necessary
        }
        country_name = craft_country_mapping.get(craft, 'International')
        flag = search_flag(flags, country_name)

        # Since the API doesn't provide 'days in space', we can omit it or fetch from another source
        person_days = ''  # Placeholder or fetch from another source if available

        if idx != 1:
            output += "\n"

        output += f"{idx}.{name}{flag} - {craft} - {person_days}"

    # Replace titles as in your original code
    output = output.replace("Engineer", "Eng.")
    output = output.replace("Commander", "Cmdr.")
    output = output.replace("Colonel", "Col.")
    output = output.replace("Lieutenant", "Lt.")
    output = output.replace("Flight", "FLT")
    return output


def write_output_to_file(output, people_in_space):
    settings = read_json(SETTINGS_JSON)

    # Write to the output file specified in settings
    output_file = settings.get(json_file_key, 'output.txt')
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(f"🚀   🪐  🌍     {people_in_space}   🧑‍🚀🧑‍🚀\n")
        outfile.write(output)


if __name__ == '__main__':
    print(scrape())
