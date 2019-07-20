# encoding: utf-8
import subprocess
from system.config import shell_set as shell_set
subprocess.call(['python','system/integrated.py'], shell=shell_set, encoding='utf-8')
