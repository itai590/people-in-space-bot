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

    def log_user_call(self, u):
        logging.info('{} {} ({}) id:{} called'.format(
            u.first_name(), str(u.last_name()), u.username(), u.id()))

    def log_subscription_event(self, user, subscribe=True):
        action_txt = "SUBSCRIBE" if subscribe else "UN-SUBSCRIBE"
        self.log_info(f"{action_txt} {user.full_name()} <{user._chat_id}>")

    def log_subscription_event_to_file(logfile, user, subscribe=True):
        # format = "SUBSCRIBE (fullName:"+ fullName + ", chatId:" + chatId + ")\n"
        f = open(logfile, "a")
        action_txt = "SUBSCRIBE" if subscribe else "UN-SUBSCRIBE"
        output = f"{action_txt} {user.full_name()} <{user._chat_id}>\n"
        f.write(output)
        f.close()
