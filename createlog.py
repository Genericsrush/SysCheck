# Title: Create log
# Author: Macray Keeper
# Date: Feb 3, 2025
# Description: Creates log from the system check program and exports it into a txt file with the date and time.

# Module imports
import os
from datetime import datetime

# Creates the logs folder if one doesn't already exist.
if not (os.path.exists("./logs")):
    os.mkdir("./logs")

# Date time call for current date and time.
dt = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

# Uses a system command to run system check program and logs the contents into a log file based on current date and time.
os.system("python syscheck.py > .\logs\syslog{0}.txt".format(dt))