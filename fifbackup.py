#!/usr/bin/python3

"""simple backup script written in python to backup files from linux to AWS/Dropbox/GPC"""

from fifbackuplib.config import Config

def main():

    """main function"""

    config = Config()

    print(config.dirs)
    print(config.targets)

main()
