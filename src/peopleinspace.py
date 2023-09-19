import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from utilities import Utilities as util

URL = "https://www.howmanypeopleareinspacerightnow.com/"

WINDOW_SIZE = "1920,1080"
FLAGS_FILE = "./src/flags.json"


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
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("enable-automation")
    chrome_options.add_argument("--dns-prefetch-disable")
    chrome_options.add_argument("--disable-gpu")

    # Capabilities
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "normal"  # complete
    # caps["pageLoadStrategy"] = "eager"  #  interactive
    # caps["pageLoadStrategy"] = "none"
    driver = webdriver.Chrome(desired_capabilities=caps, options=chrome_options)

    # Start timer
    start_time = time.time()

    # Fetch
    driver.get(URL)
    # time.sleep(2)

    # Scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(5)

    # End timer
    end_time = time.time()
    fetch_time = end_time - start_time
    fetch_time = "\n\n🕒 Fetch time: " + str(round(fetch_time, 3)) + " seconds"

    # Parse
    html = BeautifulSoup(driver.page_source, 'lxml')

    # Close driver
    driver.quit()

    # Find people in space count
    people_in_space = html.h1.get_text()  # html.find('a', id="container").h1.get_text()

    if number_only:
        return people_in_space + fetch_time

    # Find people in space details
    persons = html.find('div', id='listing')

    # Build output
    i = 1
    output = "🚀   🪐  🌍     " + str(people_in_space) + "   🧑‍🚀🧑‍🚀\n"
    for person in persons:

        # Skip first element
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

    # Replace long titles
    output = output.replace("Engineer", "Eng.")
    output = output.replace("Commander", "Cmdr.")
    output = output.replace("Colonel", "Col.")
    output = output.replace("Lieutenant", "Lt.")
    output = output.replace("Flight", "FLT")
    output += fetch_time
    return output


if __name__ == "__main__":
    print(scrape())
