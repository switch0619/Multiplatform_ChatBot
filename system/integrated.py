import subprocess
from config import shell_set as shell_set
subprocess.run(['core_discord.py'], shell=shell_set)
subprocess.run(['core_telegram.py'], shell=shell_set)