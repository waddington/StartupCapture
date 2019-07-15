import time
import datetime
from SystemInformation.SystemDetector import SystemDetector
from SystemInformation.UserDetector import UserDetector
import os
import sys
import Logging.Logger


class StartupScript:
    def __init__(self):
        # self.__setup_logger()
        self.logger = Logging.Logger.get_logger(__name__)
        self.logger.info("Logger intialised.")
        self.__loop()

    def __loop(self):
        self.logger.info("Main loop starting")
        while(True):
            curr_time = datetime.datetime.fromtimestamp(
                time.time()).strftime('%Y-%m-%d %H:%M:%S')

            system_detector = SystemDetector()  # Detect OS info
            user_info = UserDetector(system_detector.get_os_name())

            self.logger.info("Reached end of loop.")
            time.sleep(2)
            # Get user if logged in
            # Get picture
            # Get IP hopefully
            # Add to DB/storage
            # Try and call home


# Entry point
if __name__ == "__main__":
    StartupScript()
