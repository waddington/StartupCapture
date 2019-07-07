import platform
import os
import sys


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

    def __init__(self):
        self.python_version = sys.version.split("\n")
        self.dist = str(platform.dist())
        self.linux_dist = self.find_linux_distro()
        self.system = platform.system()
        self.machine = platform.machine()
        self.platform = platform.platform()
        self.uname = platform.uname()
        # self.users
        self.version = platform.version()
        self.mac_ver = platform.mac_ver()
        self.os_name = self.find_os_name()
