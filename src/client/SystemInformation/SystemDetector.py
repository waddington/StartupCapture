import platform
import os
import sys
import Logging.Logger


class SystemDetector:

    def find_linux_distro(self):
        try:
            return platform.linux_distribution()
        except:
            return None

    def find_os_name(self):
        if sys.platform == "linux" or sys.platform == "linux2":
            return "linux"  # linux
        elif sys.platform == "darwin":
            return "osx"  # osx
        elif sys.platform == "win32":
            return "windows"  # windows
        return None

    def get_os_name(self):
        return self.os_name

    def __init__(self):
        self.logger = Logging.Logger.get_logger(__name__)
        self.logger.info("Getting system information.")
        self.python_version = sys.version.split("\n")
        self.dist = str(platform.dist())
        self.linux_dist = self.find_linux_distro()
        self.system = platform.system()
        self.machine = platform.machine()
        self.platform = platform.platform()
        self.uname = platform.uname()
        # self.users
        self.version = platform.version()
        self.os_name = self.find_os_name()
        self.info = [
            ("Python Version", self.python_version),
            ("Distro", self.dist),
            ("Linux Distro", self.linux_dist),
            ("System", self.system),
            ("Machine", self.machine),
            ("Platform", self.platform),
            ("Uname", self.uname),
            ("Platform version", self.version),
            ("OS Name", self.os_name)
        ]
        self.logger.info("System Information: <{}>".format(self.info))
