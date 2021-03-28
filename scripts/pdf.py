import os
import subprocess
import shutil
from sys import argv, stdout, stderr, exit

from toolbox import print, println, slurp_file, panic

#---------- CONSTANTS ----------#

FORMAT_NAME = "PDF"
BUILD_COMMAND = 'xelatex -interaction=nonstopmode %s'
BUILD_DIR = 'builds/pdf/'

#---------- PROCEDURES ----------#

def setup():
    try:
        os.mkdir(BUILD_DIR)
    except FileExistsError:
        pass

def build_file(path: str) -> None:
    path_ = f'\"{path}\"'
    nm = os.path.basename(path).replace('.tex', '') + '.pdf'

    res1 = subprocess.run(BUILD_COMMAND % (path_), shell=True)
    res2 = subprocess.run(BUILD_COMMAND % (path_), shell=True) # index

    if res1.returncode + res2.returncode == 0:
        shutil.move(nm, BUILD_DIR + nm)