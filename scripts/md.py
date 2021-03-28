import os
import shutil
import subprocess
from sys import argv, stdout, stderr, exit

from toolbox import print, println, slurp_file, panic

#---------- CONSTANTS ----------#

FORMAT_NAME = "Markdown"
BUILD_COMMAND = 'pandoc --columns=10000 -s %s -o %s'
BUILD_DIR = 'builds/md/'

#---------- PROCEDURES ----------#

def setup():
    try:
        os.mkdir(BUILD_DIR)
    except FileExistsError:
        pass

def build_file(path: str) -> None:
    path_ = f'\"{path}\"'
    nm = os.path.basename(path).replace('.tex', '') + '.md'
    name = f'\"{nm}\"'

    res = subprocess.run(BUILD_COMMAND % (path_, name), shell=True)

    if res.returncode == 0:
        shutil.move(nm, BUILD_DIR + nm)