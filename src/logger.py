import datetime
import logging
import sys


class Logger:

    def set_logger():
        root = logging.getLogger()
        root.setLevel(logging.INFO)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        root.addHandler(handler)
        logging.info("setting logger")
        return root

    def log_info(msg):
        logging.info(msg)

    def log_err(msg):
        logging.error(msg)

    def log_user_call(u, command):
        logging.info('{} {} ({}) id:{} called - {}'.format(
            u.first_name, str(u.last_name), u.username, u.chat_id, command))

    def log_subscription_event(logfile, user, subscribe=True):
        '''
        logs subscription event event to a file and stdout
        format = "SUBSCRIBE (fullName:"+ fullName + ", chatId:" + chatId + ")\n"
        '''
        action_txt = "SUBSCRIBE" if subscribe else "UN-SUBSCRIBE"
        log_txt = f"{action_txt} {user.full_name()} ({user.username}) <{user.chat_id}>"
        Logger.log_info(log_txt)
        dateandtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f = open(logfile, "a")
        f.write(dateandtime + " " + log_txt)
        f.write("\n")
        f.close()
        
        
    def abort(abort_msg, log=True):
        if log:
            logging.info(abort_msg)
            logging.info("aborting\n")
        exit()

