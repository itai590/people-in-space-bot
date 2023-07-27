import logging
import sys


class Logger:

    def __init__(self) -> None:
        root = logging.getLogger()
        root.setLevel(logging.INFO)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        root.addHandler(handler)
        logging.info("setting logger")

    def log_info(self, msg):
        logging.info(msg)

    def log_err(self, msg):
        logging.error(msg)

    def log_user_call(self, first_name, last_name, username, id):
        logging.info('{} {} ({}) id:{} called'.format(
            first_name, str(last_name), username, id))
