import time
from SystemDetector import SystemDetector


class StartupScript:
    def __init__(self):
        while(True):
            # Decide OS
            system_detector = SystemDetector()
            time.sleep(2)
            # Start loop
            # Get time
            # Get user if logged in
            # Get picture
            # Get IP hopefully
            # Add to DB/storage
            # Try and call home


# Entry point
if __name__ == "__main__":
    StartupScript()
