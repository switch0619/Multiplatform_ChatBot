import subprocess
from config import shell_set as shell_set
subprocess.call(['python','system/core_discord.py'], shell=shell_set)
subprocess.call(['python','system/core_telegram.py'], shell=shell_set)