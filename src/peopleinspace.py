import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.utilities import Utilities as util

URL = "https://www.howmanypeopleareinspacerightnow.com/"

WINDOW_SIZE = "1920,1080"
FLAGS_FILE = "flags.json"


def search(dict, searchFor):
    searchFor = searchFor.lower()
    for k in dict:
        if searchFor in k.lower():
            return dict.get(k)
    return None


def scrape(number_only=False):
    flags = util.read_json(FLAGS_FILE)  # dictionary

    # Options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(URL)
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    html = BeautifulSoup(driver.page_source, 'lxml')

    # print(html)
    # print(html.prettify())

    people_in_space = html.h1.get_text()  # html.find('a', id="container").h1.get_text()
    if number_only:
        return people_in_space
    
    persons = html.find('div', id='listing')

    i = 1
    output = "🚀   🪐  🌍     " + str(people_in_space) + "   🧑‍🚀🧑‍🚀\n"
    for person in persons:

        if i != 1:
            output += "\n"

        person_name = person.h2.get_text()
        person_craft = person.h3.get_text()
        person_days = person.h4.get_text()
        person_flag = person.find('img').get('alt')
        person_flag = person_flag.replace("Flag of ", "")
        person_flag = search(flags, person_flag)

        output += str(i) + "." + person_name + person_flag + " - " + person_craft + " - " + person_days
        i += 1

    output = output.replace("Engineer", "Eng.")
    output = output.replace("Commander", "Cmdr.")
    output = output.replace("Colonel", "Col.")
    output = output.replace("Lieutenant", "Lt.")
    output = output.replace("Flight", "FLT")

    return output