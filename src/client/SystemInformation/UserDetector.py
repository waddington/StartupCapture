import Logging.Logger
import pwd
import grp
import os


class UserDetector:

    def is_unix(self, os):
        return os is 'linux'

    def get_unix_users(self):
        users = []
        for p in pwd.getpwall():
            users.append((p[0], grp.getgrgid(p[3])[0]))
        users.sort(key=lambda tup: tup[0])
        return users

    def get_unix_user(self):
        return os.popen("whoami").read().strip()

    def get_win_users(self):
        return None

    def get_win_user(self):
        return None

    def __init__(self, os):
        self.logger = Logging.Logger.get_logger(__name__)
        if self.is_unix(os):
            self.users = self.get_unix_users()
            self.current_user = self.get_unix_user()
        else:
            self.users = self.get_win_users()
            self.current_user = self.get_win_user()
        self.logger.info("User Information: <{}>".format(self.users))
        self.logger.info("Current User: <{}>".format(self.current_user))
